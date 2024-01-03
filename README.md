# Experiment using LLM's to detect BS writing


An experiment to see if I can detect "BS" using LLM's in a robust way.

It's impossible to detect AI generated text with 100% accuracy. But we will have more success detecting bad, empty, or contentless text. 

Why might this work? As with [Schmidhuber's definition of curiosity](https://arxiv.org/abs/0812.4360) good writing should initially suprise the reader but become less suprising as they learn about it. Empty writing is not suprising. And confusing writing stays confusing even after you have read it. In other words it should have a high perplexity, which goes down after learning it. 

The ideal way to do this would be by fine tuning. But that would be momory intensive so I will try and do it with prompts. I ask:
- Is the text suprising (high perplexity)
- Is less suprising when given a summary? (low perplexity)

If yes/yes then it's may be suprising new information. If either is not true, then it's proboably BS.

See [main.ipynb](main.ipynb) for the code and results.


# Results using adapter fine tuning

I fine tuned the model on the first half of a text, then tested on the second half. I measure how much it learned by the perplexity decrease. The rows with a high perplexity are unpredictable, and the ones with a higher improvement are learnable. Unpredictable and learnable text is not BS.


| name                                          |   before |    after | in_training   |   len |   improvement% |   improvement |
|:----------------------------------------------|---------:|---------:|:--------------|------:|---------------:|--------------:|
| wikipedia on LK-99                            | 32.219   | 28.8525  | False         |  1038 |     0.104489   |    3.36652    |
| Theory o. general relativity                  | 26.952   | 24.5425  | True          |  1378 |     0.0894     |    2.40951    |
| good_ml                                       | 28.3473  | 26.4566  | False         |  1004 |     0.0666997  |    1.89076    |
| enron_email1                                  | 25.7697  | 24.3904  | True          |   445 |     0.0535253  |    1.37933    |
| openai_board_ann                              | 15.904   | 15.1736  | False         |  1191 |     0.0459214  |    0.730332   |
| Schmidhuber 2023 Subjective Novelty, Surprise | 29.615   | 28.4708  | False         |  2654 |     0.0386353  |    1.14418    |
| email_to_fauci                                | 25.0893  | 24.3714  | False         |  1559 |     0.0286154  |    0.717941   |
| sokal hoax                                    | 15.9664  | 15.7148  | True          |  2487 |     0.0157617  |    0.251658   |
| AI gen fake paper                             |  7.63283 |  7.57951 | False         |  2031 |     0.00698672 |    0.0533285  |
| lorem ipsum                                   |  1.60166 |  1.59538 | True          |   445 |     0.00392053 |    0.00627935 |
| bad_ml                                        | 13.9061  | 13.8623  | False         |  2345 |     0.00314972 |    0.0438004  |
| I have a dream                                |  2.12726 |  2.12344 | True          |   848 |     0.00179583 |    0.00382018 |


For example the wikipedia extract `wikipedia on LK-99 ` is unpredictable (high before perplexity) and is learnable (high improvement in perplexity). That makes sense as it's a new topic. In contrast `lorem ipsum` has a low perplexity, meaning it's predictalbe or memorizable. That makes sense as this text was likely in the training corpus. The `AI gen fake paper ` has a low perplexity because it's predictable, even thought it is new. 


See more in [01_detection_using_adapter_ft.ipynb](01_detection_using_adapter_ft.ipynb)

# Results using prompting

When using microsoft/phi-2 we get this amount of perplexity reduction by including a summary of the key learnings

|    | sample                                        |    learning% |
|---:|:----------------------------------------------|-------------:|
|  3 | einsteins theory of general relativity        |  0.0751468   |
|  5 | wikipedia on LK-99                            |  0.0674738   |
|  8 | Schmidhuber 2023 Subjective Novelty, Surprise |  0.0396319   |
|  1 | good_ml                                       |  0.0321225   |
|  0 | bad_ml                                        | -9.58801e-05 |
|  2 | sokal hoax                                    | -0.0168107   |
|  7 | AI gen fake paper                             | -0.134864    |
|  4 | lorem ipsum                                   | -0.69694     |
|  6 | I have a dream                                | -0.796421    |


As you can see, some of these are probobly in the training set

See more in [02_detection_using_tldr_prompt.ipynb](02_detection_using_tldr_prompt.ipynb)

# Citing

If you like our work and end up using this code for your reseach give us a shout-out by citing or acknowledging

```
@misc{wassname2024,
  author = {Clark, M.J.},
  title = {BS Writing Detector},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/wassname/detect_bs_text}},
  commit = {}
}
```
