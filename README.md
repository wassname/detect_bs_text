# Experiment using LLM's to detect BS writing


An experiment to see if I can detect "BS" using LLM's in a robust way.

It's impossible to detect AI generated text with 100% accuracy. But we will have more success detecting bad, empty, or contentless text. 

Why might this work? As with [Schmidhuber's definition of curiosity](https://arxiv.org/abs/0812.4360) good writing should initially suprise the reader but become less suprising as they learn about it. Empty writing is not suprising. And confusing writing stays confusing even after you have read it. In other words it should have a high perplexity, which goes down after learning it. 

The ideal way to do this would be by fine tuning. But that would be momory intensive so I will try and do it with prompts. I ask:
- Is the text suprising (high perplexity)
- Is less suprising when given a summary? (low perplexity)

If yes/yes then it's may be suprising new information. If either is not true, then it's proboably BS.

See [main.ipynb](main.ipynb) for the code and results.


# Results

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
