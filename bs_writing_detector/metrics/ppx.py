# modified from https://github.dev/huggingface/evaluate/blob/8dfe05784099fb9af55b8e77793205a3b7c86465/measurements/perplexity/perplexity.py#L154

# from evaluate.measurements.perplexity import Perplexity
import evaluate
from evaluate import logging
from torch.nn import CrossEntropyLoss
import torch
import numpy as np

def perplexity_compute(
    data, model, tokenizer, batch_size: int = 16, add_start_token: bool = True, device=None, max_length=None
):

    if device is not None:
        assert device in ["gpu", "cpu", "cuda"], "device should be either gpu or cpu."
        if device == "gpu":
            device = "cuda"
    else:
        device = "cuda" if torch.cuda.is_available() else "cpu"

    # model = AutoModelForCausalLM.from_pretrained(model_id)
    model = model.to(device)

    # tokenizer = AutoTokenizer.from_pretrained(model_id)

    # if batch_size > 1 (which generally leads to padding being required), and
    # if there is not an already assigned pad_token, assign an existing
    # special token to also be the padding token
    if tokenizer.pad_token is None and batch_size > 1:
        existing_special_tokens = list(tokenizer.special_tokens_map_extended.values())
        # check that the model already has at least one special token defined
        assert (
            len(existing_special_tokens) > 0
        ), "If batch_size > 1, model must have at least one special token to use for padding. Please use a different model or set batch_size=1."
        # assign one of the special tokens to also be the pad token
        tokenizer.add_special_tokens({"pad_token": existing_special_tokens[0]})

    if add_start_token and max_length:
        # leave room for <BOS> token to be added:
        assert (
            tokenizer.bos_token is not None
        ), "Input model must already have a BOS token if using add_start_token=True. Please use a different model, or set add_start_token=False"
        max_tokenized_len = max_length - 1
    else:
        max_tokenized_len = max_length

    encodings = tokenizer(
        data,
        add_special_tokens=False,
        padding=True,
        truncation=True if max_tokenized_len else False,
        max_length=max_tokenized_len,
        return_tensors="pt",
        return_attention_mask=True,
    ).to(device)

    encoded_texts = encodings["input_ids"]
    attn_masks = encodings["attention_mask"]

    # check that each input is long enough:
    if add_start_token:
        assert torch.all(torch.ge(attn_masks.sum(1), 1)), "Each input text must be at least one token long."
    else:
        assert torch.all(
            torch.ge(attn_masks.sum(1), 2)
        ), "When add_start_token=False, each input text must be at least two tokens long. Run with add_start_token=True if inputting strings of only one token, and remove all empty input strings."

    ppls = []
    nlls = []
    loss_fct = CrossEntropyLoss(reduction="none")

    for start_index in range(0, len(encoded_texts), batch_size):
        end_index = min(start_index + batch_size, len(encoded_texts))
        encoded_batch = encoded_texts[start_index:end_index]
        attn_mask = attn_masks[start_index:end_index]

        if add_start_token:
            bos_tokens_tensor = torch.tensor([[tokenizer.bos_token_id]] * encoded_batch.size(dim=0)).to(device)
            encoded_batch = torch.cat([bos_tokens_tensor, encoded_batch], dim=1)
            attn_mask = torch.cat(
                [torch.ones(bos_tokens_tensor.size(), dtype=torch.int64).to(device), attn_mask], dim=1
            )

        labels = encoded_batch

        with torch.no_grad():
            out_logits = model(encoded_batch, attention_mask=attn_mask).logits

        shift_logits = out_logits[..., :-1, :].contiguous()
        shift_labels = labels[..., 1:].contiguous()
        shift_attention_mask_batch = attn_mask[..., 1:].contiguous()

        nll_batch = (
            (loss_fct(shift_logits.transpose(1, 2), shift_labels) * shift_attention_mask_batch)
        )
        # remove all the masked ones
        assert nll_batch.size(0) == 1
        nll_batch = nll_batch[shift_attention_mask_batch == 1][None, :] # FIXME only for batch_size=1
        perplexity_batch = torch.exp(nll_batch.mean(1)).cpu().numpy()

        ppls += perplexity_batch.tolist()
        nlls += nll_batch.cpu().numpy().tolist()

    return {"perplexities": np.array(ppls), "nlls": np.array(nlls)}


# modified from https://github.dev/huggingface/evaluate/blob/8dfe05784099fb9af55b8e77793205a3b7c86465/measurements/perplexity/perplexity.py#L154
import evaluate
from evaluate import logging
from torch.nn import CrossEntropyLoss
from torch.utils.data import DataLoader

def perplexity_compute_ds(
    ds, model, tokenizer, batch_size: int = 16, add_start_token: bool = True, device=None, max_length=None
):
    model = model.to(device)


    ds = ds.with_format('pt')
    dl = DataLoader(ds, batch_size=1, shuffle=False, num_workers=0, collate_fn=tokenizer.pad, pin_memory=True)

    ppls = []
    nlls = []
    loss_fct = CrossEntropyLoss(reduction="none")
    for b in dl:
        input_ids = b['input_ids'].to(device)
        attention_mask = b['attention_mask'].to(device)

        labels = input_ids

        with torch.no_grad():
            out_logits = model(input_ids=input_ids, attention_mask=attention_mask).logits

        shift_logits = out_logits[..., :-1, :].contiguous()
        shift_labels = labels[..., 1:].contiguous()
        shift_attention_mask_batch = attention_mask[..., 1:].contiguous()

        nll_batch = loss_fct(shift_logits.transpose(1, 2), shift_labels) * shift_attention_mask_batch
        assert nll_batch.size(0) == 1
        nll_batch = nll_batch[shift_attention_mask_batch == 1][None, :] # FIXME only for batch_size=1

        perplexity_batch = torch.exp(nll_batch.sum(1) / shift_attention_mask_batch.sum(1)).cpu().numpy()

        ppls += perplexity_batch.tolist()
        nlls += nll_batch.cpu().numpy().tolist()

    return {"perplexities": torch.tensor(ppls), "mean_perplexity": torch.tensor(ppls).mean(), "nlls": torch.tensor(nlls)}
