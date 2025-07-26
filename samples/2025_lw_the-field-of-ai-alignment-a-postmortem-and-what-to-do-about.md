---
title: "The Field of AI Alignment: A Postmortem, and What To Do About It"
date: 2025-01-01 00:42:36.538000+00:00
url: https://www.lesswrong.com/posts/nwpyhyagpPYDn4dAW/the-field-of-ai-alignment-a-postmortem-and-what-to-do-about
novelty: 0.9254826649561891
score: 0.5714353919029236
baseScore: 282
voteCount: 174
---
> A policeman sees a drunk man searching for something under a streetlight and asks what the drunk has lost. He says he lost his keys and they both look under the streetlight together. After a few minutes the policeman asks if he is sure he lost them here, and the drunk replies, no, and that he lost them in the park. The policeman asks why he is searching here, and the drunk replies, "this is where the light is".

Over the past few years, a major source of my relative optimism on AI has been the hope that the field of alignment would transition from pre-paradigmatic to paradigmatic, and make much more rapid progress.

At this point, that hope is basically dead. There *has* been some degree of paradigm formation, but the memetic competition has mostly been won by streetlighting: the large majority of AI Safety researchers and activists are focused on searching for their metaphorical keys under the streetlight. The memetically-successful strategy in the field is to tackle problems which are easy, rather than problems which are plausible bottlenecks to humanity’s survival. That pattern of memetic fitness looks likely to continue to dominate the field going forward.

This post is on my best models of how we got here, and what to do next.

What This Post Is And Isn't, And An Apology
===========================================

This post starts from the observation that streetlighting has mostly won the memetic competition for alignment as a research field, and we'll mostly take that claim as given. Lots of people will disagree with that claim, and convincing them is not a goal of this post. In particular, probably the large majority of people in the field have some story about how their work is not searching under the metaphorical streetlight, or some reason why searching under the streetlight is in fact the right thing for them to do, or [...].

The kind and prosocial version of this post would first walk through every single one of those stories and argue against them at the object level, to establish that alignment researchers are in fact mostly streetlighting (and review how and why streetlighting is bad). Unfortunately that post would be hundreds of pages long, and nobody is ever going to get around to writing it. So instead, I'll link to:

