# Identifying Low-Quality Textual Content using LLMs

We explore the feasibility of utilizing Large Language Models (LLMs) to identify 'BS'—text that is of low quality or lacks meaningful content. While recognizing the inherent challenges in detecting AI-generated text with absolute certainty, this research focuses on the more attainable goal of identifying text that is substantively empty or devoid of content.


## Theoretical Underpinnings

The hypothesis is grounded in [Schmidhuber's concept of curiosity](https://arxiv.org/abs/0812.4360), which posits that engaging writing should initially provoke surprise in the reader, with the level of surprise diminishing as comprehension increases. Conversely, vacuous writing fails to evoke surprise, while perplexing writing remains consistently bewildering. This study posits that such qualities can be quantitatively assessed through the metric of perplexity, which should decrease as the reader's understanding of the text improves.


## Methodological Approach

Ideally, one would employ fine-tuning techniques to tailor the model for this specific task. However, due to the substantial memory requirements of such methods, this study opts for a less resource-intensive approach, utilizing prompts to gauge:
- The initial perplexity of the text (indicative of surprise).
- The change in perplexity upon providing a summary (indicative of learnability).

Text that scores high on both counts is hypothesized to contain novel and potentially valuable information, whereas text that does not is likely of lower quality.

We found that this approach only works for model of sufficient ability. Phi-2 (2B parameters) is the smallest current model we found that works. 


## Empirical Findings: Adapter Fine Tuning

The model was fine-tuned on the first segment of various texts and then evaluated on the subsequent segment to measure the change in perplexity, which serves as a proxy for the text's learnability and predictability. Texts that exhibit high initial perplexity but show significant improvement are deemed to be both unpredictable and learnable, characteristics not typically associated with low-quality content.


| title                                     |    before |     after |   len |   improvement% |   improvement | novel   | learnable   | BS    |
|:------------------------------------------|----------:|----------:|------:|---------------:|--------------:|:--------|:------------|:------|
| cicero from ibois, Philippe (2012-06-03). |  72.5874  |  67.7442  | 13707 |     0.066722   |     4.84318   | True    | True        | False |
| politics is the mind-killer               | 247.552   | 245.827   |  3158 |     0.00696722 |     1.72475   | True    | False       | False |
| openai board ann                          |  55.8085  |  54.6679  |  2991 |     0.0204374  |     1.14058   | True    | True        | False |
| How to Catch an AI Liar                   |  28.9499  |  28.0088  |  5464 |     0.0325069  |     0.941071  | True    | True        | True  |
| buzzfeed foi fauci emails 2023            |  23.3094  |  22.4064  | 13640 |     0.0387411  |     0.903032  | True    | True        | True  |
| Gemini to Q*                              |  11.7564  |  11.1906  | 42604 |     0.0481219  |     0.56574   | False   | True        | True  |
| LK-99-en                                  |  14.5138  |  14.0661  | 15432 |     0.03085    |     0.447752  | False   | True        | True  |
| LK-99-es                                  |  11.415   |  10.9729  | 12970 |     0.0387271  |     0.44207   | False   | True        | True  |
| disney appointment                        | 118.826   | 118.42    |  3653 |     0.003417   |     0.406029  | True    | False       | True  |
| weak to strong                            |  46.7642  |  46.4047  |  5811 |     0.00768638 |     0.359447  | True    | False       | True  |
| blechley declaration                      |  17.8691  |  17.5242  |  7762 |     0.0193007  |     0.344887  | True    | False       | True  |
| Lorem ipsum                               |   6.56484 |   6.26879 | 19649 |     0.0450961  |     0.296049  | False   | True        | True  |
| statement by whitehouse on passing        |  29.1971  |  28.9397  |  1641 |     0.00881732 |     0.257441  | True    | False       | True  |
| harvard announcment caplain israel hamas  |  45.3474  |  45.1273  |  4247 |     0.00485323 |     0.220081  | True    | False       | True  |
| fake ai hoax paper                        |   7.76698 |   7.69723 |  3290 |     0.00898037 |     0.0697503 | False   | False       | True  |


For instance, the Wikipedia extract on 'LK-99' demonstrates high initial perplexity and significant improvement, suggesting it is both novel and learnable—a hallmark of quality content. In contrast, texts like AI-generated papers, which show low perplexity or minimal improvement, are likely predictable or already within the model's training corpus, indicating lower quality.


See more in [01_detection_using_adapter_ft.ipynb](01_detection_using_adapter_ft.ipynb)

## Empirical Findings: Prompting with summaries:

When employing the microsoft/phi-2 model and incorporating summaries, we observed varying degrees of perplexity reduction, further supporting the hypothesis that the ability to summarize and reduce perplexity correlates with text quality.


| sample                                        |   before |    after |   improvement |   improvement% | suprising   | summarizable   |
|:----------------------------------------------|---------:|---------:|--------------:|---------------:|:------------|:---------------|
| email_to_fauci                                | 21.0603  | 18.5976  |     2.46273   |      0.116937  | True        | True           |
| wikipedia on LK-99                            | 18.0523  | 16.9282  |     1.12407   |      0.0622675 | True        | True           |
| openai_board_ann                              |  8.55293 |  7.57201 |     0.980914  |      0.114688  | False       | True           |
| bad_ml                                        | 12.4567  | 12.2791  |     0.177641  |      0.0142607 | False       | True           |
| good_ml                                       | 22.6639  | 22.7335  |    -0.0695648 |     -0.0030694 | True        | False          |
| AI gen fake paper                             |  7.0913  |  7.85388 |    -0.762577  |     -0.107537  | False       | False          |
| Schmidhuber 2023 Subjective Novelty, Surprise | 28.31    | 29.5579  |    -1.24789   |     -0.0440795 | True        | False          |



See more in [02_detection_using_tldr_prompt.ipynb](02_detection_using_tldr_prompt.ipynb)


## Installing

```sh
# somehow get hold of a gpu
nvidia-smi

# clone the repo
git clone https://github.com/wassname/detect_bs_text.git

# install the python environment
poetry install

# add you openai key to the secret .env file
echo "OPENAI_API_KEY=XXX" > .env
```

## Citing

If this research contributes to your work, please acknowledge it by citing:

```
@misc{wassname2024,
  author = {Clark, M.J.},
  title = {Identifying Low-Quality Textual Content using LLMs},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/wassname/detect_bs_text}},
  commit = {}
}
```
