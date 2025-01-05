# 2024-01-03 18:57:01

Initial version

- added large docs. But not the results don't make sense. I think I have a problem where the first and latter half of the docs are diff
  - [ ] I need to window, then spit into train and test


# 2025-01-01 12:19:33

I need more examples, and I need to rate them so I can get a single metric

I need to choose things after the base model was trained because
- the theory of relativity was novel at the time but it now

I need to make it conditional on context. Because the theory of relativity is not novel in way that's relevent to a poetry journal



Q? Which base model? I can only use a small model on my 3090ti. So <3b at half precision, or 8b at bnb 8 bit precision?
I was using phi-2 which is 3b. I should switch to the best of size, or the most open (tinyllama or the eleuther one)
the only problem is that so called base models appear to be post trainer not just perplexity?

Gwern notes this is slop https://www.lesswrong.com/posts/Rk2o8hjYmjENH8zs6/deontic-explorations-in-paying-to-talk-to-slaves
Good https://www.narrowpath.co/phase-1
good https://www.lesswrong.com/posts/fAW6RXLKTLHC3WXkS/shallow-review-of-technical-ai-safety-2024#comments
very good as it has multiple authors https://www.lesswrong.com/posts/KFFaKu27FNugCHFmh/by-default-capital-will-matter-more-than-ever-after-agi
ok https://www.dwarkeshpatel.com/p/notes-on-china?triedRedirect=true
very good https://www.lesswrong.com/posts/nAsMfmxDv6Qp7cfHh/fabien-s-shortform?commentId=gGDAXomb2ihucF4Ls
good  https://github.com/dottxt-ai/outlines
good https://arxiv.org/abs/2312.02179

I can also ask an llm how suprising it is, and how much it learned from the prompt. or even just how novel

I should use LLM's trained before 2024. In deployment how would I know if the llm has seen it... maybe it's OK to know if but we can look 

I'd like to try a range of methods
- please rate how novel this is on a scale of 1-5 where 0 is spam and 5 is the theory of relativity
- text -> tldr -> reconstruct
- try learning the text with X and then measuring it with Y
  - X
    - fine tune
    - prompt
  - Y
    - perplexity
    - rating
- try using a base model vs a calibrated instruct model (since thier outputs have been changed since they were trained on perplexity)

# Data
Data Freshness: The pretraining data has a cutoff of December 2023.

So for each peice of text I need to know
- when it was written
- context
- most similar thing from search?
- my own rating of how novel it WAS, for the context
- and perplexity

I'll use markdown with yaml front matter



| cicero from ibois, Philippe (2012-06-03). 
| politics is the mind-killer               
| openai board ann                          
| How to Catch an AI Liar                   
| buzzfeed foi fauci emails 2023            
| Gemini to Q*                              
| LK-99-en                                  
| LK-99-es                                  
| disney appointment                        
| weak to strong                            
| blechley declaration                      
| Lorem ipsum                               
| statement by whitehouse on passing        
| harvard announcment caplain israel hamas  
| fake ai hoax paper                        


trumps announcements
latest meta papers e.g. blt
- 2023-11-20 Gwern predicts how o1 works https://old.reddit.com/r/mlscaling/comments/1gur5ys/stream_of_search_sos_learning_to_search_in/ly1ev55/ 
- 2024-12-09 FAIR  COCONUT https://arxiv.org/abs/2412.06769
- 
- 2024-12-11 semianalysis on o1 https://semianalysis.com/2024/12/11/scaling-laws-o1-pro-architecture-reasoning-training-infrastructure-orion-and-claude-3-5-opus-failures/
- 2024-12-16 H4: A replication of using a process control reward model to bootstrap https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute 
o3 announcemenbt https://arcprize.org/blog/oai-o3-pub-breakthrough
deliberative alignment https://openai.com/index/deliberative-alignment/

semianalyss
https://www.manifold1.com/episodes/huawei-and-the-us-china-chip-war-44/transcript


# open questions

What about a form which is 99% spam but 1% theory of relativity?
What about the theory of relativity in a poetry journal?
What about the theory of relativity but it's copied?

