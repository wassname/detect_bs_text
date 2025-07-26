---
title: "The Plan - 2024 Update"
date: 2024-12-31 19:29:23.013000+00:00
url: https://www.lesswrong.com/posts/kJkgXEwQtWLrpecqg/the-plan-2024-update
novelty: 0.7851697060402698
score: 0.542655885219574
baseScore: 113
voteCount: 48
---
This post is a follow-up to [The Plan - 2023 Version](https://www.lesswrong.com/posts/HfqbjwpAEGep9mHhc/the-plan-2023-version). There’s also [The Plan - 2022 Update](https://www.lesswrong.com/posts/BzYmJYECAc3xyCTt6/the-plan-2022-update) and [The Plan](https://www.lesswrong.com/posts/3L46WGauGpr7nYubu/the-plan), but the 2023 version contains everything you need to know about the current Plan. Also see [this comment](https://www.lesswrong.com/posts/BzYmJYECAc3xyCTt6/the-plan-2022-update?commentId=grDHP2Yc6os2SjFsy) and [this comment](https://www.lesswrong.com/posts/HfqbjwpAEGep9mHhc/the-plan-2023-version?commentId=CGoaDgsDdK5TztBqi) on how my plans interact with the labs and other players, if you’re curious about that part.

What Have You Been Up To This Past Year?
----------------------------------------

Our big thing at the end of 2023 was [Natural Latents](https://www.lesswrong.com/posts/dWQWzGCSFj6GTZHz7/natural-latents-the-math). Prior to natural latents, the biggest problem with my [math on natural abstraction](https://www.lesswrong.com/posts/gvzW46Z3BsaZsLc25/natural-abstractions-key-claims-theorems-and-critiques-1) was that it didn’t handle approximation well. Natural latents basically solved that problem. With that theoretical barrier out of the way, it was time to focus on crossing the theory-practice gap. Ultimately, that means building a product to get feedback from users on how well our theory works in practice, providing an empirical engine for iterative improvement of the theory.

In late 2023 and early 2024, David and I spent about 3-4 months trying to speedrun the theory-practice gap. Our target product was an image editor; the idea was to use a standard image generation net (specifically [this one](https://huggingface.co/SimianLuo/LCM_Dreamshaper_v7)), and edit natural latent variables internal to the net. It’s conceptually similar to some things people have built before, but the hope would be that natural latents would better match human concepts, and therefore the edits would feel more like directly changing human-interpretable things in the image in natural ways.

When I say “speedrun” the theory-practice gap… well, the standard expectation is that there’s a lot of iteration and insights required to get theory working in practice (even when the theory is basically correct). The “speedrun” strategy was to just try the easiest and hackiest thing at every turn. The hope was that (a) maybe it turns out to be that easy (though probably not), and (b) even if it doesn’t work we’ll get some useful feedback. After 3-4 months, it indeed did not work very well. But more importantly, we did not actually get much useful feedback signal. David and I now think the project was a pretty major mistake; it cost us 3-4 months and we got very little out of it.

After that, we spent a few months on some smaller and more theory-ish projects. We worked out a [couple](https://www.lesswrong.com/posts/NHKCtSXgFieDAyWt2/calculating-natural-latents-via-resampling) [more](https://www.lesswrong.com/posts/xDsbqxeCQWe4BiYFX/natural-latents-are-not-robust-to-tiny-mixtures) pieces of the math of natural latents, [explained](https://www.lesswrong.com/posts/RrQftNoRHd5ya54cb/towards-a-less-bullshit-model-of-semantics) what kind of model of semantics we’d ideally like (in terms of natural latents), [wrote up](https://www.lesswrong.com/posts/DXxEp3QWzeiyPMM3y/a-simple-toy-coherence-theorem) a toy coherence theorem which I think is currently the best illustration of how coherence theorems *should* work, [worked out](https://www.lesswrong.com/posts/QA7bQHpKymPBFBuHb/a-solomonoff-inductor-walks-into-a-bar-schelling-points-for) a version of natural latents for Solomonoff inductors[[1]](#fn6vcsu80422i) and applied that to semantics as well, [presented](https://www.lesswrong.com/posts/7LaDvWtymFWtidGxe/corrigibility-tool-ness) an interesting notion of corrigibility and tool-ness, and [put](https://www.lesswrong.com/posts/YgaPhcrkqnLrTzQPG/we-don-t-know-our-own-values-but-reward-bridges-the-is-ought) [together](https://www.lesswrong.com/posts/a5hpPfABQnrkfGGxb/values-are-real-like-harry-potter) an agent model which resolved all of my own most pressing outstanding confusions about the type-signature of human values. There were also a few other results which we haven’t yet written up, including a version of the second law of thermo more suitable for embedded agents, and some more improvements to the theory of natural latents, as well as a bunch of small investigations which didn’t yield anything legible.

Of particular note, we spent several weeks trying to [apply](https://www.lesswrong.com/posts/QsstSjDqa7tmjQfnq/wait-our-models-of-semantics-should-inform-fluid-mechanics) the theory of natural latents to fluid mechanics. That project has not yet yielded anything notable, but it’s of interest here because it’s another plausible route to a useful product: a fluid simulation engine based on natural latent theory would, ideally, make all of today’s fluid simulators completely obsolete, and totally change the accuracy/compute trade-off curves. To frame it in simulation terms, the ideal version of this would largely solve the challenges of [multiscale simulation](https://en.wikipedia.org/wiki/Multiscale_modeling), i.e. eliminate the need for a human to figure out relevant summary statistics and hand-code multiple levels. Of course that project has its own nontrivial theory-practice gap to cross.

At the moment, we’re focused on another project with an image generator net, about which we might write more in the future.

Why The Focus On Image Generators Rather Than LLMs?
---------------------------------------------------

At this stage, we’re not really interested in the internals of nets themselves. Rather, we’re interested in what kinds of patterns in the environment the net learns and represents. Roughly speaking, one can’t say anything useful about representations in a net until one has a decent characterization of the types of patterns in the environment which are represented in the first place.[[2]](#fnbosody02zja)

And for that purpose, we want to start as “close to the metal” as possible. We definitely do not want our lowest-level data to be symbolic strings, which are themselves already high-level representations far removed from the environment we’re trying to understand.

And yes, I do think that interp work today should mostly focus on image nets for the same reasons we focus on image nets. The field’s current focus on LLMs is a mistake

Any Major Changes To The Plan In The Past Year?
-----------------------------------------------

In previous years, much of my relative optimism stemmed from the hope that the field of alignment would soon shift from pre-paradigmatic to paradigmatic, and progress would accelerate a lot as a result. [I’ve largely given up on that hope](https://www.lesswrong.com/posts/nwpyhyagpPYDn4dAW/the-field-of-ai-alignment-a-postmortem-and-what-to-do-about). The probability I assign to a good outcome has gone down accordingly; I don’t have a very firm number, but it’s definitely below 50% now.

In terms of the plan, we’ve shifted toward assuming we’ll need to do more of the work ourselves. Insofar as we’re relying on other people to contribute, we expect it to be a narrower set of people on narrower projects.

This is not as dire an update as it might sound. The results we already have are far beyond what I-in-2020 would have expected from just myself and one other person, especially with the empirical feedback engine not really up and running yet.  Earlier this year, David and I estimated that we’d need roughly a 3-4x productivity multiplier to feel like we were basically on track. And that kind of productivity multiplier is not out of the question; I already estimate that working with David has been about a 3x boost for me, so we’d need roughly that much again. Especially if we get the empirical feedback loop up and running, another 3-4x is very plausible. Not easy, but plausible.

Do We Have Enough Time?
-----------------------

Over the past year, my timelines have become even more bimodal than they already were. The key question is whether o1/o3-style models achieve criticality (i.e. are able to autonomously self-improve in non-narrow ways), including possibly under the next generation of base model. My median guess is that they won’t and that the excitement about them is [very overblown](https://www.lesswrong.com/posts/puv8fRDCH9jx5yhbX/johnswentworth-s-shortform?commentId=szp5fNZJqpfrsyQP9). But I’m not very confident in that guess.

If the excitement is overblown, then we’re most likely still about 1 transformers-level paradigm shift away from AGI capable of criticality, and timelines of ~10 years seem reasonable. Conditional on that world, I also think we’re likely to see another AI winter in the next year or so.

If the excitement is not overblown, then we’re probably looking at more like 2-3 years to criticality. In that case, any happy path probably requires outsourcing a lot of alignment research to AI, and then the main bottleneck is probably [our own understanding](https://www.lesswrong.com/s/TLSzP4xP42PPBctgw/p/3gAccKDW6nRKFumpP) of how to align much-smarter-than-human AGI.

1. **[^](#fnref6vcsu80422i)**
   
   Woohoo! I’d been wanting a Solomonoff version of natural abstraction theory for years.
2. **[^](#fnrefbosody02zja)**
   
   The lack of understanding of the structure of patterns in the environment is a major barrier for interp work today. The cutting edge is “sparse features”, which is indeed a pattern which comes up a lot in our environment, but it’s probably far from a complete catalogue of the relevant types of patterns.
