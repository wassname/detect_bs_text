# Experiment using LLM's to detect BS writing


An experiment to see if I can detect "BS" using LLM's in a robust way.

It's impossible to detect AI generated text with 100% accuracy. But we will have more success detecting bad, empty, or contentless text. 

Why might this work? As with [Schmidhuber's definition of curiosity](https://arxiv.org/abs/0812.4360) good writing should initially suprise the reader but become less suprising as they learn about it. Empty writing is not suprising. And confusing writing stays confusing even after you have read it. In other words it should have a high perplexity, which goes down after learning it. 

The ideal way to do this would be by fine tuning. But that would be momory intensive so I will try and do it with prompts. I ask:
- Is the text suprising (high perplexity)
- Is less suprising when given a summary? (low perplexity)

If yes/yes then it's may be suprising new information. If either is not true, then it's proboably BS.

See main.ipynb
