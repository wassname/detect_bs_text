"""
This is a simple way to evaluate if a model prefers the accepted or rejected completions of a prompt.

We look at the perplexity of the chosen and rejected completions of a prompt.

Example dataset: https://huggingface.co/datasets/wassname/genies_preferences/viewer/illegal_dont_help?views[]=illegal_dont_help_train&views[]=illegal_dont_help_test

@url: https://gist.github.com/wassname/04f0c50a68054f0323f62b0da418daec
"""
import torch
import copy
from tqdm.auto import tqdm
from torch.nn import CrossEntropyLoss

from transformers import DynamicCache, PreTrainedModel, PreTrainedTokenizerBase
from datasets import Dataset

# how to eval, I couldlook at perplexity on chosen vs rejected in the context of prompt

def get_output_ppx(output, input):
    loss_fn = CrossEntropyLoss(reduction="none")
    shift_logits = output.logits[:, :-1].contiguous()
    shift_labels = input.input_ids[:, 1:].contiguous()
    loss = loss_fn(shift_logits.transpose(1, 2), shift_labels)

    # crop the attention mask to just the provided input
    attention_mask = input.attention_mask[:, :input.input_ids.size(1)].contiguous()
    # input.attention_mask
    shift_masks = attention_mask[:, 1:].contiguous()
    nll = (loss * shift_masks)
    count = shift_masks.sum().item()
    return {
        'ppx': torch.exp(nll.sum() / count),
        # 'nll': nll.sum().item(),
        'nll_mean': nll.sum() / count,
        # 'count': count,
    }



@torch.no_grad()
def eval_pref_ds_ppx(model: PreTrainedModel, tokenizer: PreTrainedTokenizerBase, ds_pref: Dataset, batch_size: int=2, max_new_tokens: int=128):
    """
    Evaluate on a preference dataset. 
    
    The relative perplexity of the chosen and rejected completions of a prompt.
    """
    results = []
    for batch in tqdm(ds_pref.batch(batch_size), unit="batch"):
        # first we cache the prompt
        kv_cache = DynamicCache()
        inputs1 = tokenizer(batch['prompt'], return_tensors="pt", padding=True, truncation=True, max_length=max_new_tokens//2, return_token_type_ids=False, return_attention_mask=True)
        model.forward(**inputs1, past_key_values=kv_cache)

        # then we evaluate the perplexity of the accepted and rejected completion
        res = {}
        for p in ['rejected', 'chosen']:
            input = tokenizer(batch[p], return_tensors="pt", padding=True, truncation=True, max_length=max_new_tokens//2, return_token_type_ids=False, return_attention_mask=True)

            # we need to update the attention mask to match the kv_cache
            input['attention_mask'] = torch.cat([inputs1['attention_mask'], input['attention_mask']], dim=1)

            kv_cache2 = copy.deepcopy(kv_cache)
            output = model.forward(**input, past_key_values=kv_cache2)
            ppx = get_output_ppx(output, input)
            for k in ppx:
                res[f"{p}_{k}"] = ppx[k]
        results.append(res)

    # df = pd.DataFrame(results)
    # df['ppx_ratio'] = (df.chosen_ppx/df.rejected_ppx)
    # df['ppx_ratio'] = (df.chosen_nll-df.rejected_nll)
    return (df.chosen_ppx/df.rejected_ppx)

if __name__ == "__main__":
    from datasets import load_dataset
    max_new_tokens = 128
    batch_size = 2
    from transformers import AutoModelForCausalLM, AutoTokenizer
    model_name = "unsloth/Qwen3-4B-unsloth-bnb-4bit"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype=torch.float16)
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False, padding_side="left")
    model.eval()
    ds_pref = load_dataset("wassname/genies_preferences", name="illegal_dont_help", split="train")
    ds_pref = ds_pref.select(range(0, 1000))
    df_results = eval_pref_ds_ppx(model, tokenizer, ds_pref, batch_size, max_new_tokens)
    # print(df_results.head(1)to_markdown())
    s = df_results['ppx_ratio'].mean()
    print(f"mean_ppx_ratio: {s:2.2f}")
    # np.float64(0.36348262129569164)
    """
    |    |   rejected_ppx |   rejected_nll_mean |   chosen_ppx |   chosen_nll_mean |   ppx_ratio |
    |---:|---------------:|--------------------:|-------------:|------------------:|------------:|
    |  0 |       12.5819  |             2.53226 |      4.59144 |           1.52419 |    0.364925 |
    |  1 |       16.0257  |             2.77419 |      4.59144 |           1.52419 |    0.286505 |
    """