* [Eliezer's List O' Doom](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities)
* My own [Why Not Just...](https://www.lesswrong.com/s/TLSzP4xP42PPBctgw) sequence
* Nate's [How Various Plans Miss The Hard Bits Of The Alignment Challenge](https://www.lesswrong.com/posts/3pinFH3jerMzAvmza/on-how-various-plans-miss-the-hard-bits-of-the-alignment)

(Also I might link some more in the comments section.) Please go have the object-level arguments there rather than rehashing everything here.

Next comes the really brutally unkind part: the subject of this post necessarily involves modeling what's going on in researchers' heads, such that they end up streetlighting. That means I'm going to have to speculate about how lots of researchers are being stupid internally, when those researchers themselves would probably say that they are not being stupid at all and I'm being totally unfair. And then when they try to defend themselves in the comments below, I'm going to say "please go have the object-level argument on the posts linked above, rather than rehashing hundreds of different arguments here". To all those researchers: yup, from your perspective I am in fact being very unfair, and I'm sorry. You are not the intended audience of this post, I am basically treating you like a child and saying "quiet please, the grownups are talking", but the grownups in question are talking *about you* and in fact I'm trash talking your research pretty badly, and that is not fair to you at all.

But it is important, and this post just isn't going to get done any other way. Again, I'm sorry.

Why The Streetlighting?
=======================

A Selection Model
-----------------

First and largest piece of the puzzle: selection effects favor people doing easy things, regardless of whether the easy things are in fact the right things to focus on. (Note that, under this model, it's totally possible that the easy things *are* the right things to focus on!)

What does that look like in practice? Imagine two new alignment researchers, Alice and Bob, fresh out of a CS program at a mid-tier university. Both go into MATS or AI Safety Camp or get a short grant or [...]. Alice is excited about the [eliciting latent knowledge](https://www.lesswrong.com/posts/qHCDysDnvhteW7kRd/arc-s-first-technical-report-eliciting-latent-knowledge) (ELK) doc, and spends a few months working on it. Bob is excited about [debate](https://www.lesswrong.com/tag/debate-ai-safety-technique-1), and spends a few months working on it. At the end of those few months, Alice has a much better understanding of how and why ELK is hard, has correctly realized that she has no traction on it at all, and pivots to working on technical governance. Bob, meanwhile, has some toy but tangible outputs, and feels like he's making progress.

... of course (I would say) Bob has not made any progress *toward solving any probable bottleneck problem of AI alignment*, but he has tangible outputs and is making progress on *something*, so he'll probably keep going.

And that's what the selection pressure model looks like in practice. Alice is working on something hard, correctly realizes that she has no traction, and stops. (Or maybe she just keeps spinning her wheels until she burns out, or funders correctly see that she has no outputs and stop funding her.) Bob is working on something easy, he has tangible outputs and feels like he's making progress, so he keeps going and funders keep funding him. How much impact Bob's work has impact on humanity's survival is very hard to measure, but the fact that he's making progress on *something* is easy to measure, and the selection pressure rewards that easy metric.

Generalize this story across a whole field, and we end up with most of the field focused on things which are easy, regardless of whether those things are valuable.

### Selection and the Labs

Here's a special case of the selection model which I think is worth highlighting.

Let's start with a hypothetical CEO of a hypothetical AI lab, who (for no particular reason) we'll call Sam. Sam wants to win the race to AGI, but also needs an AI Safety Strategy. Maybe he needs the safety strategy as a political fig leaf, or maybe he's honestly concerned but not very good at not-rationalizing. Either way, he meets with two prominent AI safety thinkers - let's call them (again for no particular reason) Eliezer and Paul. Both are clearly pretty smart, but they have very different models of AI and its risks. It turns out that Eliezer's model predicts that alignment is very difficult and totally incompatible with racing to AGI. Paul's model... if you squint just right, you could maybe argue that racing toward AGI is sometimes a good thing under Paul's model? Lo and behold, Sam endorses Paul's model as the Official Company AI Safety Model of his AI lab, and continues racing toward AGI. (Actually the version which eventually percolates through Sam's lab is not even Paul's actual model, it's a quite different version which just-so-happens to be even friendlier to racing toward AGI.)

A "Flinching Away" Model
------------------------

While selection for researchers working on easy problems is one big central piece, I don't think it fully explains how the field ends up focused on easy things in practice. Even looking at *individual* newcomers to the field, there's usually a tendency to gravitate toward easy things and away from hard things. What does that look like?

Carol follows a similar path to Alice: she's interested in the Eliciting Latent Knowledge problem, and starts to dig into it, but hasn't really understood it much yet. At some point, she notices a deep difficulty introduced by sensor tampering - in extreme cases it makes problems undetectable, which [breaks the iterative problem-solving loop](https://www.lesswrong.com/posts/xFotXGEotcKouifky/worlds-where-iterative-design-fails), breaks ease of validation, destroys potential training signals, etc. And then she briefly wonders if the problem could somehow be tackled without relying on accurate feedback from the sensors at all. At that point, I would say that Carol is thinking about the real core ELK problem for the first time.

... and Carol's thoughts run into a blank wall. In the first few seconds, she sees no toeholds, not even a starting point. And so she reflexively [flinches away](https://www.lesswrong.com/posts/YpXsZ4H67MaQsoyzz/historical-examples-of-flinching-away) from that problem, and turns back to some easier problems. At that point, I would say that Carol is streetlighting.

It's the reflexive flinch which, on this model, comes first. After that will come rationalizations. Some common variants:

* Carol explicitly introduces some assumption simplifying the problem, and claims that without the assumption the problem is impossible. (Ray's workshop on one-shotting Baba Is You levels [apparently reproduced this phenomenon](https://www.lesswrong.com/posts/8ZR3xsWb6TdvmL8kx/optimistic-assumptions-longterm-planning-and-cope) very reliably.)
* Carol explicitly says that she's not trying to solve the full problem, but hopefully the easier version will make useful marginal progress.
* Carol explicitly says that her work on easier problems is only intended to help with near-term AI, and hopefully those AIs will be able to solve the harder problems.
* (Most common) Carol just doesn't think about the fact that the easier problems don't really get us any closer to aligning superintelligence. Her social circles act like her work is useful somehow, and that's all the encouragement she needs.

... but crucially, the details of the rationalizations aren't that relevant to this post. Someone who's flinching away from a hard problem will always be able to find some rationalization. Argue them out of one (which is itself difficult), and they'll promptly find another. If we want people to not streetlight, then we need to somehow solve the flinching.

Which brings us to the "what to do about it" part of the post.

What To Do About It
===================

Let's say we were starting a new field of alignment from scratch. How could we avoid the streetlighting problem, assuming the models above capture the core gears?

First key thing to notice: in our opening example with Alice and Bob, Alice *correctly* realized that she had no traction on the problem. If the field is to be useful, then somewhere along the way someone needs to actually have traction on the hard problems.

Second key thing to notice: if someone actually has traction on the hard problems, then the "flinching away" failure mode is probably circumvented.

So one obvious thing to focus on is getting traction on the problems.

... and in my experience, there *are* people who can get traction on the core hard problems. Most notably physicists - when they grok the hard parts, they tend to immediately see footholds, rather than a blank impassable wall. I'm picturing here e.g. the sort of crowd at [the ILIAD conference](https://www.lesswrong.com/posts/r7nBaKy5Ry3JWhnJT/announcing-iliad-theoretical-ai-alignment-conference); these were people who mostly did not seem at risk of flinching away, because they saw routes to tackle the problems. (Though to be clear, though ILIAD was a theory conference, I do *not* mean to imply that it's only theorists who ever have any traction.) And they weren't being selected away, because many of them were in fact doing work and making progress.

Ok, so if there are a decent number of people who can get traction, why do the large majority of the people I talk to seem to be flinching away from the hard parts?

How We Got Here
---------------

The main problem, according to me, is the EA recruiting pipeline.

On my understanding, EA student clubs at colleges/universities have been the main “top of funnel” for pulling people into alignment work during the past few years. The mix people going into those clubs is disproportionately STEM-focused undergrads, and looks pretty typical for STEM-focused undergrads. We’re talking about pretty standard STEM majors from pretty standard schools, neither the very high end nor the very low end of the skill spectrum.

... and that's just not a high enough skill level for people to look at the core hard problems of alignment and see footholds.

Who To Recruit Instead
----------------------

We do not need pretty standard STEM-focused undergrads from pretty standard schools. In practice, the level of smarts and technical knowledge needed to gain any traction on the core hard problems seems to be roughly "physics postdoc". Obviously that doesn't mean we exclusively want physics postdocs - I personally have only an undergrad degree, though amusingly [a list of stuff I studied has been called "uncannily similar to a recommendation to readers to roll up their own doctorate program"](https://www.lesswrong.com/posts/bjjbp5i5G8bekJuxv/study-guide?commentId=euo2anBF6PXhKYrju). Point is, it's the rough level of smarts and skills which matters, not the sheepskin. (And no, a doctorate degree in almost any other technical field, including ML these days, does not convey a comparable level of general technical skill to a physics PhD.)

As an alternative to recruiting people who have the skills already, one could instead try to train people. I've [tried that](https://www.lesswrong.com/posts/nvP28s5oydv8RjF9E/mats-models) to some extent, and at this point I think there just isn't a substitute for [years of technical study](https://www.lesswrong.com/posts/bjjbp5i5G8bekJuxv/study-guide). People need that background knowledge in order to see footholds on the core hard problems.

Integration vs Separation
-------------------------

Last big piece: if one were to recruit a bunch of physicists to work on alignment, I think it would be useful for them to form a community mostly-separate from the current field. They need a memetic environment which will amplify progress on core hard problems, rather than... well, all the stuff that's currently amplified.

This is a problem which might solve itself, if a bunch of physicists move into alignment work. Heck, we've already seen it to a very limited extent with the ILIAD conference itself. Turns out people working on the core problems want to talk to other people working on the core problems. But the process could perhaps be accelerated a lot with more dedicated venues.
