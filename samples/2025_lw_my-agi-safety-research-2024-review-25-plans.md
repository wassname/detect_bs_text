---
title: "My AGI safety research—2024 review, ’25 plans"
date: 2025-01-01 22:01:48.820000+00:00
url: https://www.lesswrong.com/posts/2wHaCimHehsF36av3/my-agi-safety-research-2024-review-25-plans
novelty: 0.7569247703430972
score: 0.49594494700431824
baseScore: 94
voteCount: 25
---
*Previous:*[*My AGI safety research—2022 review, ’23 plans*](https://www.lesswrong.com/posts/qusBXzCpxijTudvBB/my-agi-safety-research-2022-review-23-plans)*. (I guess I skipped it last year.)*

*“Our greatest fear should not be of failure, but of succeeding at something that doesn't really matter.”  –*[*attributed to DL Moody*](https://www.goodreads.com/quotes/390887-our-greatest-fear-should-not-be-of-failure-but-of)

Tl;dr
=====

* Section 1 goes through my main research project, “reverse-engineering human social instincts”: what does that even mean, what’s the path-to-impact, what progress did I make in 2024 (spoiler: lots!!), and how can I keep pushing it forward in the future?
* Section 2 is what I’m expecting to work on in 2025: most likely, I’ll start the year with some bigger-picture thinking about Safe & Beneficial AGI, then eventually get back to reverse-engineering human social instincts after that. Plus, a smattering of pedagogy, outreach, etc.
* Section 3 is a sorted list of all my blog posts from 2024
* Section 4 is acknowledgements

1. Main research project: reverse-engineering human social instincts
====================================================================

1.1 Background: What’s the problem and why should we care?
----------------------------------------------------------

*(copied almost word-for-word from*[*Neuroscience of human social instincts: a sketch*](https://www.lesswrong.com/posts/kYvbHCDeMTCTE9TAj/neuroscience-of-human-social-instincts-a-sketch)*)*

My primary neuroscience research goal for the past couple years has been to solve a certain problem, a problem which has had me stumped since the very beginning of when I became interested in neuroscience at all ([as a lens into Artificial General Intelligence safety](https://www.lesswrong.com/s/HzcM2dkCq7fwXBej8)) back in 2019.

What is this grand problem? As described in [Intro to Brain-Like-AGI Safety](https://www.lesswrong.com/s/HzcM2dkCq7fwXBej8), I believe the following:

1. We can divide the brain into a [“Learning Subsystem”](https://www.lesswrong.com/posts/wBHSYwqssBGCnwvHg/intro-to-brain-like-agi-safety-2-learning-from-scratch-in) (cortex, striatum, amygdala, cerebellum, and a few other areas) that houses a bunch of [randomly-initialized](https://www.lesswrong.com/posts/wBHSYwqssBGCnwvHg/intro-to-brain-like-agi-safety-2-learning-from-scratch-in) within-lifetime learning algorithms, and a [“Steering Subsystem”](https://www.lesswrong.com/posts/hE56gYi5d68uux9oM/intro-to-brain-like-agi-safety-3-two-subsystems-learning-and) (hypothalamus, brainstem, and a few other areas) that houses a bunch of specific, genetically-specified [“business logic”](https://www.lesswrong.com/posts/hE56gYi5d68uux9oM/intro-to-brain-like-agi-safety-3-two-subsystems-learning-and#:~:text=nice%20term%C2%A0%E2%80%9C-,business%20logic,-%E2%80%9D%2C%20for%20code). A major role of the Steering Subsystem is as the home for the brain’s **“innate drives”, a.k.a. “primary rewards”**, roughly equivalent to the reward function in reinforcement learning—things like eating-when-hungry being good (other things equal), pain being bad, and so on.
2. Some of those “innate drives” are related to **human social instincts**—a suite of reactions and drives that are upstream of things like compassion, friendship, love, spite, sense of fairness and justice, etc.
3. **The grand problem is: how do those human social instincts work?** Ideally, an answer to this problem would look like legible pseudocode that’s simultaneously compatible with behavioral observations (including everyday experience), with evolutionary considerations, and with a neuroscience-based story of how that pseudocode is actually implemented by neurons in the brain.[[1]](#fn72ioyjkt4p2)
4. Explaining how human social instincts work is tricky mainly because of the **“symbol grounding problem”**. In brief, everything we know—all the interlinked concepts that constitute our understanding of the world and ourselves—is created [“from scratch”](https://www.lesswrong.com/posts/wBHSYwqssBGCnwvHg/intro-to-brain-like-agi-safety-2-learning-from-scratch-in) in the cortex by a learning algorithm, and thus winds up in the form of a zillion unlabeled data entries like “pattern 387294 implies pattern 579823 with confidence 0.184”, or whatever.[[2]](#fnwdgiptlvzsk) Yet certain activation states of these unlabeled entries—e.g., the activation state that encodes the fact that Jun just told me that Xiu thinks I’m cute—need to somehow trigger social instincts in the Steering Subsystem. So there must be some way that the brain can “ground” these unlabeled learned concepts. (See my earlier post [Symbol Grounding and Human Social Instincts](https://www.lesswrong.com/posts/5F5Tz3u6kJbTNMqsb/intro-to-brain-like-agi-safety-13-symbol-grounding-and-human).)
5. A solution to this grand problem seems **useful for**[**Artificial General Intelligence**](https://www.lesswrong.com/posts/uxzDLD4WsiyrBjnPw/artificial-general-intelligence-an-extremely-brief-faq) **(AGI) safety**, since (for better or worse) someone someday might invent AGI that works by similar algorithms as the brain, and we’ll want to make those AGIs intrinsically care about people’s welfare. It would be a good jumping-off point to understand how *humans* wind up intrinsically caring about other people’s welfare sometimes. (Slightly longer version in [§2.2 here](https://www.lesswrong.com/posts/qusBXzCpxijTudvBB/my-agi-safety-research-2022-in-review-and-plans#2_2_Why_do_I_think_success_on_this_project_would_be_helpful_for_AGI_safety_); *much* longer version in [this post](https://www.lesswrong.com/posts/Sd4QvG4ZyjynZuHGt/intro-to-brain-like-agi-safety-12-two-paths-forward).)

1.2 More on the path-to-impact
------------------------------

* **I’m generally working under the assumption that future transformative**[**AGI**](https://www.lesswrong.com/posts/uxzDLD4WsiyrBjnPw/artificial-general-intelligence-an-extremely-brief-faq) **will work generally how I think the brain works (a not-yet-invented variation on Model-Based Reinforcement Learning, see**[**§1.2 here**](https://www.lesswrong.com/posts/As7bjEAbNpidKx6LR/valence-series-1-introduction#1_2_Model_based_reinforcement_learning__RL_)**).** I think this is a rather different algorithm from today’s foundation models, and I think those differences are safety-relevant (see [§4.2 here](https://www.lesswrong.com/posts/YyosBAutg4bzScaLu/thoughts-on-ai-is-easy-to-control-by-pope-and-belrose#4_2_No___brain_like_AGI__is_not_trained_similarly_to_LLMs)). You might be wondering: **why work on that, rather than foundation models?**
  + My diplomatic answer is: we don’t have AGI yet ([by my definition](https://www.lesswrong.com/posts/uxzDLD4WsiyrBjnPw/artificial-general-intelligence-an-extremely-brief-faq)), and thus we don’t know for sure what algorithmic form it will take. So we should be hedging our bets, by different AGI safety people contingency-planning for different possible AGI algorithm classes. And the model-based RL scenario seems *even more* under-resourced right now than the foundation model scenario, by far.
  + My un-diplomatic answer is: Hard to be certain, but I’m guessing that the researchers pursuing broadly-brain-like paths to AGI are the ones who will probably succeed, and everyone else will probably fail to get all the way to AGI, and/or they’ll gradually pivot / converge towards brain-like approaches, for better or worse. In other words, my guess is that 2024-style foundation model training paradigms will plateau before they hit TAI-level. Granted, they haven’t plateaued yet. But any day now, right? See [AI doom from an LLM-plateau-ist perspective](https://www.lesswrong.com/posts/KJRBb43nDxk6mwLcR/ai-doom-from-an-llm-plateau-ist-perspective) and [§2 here](https://www.lesswrong.com/posts/hsf7tQgjTZfHjiExn/my-take-on-jacob-cannell-s-take-on-agi-safety#2__Will_AGI_algorithms_look_like_brain_algorithms_).
* **How might my ideas make their way from blog posts into future AGI source code?** Well, again, there’s a scenario (threat model) for which I’m contingency-planning, and it involves future researchers who are inventing brain-like model-based RL, for better or worse. Those researchers will find that they have a slot in their source code repository labeled “reward function”, and they won’t know what to put in that slot to get good outcomes, as they get towards human-level capabilities and beyond. During *earlier* development, with rudimentary AI capabilities, I expect that the researchers will have been doing what model-based RL researchers are doing today, and indeed what they have *always* done since the invention of RL: messing around with obvious reward functions, and trying to get results that are somehow impressive. And if the AI engages in [specification gaming](https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) or other undesired behavior, then they turn it off, try to fix the problem, and try again. But, [as AGI safety people know well](https://open.substack.com/pub/dileeplearning/p/amelia-bedelia-and-agi-safety-part?r=4jbwd&utm_campaign=comment-list-share-cta&utm_medium=web&comments=true&commentId=77676334), that particular debugging loop will eventually stop working, and instead start failing in a catastrophically dangerous way. Assuming the developers notice that problem before it’s too late, they might look to the literature for a reward function (and associated training environment etc.) that will work in this new capabilities regime. Hopefully, when they go looking, they will find a literature that will *actually exist*, and be full of clear explanations and viable ideas. So that’s what I’m working on. I think it’s a very important piece of the puzzle, even if many other unrelated things can *also* go wrong on the road to (hopefully) Safe and Beneficial AGI.

1.3 Progress towards reverse-engineering human social instincts
---------------------------------------------------------------

It was a banner year!

Basically, for years, I’ve had a vague idea about how human social instincts might work, involving what I call “transient empathetic simulations”. But I didn’t know how to pin it down in more detail than that. One subproblem was: I didn’t have even one example of a *specific* social instinct based on this putative mechanism—i.e., a hypothesis where a *specific* innate reaction would be triggered by a *specific* transient empathetic simulation in a *specific* context, such that the results would be consistent with everyday experience and evolutionary considerations. The other subproblem was: I just had lots of confusion about how these things might work in the brain, in detail.

I made progress on the first subproblem in late 2023, when I guessed that there’s an innate *“drive to feel liked / admired”*, related to prestige-seeking, and I had a specific idea about how to operationalize that. It turned out that I was still held back by confusion about how social status works, and thus I spent some time in early 2024 sorting that out—see my three posts [Social status part 1/2: negotiations over object-level preferences](https://www.lesswrong.com/posts/SPBm67otKq5ET5CWP/social-status-part-1-negotiations-over-object-level), and [Social status part 2/2: everything else](https://www.lesswrong.com/posts/7RBbwqHoimj92MRnL/social-status-part-2-2-everything-else), and a rewritten [[Valence series] 4. Valence & Liking / Admiring](https://www.lesswrong.com/posts/LaeP39jJpfPyoiSZm/valence-series-4-valence-and-liking-admiring) (which replaced an older, flawed attempt at part 4 of the [Valence series](https://www.lesswrong.com/posts/As7bjEAbNpidKx6LR/valence-series-1-introduction)).

Now I had at least one target to aim for—an innate social drive that I felt I understood well enough to sink my teeth into. That was very helpful for thinking about how that drive might work neuroscientifically. But getting there was still a *hell* of a journey, and was the main thing I did the whole rest of the year. I chased down lots of leads, many of which were mostly dead ends, although I wound up figuring out lots of random stuff along the way, and in fact one of those threads turned into my 8-part [Intuitive Self-Models series](https://www.lesswrong.com/s/qhdHbCJ3PYesL9dde).

But anyway, I finally wound up with [**Neuroscience of human social instincts: a sketch**](https://www.lesswrong.com/posts/kYvbHCDeMTCTE9TAj/neuroscience-of-human-social-instincts-a-sketch), which posits a neuroscience-based story of how certain social instincts work, including not only the “drive to feel liked / admired” mentioned above, but also compassion and spite, which (I claim) are mechanistically related, to my surprise. Granted, many details remain hazy, but this still feels like great progress on the big picture. Hooray!

1.4 What’s next?
----------------

In terms of my moving this project forward, there’s lots of obvious work in making more and better hypotheses and testing them against existing literature. Again, see [Neuroscience of human social instincts: a sketch](https://www.lesswrong.com/posts/kYvbHCDeMTCTE9TAj/neuroscience-of-human-social-instincts-a-sketch), in which I point out plenty of lingering gaps and confusions. Now, it’s possible that I would hit a dead end at some point, because I have a question that is not answered in the existing neuroscience literature. In particular, the hypothalamus and brainstem have hundreds of tiny cell groups with idiosyncratic roles, and most of them remain unmeasured to date. (As an example, see [§5.2 of A Theory of Laughter](https://www.lesswrong.com/posts/7kdBqSFJnvJzYTfx9/a-theory-of-laughter#5_2_Where_exactly_in_the_brain_is_the__laugh_behavior_controller___top_box_in_that_diagram__where_I_can_read_out_the_alleged_pseudocode_of_Section_3_1_), the part where it says “If someone wanted to make progress on this question experimentally…”). But a number of academic groups are continuing to slowly chip away at that problem, and with a lot of luck, connectomics researchers will start mass-producing those kinds of measurements in as soon as the next few years.

(Reminder that [Connectomics seems great from an AI x-risk perspective](https://www.lesswrong.com/posts/ybmDkJAj3rdrrauuu/connectomics-seems-great-from-an-ai-x-risk-perspective), and as mentioned in the last section of that link, you can get involved by applying for jobs, some of which are for non-bio roles like “ML engineer”, or by donating.)

2. My plans going forward
=========================

Actually, “reverse-engineering human social instincts” is on hold for the moment, as I’m revisiting the big picture of safe and beneficial AGI, now that I have this new and hopefully-better big-picture understanding of human social instincts under my belt. In other words, knowing what I (think I) know now about how human social instincts work, at least in broad outline, well, what should a brain-like-AGI reward function look like? What about training environment? And test protocols? What are we hoping that AGI developers will do with their AGIs anyway?

I’ve been so deep in neuroscience that I have a huge backlog of this kind of big-picture stuff that I haven’t yet processed.

After that, I’ll *probably* wind up diving back into neuroscience in general, and reverse-engineering human social instincts in particular, but only after I’ve thought hard about what *exactly* I’m hoping to get out of it, in terms of AGI safety, on the current margins. That way, I can be focusing on the right questions.

Separate from all that, I plan to stay abreast of the broader AGI safety field, from fundamentals to foundation models, even if the latter is not really my core interest or comparative advantage. I also plan to continue engaging in AGI safety pedagogy and outreach when I can, including probably reworking some of my blog post ideas into a peer-reviewed paper for a neuroscience journal this spring.

If someone thinks that I should be spending my time differently in 2025, please reach out and make your case!

3. Sorted list of my blog posts from 2024
=========================================

***The** **“reverse-engineering human social instincts” project:***

* [Social status part 1/2: negotiations over object-level preferences](https://www.lesswrong.com/posts/SPBm67otKq5ET5CWP/social-status-part-1-negotiations-over-object-level) (March)
* [Social status part 2/2: everything else](https://www.lesswrong.com/posts/7RBbwqHoimj92MRnL/social-status-part-2-2-everything-else) (March)
* [Spatial attention as a “tell” for empathetic simulation?](https://www.lesswrong.com/posts/7Pt9fogptmiSduXt9/spatial-attention-as-a-tell-for-empathetic-simulation) (April)
* [[Valence series] 4. Valence & Liking / Admiring](https://www.lesswrong.com/posts/LaeP39jJpfPyoiSZm/valence-series-4-valence-and-liking-admiring) (June)
* [Against empathy-by-default](https://www.lesswrong.com/posts/TprdAhgTvr3tuDJsD/against-empathy-by-default) (Oct)
* [Neuroscience of human social instincts: a sketch](https://www.lesswrong.com/posts/kYvbHCDeMTCTE9TAj/neuroscience-of-human-social-instincts-a-sketch) (Nov)

***Other** **neuroscience posts, generally with a less immediately obvious connection to AGI safety:***

* [Woods’ new preprint on object permanence](https://www.lesswrong.com/posts/v9qj2LHLh2ALDGKyA/woods-new-preprint-on-object-permanence) (March)
* [(Appetitive, Consummatory) ≈ (RL, reflex)](https://www.lesswrong.com/posts/jZLk6DQJ2EwhSty4k/appetitive-consummatory-rl-reflex) (June)
* [Incentive Learning vs Dead Sea Salt Experiment](https://www.lesswrong.com/posts/YQ4rSTHpHeFcAmhvi/incentive-learning-vs-dead-sea-salt-experiment) (June)
* [[Intuitive self-models] 1. Preliminaries](https://www.lesswrong.com/posts/FtwMA5fenkHeomz52/intuitive-self-models-1-preliminaries) (Sept)
* [[Intuitive self-models] 2. Conscious Awareness](https://www.lesswrong.com/posts/73xBjgoHuiKvJ5WRk/intuitive-self-models-2-conscious-awareness) (Sept)
* [[Intuitive self-models] 3. The Homunculus](https://www.lesswrong.com/posts/7tNq4hiSWW9GdKjY8/intuitive-self-models-3-the-homunculus) (Oct)
* [[Intuitive self-models] 4. Trance](https://www.lesswrong.com/posts/QAjmr323LZGQBEvd5/intuitive-self-models-4-trance) (Oct)
* [[Intuitive self-models] 5. Dissociative Identity (Multiple Personality) Disorder](https://www.lesswrong.com/posts/6bW5uJ325JxHYqMFr/intuitive-self-models-5-dissociative-identity-multiple) (Oct)
* [[Intuitive self-models] 6. Awakening / Enlightenment / PNSE](https://www.lesswrong.com/posts/GvJe6WQ3jbynyhjxm/intuitive-self-models-6-awakening-enlightenment-pnse) (Oct)
* [[Intuitive self-models] 7. Hearing Voices, and Other Hallucinations](https://www.lesswrong.com/posts/k8uMmw45k3qp8LPNc/intuitive-self-models-7-hearing-voices-and-other) (Oct)
* [[Intuitive self-models] 8. Rooting Out Free Will Intuitions](https://www.lesswrong.com/posts/JLZnSnJptzmPtSRTc/intuitive-self-models-8-rooting-out-free-will-intuitions) (Nov)

***Everything** **else related to Safe & Beneficial AGI:***

* [Deceptive AI ≠ Deceptively-aligned AI](https://www.lesswrong.com/posts/a392MCzsGXAZP5KaS/deceptive-ai-deceptively-aligned-ai) (Jan)
* [Four visions of Transformative AI success](https://www.lesswrong.com/posts/3aicJ8w4N9YDKBJbi/four-visions-of-transformative-ai-success) (Jan)
* [“Artificial General Intelligence”: an extremely brief FAQ](https://www.lesswrong.com/posts/uxzDLD4WsiyrBjnPw/artificial-general-intelligence-an-extremely-brief-faq) (March)
* [Response to nostalgebraist: proudly waving my moral-antirealist battle flag](https://www.lesswrong.com/posts/8YhjpgQ2eLfnzQ7ec/response-to-nostalgebraist-proudly-waving-my-moral) (May)
* [Response to Dileep George: AGI safety warrants planning ahead](https://www.lesswrong.com/posts/LJD4C7KAr64onL8fq/response-to-dileep-george-agi-safety-warrants-planning-ahead) (July)
* [A shortcoming of concrete demonstrations as AGI risk advocacy](https://www.lesswrong.com/posts/L7t3sKnS7DedfTFFu/a-shortcoming-of-concrete-demonstrations-as-agi-risk) (Dec)

***Random** **non-work-related rants etc. in my free time:***

* [Some (problematic) aesthetics of what constitutes good work in academia](https://www.lesswrong.com/posts/LZJJK6fuuQtTLRSu9/some-problematic-aesthetics-of-what-constitutes-good-work-in) (March)
* [A couple productivity tips for overthinkers](https://www.lesswrong.com/posts/ZN6L5ysKd35FEyGr6/a-couple-productivity-tips-for-overthinkers) (April)

Also in 2024, I went through and revised my 15-post [Intro to Brain-Like-AGI Safety](https://www.lesswrong.com/s/HzcM2dkCq7fwXBej8) series (originally published in 2022). For summary of changes, see [this twitter thread](https://x.com/steve47285/status/1813971002222952852). (Or [here](https://www.lesswrong.com/posts/btHmC88KCZdzimBCM/steve2152-s-shortform?commentId=DD28htp2tWZg7w8eT) without pictures, if you want to avoid twitter.) For more detailed changes, each post of the series has a changelog at the bottom.

4. Acknowledgements
===================

Thanks Jed McCaleb & [Astera Institute](https://astera.org/) for generously supporting my research since August 2022!

Thanks to all the people who comment on my posts before or after publication, or share ideas and feedback with me through [email](mailto:steven.byrnes@gmail.com) or [other channels](https://sjbyrnes.com/), and especially those who patiently stick it out with me through long back-and-forths to hash out disagreements and confusions. I’ve learned so much that way!!!

Thanks to my coworker Seth for fruitful ideas and discussions, and to Beth Barnes and the [Centre For Effective Altruism](https://www.centreforeffectivealtruism.org/) [Donor Lottery Program](https://www.givingwhatwecan.org/donor-lottery) for helping me get off the ground with grant funding in 2021-2022. Thanks Lightcone Infrastructure ([don’t forget to donate](https://www.lesswrong.com/posts/5n2ZQcbc7r4R8mvqc/the-lightcone-is-nothing-without-its-people)!) for maintaining and continuously improving this site, which has always been an essential part of my workflow. Thanks to everyone else fighting for Safe and Beneficial AGI, and thanks to my family, and thanks to you all for reading! Happy New Year!

1. **[^](#fnref72ioyjkt4p2)**
   
   For a different (simpler) example of what I think it looks like to make progress towards that kind of pseudocode, see my post [A Theory of Laughter](https://www.lesswrong.com/posts/7kdBqSFJnvJzYTfx9/a-theory-of-laughter).
2. **[^](#fnrefwdgiptlvzsk)**
   
   Thanks to regional specialization across the cortex (roughly correspondingly to “neural network architecture” in ML lingo), there can be *a priori* reason to believe that, for example, “pattern 387294” is a pattern in short-term auditory data whereas “pattern 579823” is a pattern in large-scale visual data, or whatever. But that’s not good enough. The symbol grounding problem for social instincts needs *much* more specific information than that. If Jun just told me that Xiu thinks I’m cute, then that’s a very different situation from if Jun just told me that Fang thinks I’m cute, leading to very different visceral reactions and drives. Yet those two possibilities are built from generally the same kinds of data.
