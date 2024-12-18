# Identifying Low-Quality Textual Content using LLMs

Can Large Language Models (LLMs) detect low quality text?. We do this by finding text that can "suprise" the model.


## Theoretical Underpinnings

The hypothesis is grounded in [Schmidhuber's concept of curiosity](https://arxiv.org/abs/0812.4360), which suggests that engaging writing should initially provoke surprise in the reader, with the level of surprise diminishing as comprehension increases. We test of these qualities can be quantitatively assessed through the metric of perplexity, which should decrease as the model's understanding of the text improves.


## Methodological Approach

Ideally, one would employ fine-tuning techniques to tailor the model for this specific task. However, due to the substantial memory requirements of such methods, this study opts for a less resource-intensive approach, utilizing prompts to gauge:
- The initial perplexity of the text (indicative of surprise).
- The change in perplexity upon providing a summary (indicative of learnability).

Text that scores high on both counts is hypothesized to contain novel and potentially valuable information, whereas text that does not is likely of lower quality.

We found that this approach only works for model of sufficient ability. Phi-2 (2B parameters) is the smallest current model we found that works. 


## Empirical Findings: Method 1, Adapter Fine Tuning (succeed)

The model was fine-tuned on the first segment of various texts and then evaluated on the subsequent segment to measure the change in perplexity, which serves as a proxy for the text's learnability and predictability. Texts that exhibit high initial perplexity but show significant improvement are deemed to be both unpredictable and learnable, characteristics not typically associated with low-quality content.


| name                                          |  before |   after | text length | improvement % | abs improvement | novel? | learnable? | High Quality?   |
| :-------------------------------------------- | ------: | ------: | ----------: | ------------: | --------------: | :----- | :--------- | :---- |
| wikipedia on LK-99                            |  32.219 | 28.8525 |        1038 |      0.104489 |         3.36652 | True   | True       | False |
| good_ml                                       | 28.3473 | 26.4566 |        1004 |     0.0666997 |         1.89076 | True   | True       | False |
| openai_board_ann                              |  15.904 | 15.1736 |        1191 |     0.0459214 |        0.730332 | True   | True       | True  |
| Schmidhuber 2023 Subjective Novelty, Surprise |  29.615 | 28.4708 |        2654 |     0.0386353 |         1.14418 | True   | True       | False |
| email_to_fauci                                | 25.0893 | 24.3714 |        1559 |     0.0286154 |        0.717941 | True   | True       | True  |
| AI gen fake paper                             | 7.63283 | 7.57951 |        2031 |    0.00698672 |       0.0533285 | False  | False      | True  |
| bad_ml                                        | 13.9061 | 13.8623 |        2345 |    0.00314972 |       0.0438004 | False  | False      | True  |


For instance, the Wikipedia extract on 'LK-99' demonstrates high initial perplexity and significant improvement, suggesting it is both novel and learnable—a hallmark of quality content. In contrast, texts like AI-generated papers, which show low perplexity or minimal improvement, are likely predictable or already within the model's training corpus, indicating lower quality.


See more in [01_detection_using_adapter_ft.ipynb](01_detection_using_adapter_ft.ipynb)

## Empirical Findings: Method 2, Prompting with summaries (fail):

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
