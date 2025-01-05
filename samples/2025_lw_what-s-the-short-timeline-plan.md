---
title: What’s the short timeline plan?
date: 2025-01-05 00:10:28.708000+00:00
url: https://www.lesswrong.com/posts/bb5Tnjdrptu89rcyY/what-s-the-short-timeline-plan
novelty: 0.8981608613682581
score: 2.114389657974243
baseScore: 236
voteCount: 102
---
*This is a low-effort post. I mostly want to get other people’s takes and express concern about the lack of detailed and publicly available plans so far. This post reflects my personal opinion and not necessarily that of other members of Apollo Research. I’d like to thank Ryan Greenblatt, Bronson Schoen, Josh Clymer, Buck Shlegeris, Dan Braun, Mikita Balesni, Jérémy Scheurer, and Cody Rushing for comments and discussion.*

I think short timelines, e.g. AIs that can replace a top researcher at an AGI lab without losses in capabilities by 2027, are plausible. Some people have posted ideas on what a reasonable plan to reduce AI risk for such timelines might look like (e.g. [Sam Bowman’s checklist](https://sleepinyourhat.github.io/checklist/), or [Holden Karnofsky’s list in his 2022 nearcast](https://www.lesswrong.com/posts/vZzg8NS7wBtqcwhoJ/nearcast-based-deployment-problem-analysis#Phase_2__as_aligned_and_transformative_AI_systems_become_available)), but I find them insufficient for the magnitude of the stakes (to be clear, I don’t think these example lists were intended to be an extensive plan).

If we take AGI seriously, I feel like the AGI companies and the rest of the world should be significantly more prepared, and I think we’re now getting into the territory where models are capable enough that acting without a clear plan is irresponsible.

In this post, I want to ask what such a short timeline plan could look like. Intuitively, if an AGI lab came to me today and told me, “We really fully believe that we will build AGI by 2027, and we will enact your plan, but we aren’t willing to take more than a 3-month delay,” I want to be able to give the best possible answer. I list some suggestions but I don’t think they are anywhere near sufficient. I’d love to see more people provide their answers. If a funder is interested in funding this, I’d also love to see some sort of “best short-timeline plan prize” where people can win money for the best plan as judged by an expert panel.

In particular, I think the AGI companies should publish their detailed plans (minus secret information) so that governments, academics, and civil society can criticize and improve them. I think RSPs were a great step in the right direction and did improve their reasoning transparency and preparedness. However, I think RSPs (at least their current versions) are not sufficiently detailed and would like to see more fine-grained plans.

In this post, I generally make fairly conservative assumptions. I assume we will not make any major breakthroughs in most alignment techniques and will roughly work with the tools we currently have. This post is primarily about preventing the worst possible worlds.

Short timelines are plausible
=============================

By short timelines, I broadly mean the timelines that Daniel Kokotajlo has talked about for years (see e.g. [this summary post](https://www.lesswrong.com/posts/K2D45BNxnZjdpSX2j/ai-timelines); I also found [Eli Lifland’s argument](https://www.lesswrong.com/posts/oC4wv4nTrs2yrP5hz/what-are-the-strongest-arguments-for-very-short-timelines?commentId=Kzam9tz2WsDnBZYAu) good; and liked [this](https://milesbrundage.substack.com/p/times-up-for-ai-policy) and [this](https://www.lesswrong.com/posts/LjgcRbptarrRfJWtR/a-breakdown-of-ai-capability-levels-focused-on-ai-r-and-d)). Concretely, something like

* 2024: AIs can reliably do ML engineering tasks that take humans ~30 minutes fairly reliably and [2-to-4-hour tasks with strong elicitation](https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/).
* 2025: AIs can reliably do 2-to-4-hour ML engineering tasks and sometimes medium-quality incremental research (e.g. conference workshop paper) with strong elicitation.
* 2026: AIs can reliably do 8-hour ML-engineering tasks and sometimes do high-quality novel research (e.g. autonomous research that would get accepted at a top-tier ML conference) with strong elicitation.
* 2027: We will have an AI that can replace a top researcher at an AI lab without any losses in capabilities.
* 2028: AI companies have 10k-1M automated AI researchers. Software improvements go through the roof. Algorithmic improvements have no hard limit and increase super-exponentially. Approximately every knowledge-based job can be automated.
  + These are roughly the “geniuses in datacenters” Dario Amodei refers to in his essay “[Machines of Loving Grace](https://darioamodei.com/machines-of-loving-grace).”
  + There are still some limits to scaling due to hardware bottlenecks.
* 2029: New research has made robotics much better. The physical world doesn’t pose any meaningful limits for AI anymore. More than 95% of economically valuable tasks in 2024 can be fully automated without any loss in capabilities.
* 2030: Billions of AIs with superhuman general capabilities are integrated into every part of society, including politics, military, social aspects, and more.

I think there are some plausible counterarguments to these timelines, e.g. [Tamay Besiroglu argues that hardware limitations might throttle the recursive self-improvement of AIs](https://x.com/tamaybes/status/1848457491736133744). I think this is possible, but currently think software-only recursive self-improvements are plausible. Thus, the timelines above are my median timelines. I think there could be even faster scenarios, e.g. we could already have an AI that replaces a top researcher at an AGI lab by the end of 2025 or in 2026.

There are a couple of reasons to believe in such short timelines:

1. **The last decade of progress:**Since GPT-2, progress in AI has probably been significantly faster than most people anticipated. Most benchmarks get saturated quickly. And so far, I have not seen strong evidence of reduced benefits of scale. If progress continues roughly at this pace, I would intuitively assume the timelines above.
2. **AGI companies’ stated timelines:**Multiple AI companies have repeatedly stated that they expect roughly the timelines I describe above. While they have some incentive to overplay their capabilities, they are closest to the source and know about advances earlier than the general public, so I think it’s correct to weigh their opinions highly. I’d also note that multiple people who have decided to leave these companies and thus have a reduced incentive to overplay capabilities still continue to argue for short timelines (e.g. Daniel Kokotajlo or Miles Brundage).
3. **No further major blockers to AGI:**I think the recipe of big pre-training run + agent scaffolding + extensive fine-tuning (including RL) will, by default, scale to a system that can automate top AI researchers. There will be engineering challenges, and there might be smaller blockers, e.g. how these systems can track information over longer periods of time (memory), but I don’t expect any of these to be fundamental. I previously expected that effective inference-time compute utilization might pose a blocker (~30%), but o1 and o3 convinced me that it likely won’t.

In conclusion, I can understand why people would have longer median timelines, but I think they should consider the timelines described above at least as a plausible scenario (e.g. >10% likely). Thus, there should be a plan.

What do we need to achieve at a minimum?
========================================

There is a long list of things we would love to achieve. However, I think there are two things we need to achieve at a minimum or the default scenario is catastrophic.

1. **Model weights (and IP) are secure:**By this, I mean SL4 or higher, as defined in the [report on securing model weights](https://www.rand.org/pubs/research_reports/RRA2849-1.html) at the time we reach the capability level where an AI can replace a top researcher. If the model weights aren’t secure, either a bad actor could steal them or the model itself could self-exfiltrate. In both cases, most other alignment efforts would be drastically less impactful because there is no way of guaranteeing that they are actually being used. Model security more broadly includes scenarios where a malicious actor can do meaningfully large fine-tuning runs within the AI developer, not just exfiltration. It also includes securing algorithmic secrets to prevent malicious actors from catching up on their own (this likely requires a somewhat different set of interventions than securing model weights).
2. **The first AI that significantly speeds up alignment research isn’t successfully scheming:**At some point, there will be an AI system that significantly (e.g. 10x) speeds up any kind of research.  This AI system will likely/hopefully be used for AI safety research. If this AI system is scheming and we’re unable to detect it, or we’re unable to prevent the scheming plans from succeeding ([Control](https://www.lesswrong.com/tag/ai-control)), I expect the default outcome to be bad. Thus, a large part of this post is concerned with ensuring that we can trust the first sufficiently powerful AI system and thus “bootstrap” alignment plans for more capable systems.

The default scenario I have in mind here is broadly the following: There is one or a small number of AGI endeavors, almost certainly in the US. This project is meaningfully protected by the US government and military both for physical and cyber security (perhaps not at the maximal level of protection, but it’s a clear priority for the US government). Their most advanced models are not accessible to the public. This model is largely used for alignment and other safety research, e.g. it would compress 100 years of human AI safety research into less than a year. This research is then used to ensure that the next system is sufficiently aligned/controlled and that the model weights continue to be secure.

This feels like a minimal stable solution. Of course, I would prefer if we were more prepared. I also think there are other paths than building more aligned & powerful successors that AI developers could take with human-level AI systems. However, for this post, I will make the conservative assumption that nobody is willing to stop racing. Thus, conditional on a capability race, I’d want them to use their first AGIs to do lots of alignment, control, and security research.

There is a very long list of further assumptions and desiderata that I don’t elaborate on in this post, e.g.

1. Leaders in the labs are trustworthy enough and would actually use this first AI system for alignment and other safety research.
2. There is no war in the run-up to AGI that would derail the project, e.g. by necessitating that most resources be used for capabilities instead of safety research.
3. There is sufficiently good international AI governance.
4. The training runs are not sabotaged by external actors, e.g. other governments.
5. …

I want as many of those assumptions to hold. However, in this post, I want to primarily focus on the most minimal version.

Making conservative assumptions for safety progress
===================================================

If we only have 2-3 years until AGI, I think it’s reasonable to make conservative assumptions about AI safety progress. Concretely:’

1. **No major scientific breakthroughs in interpretability, scalable oversight, or super alignment.** We will make continued improvements for all of these techniques, but none of them will be strong enough that they provide sufficient confidence on their own. They are, at best, part of a larger defense-in-depth strategy as supporting arguments.
2. **We roughly have ++ versions of the tools we currently have**, e.g. evals, control, basic alignment training techniques, monitoring, etc.
3. **There are no major changes in governance.** Maybe some of the voluntary commitments will be mandated and third-party auditing is required but there are no major international treaties or bigger legislation in the US and UK.
4. **There are no major paradigm changes.** AGI is based on a scaffolded transformer that is trained with a lot of RL. Some new bells and whistles, such as improved memory techniques, are added, but there is no change in the core architecture or training regime. It is possible that the CoT is not human-legible or faithful anymore after these changes.

I think it is plausible that we will make a lot of alignment progress if we get to the aligned-enough human-level AI systems (i.e. roughly 2028 in my timeline above). This post is mostly concerned with how we get to this point so that we are set up for success and don’t create irreversible catastrophic harm on the way.

So what's the plan?
===================

The following is my best guess for what we should do AT LEAST, but I haven’t thought about it deeply and would hope that the current plans of everyone who’s trying to build AGI are significantly better. This is very much a “throw the kitchen sink at the problem” approach with almost no theoretical grounding. I think a better version of this approach would do a few things differently, e.g.

1. **Explicit assumptions:** It should make more concrete explicit assumptions about where the risk comes from, how much risk we’d expect, what our safety budget is, and what risks we’d be willing to take.
2. **Defense in depth:**The current version is mostly “let’s try different strategies and stack them to reduce risks.” A better version of the plan would choose these different efforts as an explicit defense-in-depth approach where we have strong evidence that the measures are uncorrelated or even anti-correlated such that they cover each other’s weaknesses.
3. **Consistency:**I think the outlined plan is inconsistent in a bunch of ways, e.g. if we assume that the AI company is not willing to pause for more than 3 months, they might also not be willing to accept higher costs for transparent CoT.

The plan is divided into two layers, where the first layer seems absolutely required to me, i.e. any plan that doesn’t include these would very likely yield catastrophically bad results. The second layer is still very important and reduces risk substantially, but is a lower priority than the first layer, in my opinion. Note that this is already very triaged, i.e. there is a third, fourth, and fifth layer that I think a great plan would contain that I don’t even mention here because the post explicitly makes very conservative assumptions about the success of various alignment strategies.

Intuitively, if we were building a car, this plan is the “could we at least add breaks”-plan that doesn’t even consider techniques like airbags, ABS, ESC, seatbelts, or crumple zones.

Layer 1
-------

Everything in this section seems very important to me. In short,

1. We should try hard to keep a paradigm with faithful and human-legible CoT
2. If we have a paradigm with faithful and legible CoT (where the internal and external reasoning align), our main defense should be based on very detailed monitoring of reasoning and actions.
3. If we have a paradigm without faithful and legible CoT, our main defense should be based on control (that doesn’t assume human-legible CoT).
4. In both worlds, we should use the other, i.e. control/monitoring, as a second line of defense.
5. In all worlds, we should understand why, how, and when models scheme significantly better than we do now.
6. For all of the above, we need strong evals. Both in order to gather evidence whether our monitoring and control techniques catch the most important cases, as well as to get a better sense of models’ capabilities and propensities more broadly.
7. Under all circumstances, physical and cyber security needs to be high.

### Keep a paradigm with faithful and human-legible CoT

In the grand scheme of things, we got very lucky that a large part of the reasoning of current AI systems is directly visible and understandable in plain sight (assuming that the hidden CoT in o1 and o3 is human-legible).

By faithful and human-legible, I mean that the model’s reasoning is done in a way that is directly understandable by humans and accurately reflects the reasons for the model’s actions. It also excludes situations where the model does a lot of internal reasoning that differs from what the CoT states.

At a minimum, I think we should

1. All agree to keep this an important consideration for further development, e.g. be willing to take relevant capability hits (e.g. 2x higher cost for normal applications and up to 5x for high-stakes applications) if they lead to more understandable CoT.
2. Focus more effort on research on legible and faithful CoT. I feel like there are still a lot of low-hanging fruits to pick, e.g. building a suite of hundreds of evaluations to test whether we’d consider any particular model’s CoT as faithful or to understand which side effects directly optimizing for legibility has (such as hiding the undesired reasoning instead of removing it).
3. Deprioritize efforts to remove the visible CoT from our architecture, such as Meta’s [COCONUT](https://arxiv.org/abs/2412.06769).

Assuming the legibility tax isn’t that large (e.g. less than 2x), I feel like we’d be shooting ourselves in the foot if we were to build AGI that doesn’t use human-legible CoT from the point where we are now even under these conservative assumptions.

I think my view would be significantly changed if there was evidence that high-compute RL, as used in o1 and o3, leads to non-legible CoT, e.g. where the model develops its own language that is not trivially comprehensible to us. In such a world, I would want

1. The AI developers to share this information as soon as possible. I think the message “my model is a really good reasoner AND we don’t understand its reasoning” is significantly scarier than “my model is a really good reasoner BUT we understand its reasoning.”
2. This information should change what research and governance strategies should be prioritised. For example, I would want to put signficant effort into decoding whatever language the model has learned to use.

Relatedly, Daniel Kokotajlo has recently written about a concrete proposal in this direction in “[Why Don't We Just... Shoggoth+Face+Paraphraser?](https://www.lesswrong.com/posts/Tzdwetw55JNqFTkzK/why-don-t-we-just-shoggoth-face-paraphraser)”

### Significantly better (CoT, action & white-box) monitoring

In the world where we have models *with* human-legible CoT, my main line of defense would go through really detailed monitoring (and control that doesn’t assume human-legible CoT would be the second line of defense).

Better monitoring seems like an incredibly cost-effective yet neglected approach. Clearly, it would be desirable to have multiple simple monitors analyzing model outputs for a number of generic failure modes and bad behaviors at all times. The kinds of behaviors we could be tracking could, for example, include:

1. **Different types of scheming,**e.g. whether the model is hiding a particular goal, attempting to reduce oversight, taking actions that it knows to be not in the user's interest, and more.
2. **Different types of power-seeking**, e.g. whether they try to acquire resources, try to reduce their access restrictions, try to persuade others in some systematic way, and more.
3. **Strong broad goal-directedness**, e.g. when models appear to strongly pursue a specific goal across many context windows. This requires a comparison between contexts.

There are many possible ways these could be implemented, e.g. we could have black-box-only monitors such as smaller-but-faster models that constantly run in parallel (like Gemini-flash to monitor Gemini) or simple white-box probes trained to detect these problematic behaviors (e.g. linear probes or SAE probes). I would also want to both monitor the actions itself (e.g. tool calls) as well as the reasoning that led to them.

I expect that some model providers are already using online black box monitors for jailbreaks, so there already is a proof of concept. Simple linear probes are incredibly cost-effective (just a simple vector product) and we could run thousands of probes in parallel at almost zero additional overhead.

While these seem like simple approaches, I think nobody has really tried very hard to make them work in practice. Furthermore, while they are conceptually simple, they still require a lot of iteration and tuning, e.g. we would need to create good datasets to train and evaluate our probes and calibrate the thresholds such that they trigger in the correct cases but don’t provide too many false positives. Especially in the case where it is hard to build really good monitoring systems, we should know that as soon as possible so that AI developers can put more effort into them.

I think every AI lab should have a full team just to build these monitors, make sure they work as intended, analyze their outcomes, make them efficient to use, and more. I would prioritize efforts to build high-sensitivity monitors for high-stakes situations, e.g. developer-internal agentic deployments, over good monitors for average-stakes deployments, e.g. most chatbot use-cases.

My general feeling is that these monitors would both directly prevent harm but also unlock a lot of other benefits, e.g. we could understand the effectiveness of our alignment techniques faster and more thoroughly.

### Control (that doesn’t assume human-legible CoT)

In the world where we have models *without* human-legible CoT, my main line of defense would go through control that doesn’t assume human-legible CoT (and monitoring would be the second line of defense).

I specifically mean the [Redwood Research definition](https://arxiv.org/abs/2312.06942) of control, where we make the worst-case assumption that the model is scheming and it is not necessarily visible to us in CoT. We then attempt to develop protocols that maximize the usefulness of these models while minimizing risks.

While CoT monitoring might be useful for some control approaches, I specifically want to see further development of techniques that don’t assume that the CoT is legible to humans, as done by Redwood Research.

In general, I think the kind of work required for control is something like what Redwood has been doing just 100x more and applied to frontier systems by the AGI labs. Some concrete suggestions include:

1. **Agents:**We want control to work on frontier AI agents. Prior work has focused on minimally agentic systems or agents on smaller tasks. I think labs should aim to work on applying their control techniques on their most advanced systems as fast as possible to start getting practical experience with it.
2. **Realism:**Apply control in the kind of situations where we expect that we will need it the most, e.g. frontier LM agents doing AI R&D and whatever else frontier AI companies are using their AI systems internally.
3. **Rules for blue & red teams:**I think there are still a lot of open questions around what the blue and red teams are allowed to do for control protocols. Under some variants, the red team is completely overpowered and can almost certainly find a winning strategy, e.g. when it has access to all the knowledge of the blue team and is allowed to train against the blue team methods. While very conservative assumptions might be totally justified in relevant cases, I think we should be much more precise with what reasonable assumptions for the teams look like across different cases. My guess is that “reasonableness” can be derived from deployment assumptions, i.e. the red team is allowed to use anything that the model would have access to in a realistic deployment. In the case where the most conservative assumptions are correct in almost all cases, we should know this as soon as possible since this likely makes defense significantly harder.
4. **Relaxed assumptions:**The assumptions of control are intentionally conservative, e.g. it assumes that the model is constantly scheming. We might be able to define tighter bounds that provide similar safety but add fewer constraints (for more, see Ryan Greenblatt’s writing, e.g. [here](https://www.lesswrong.com/posts/GCqoks9eZDfpL8L3Q/how-to-prevent-collusion-when-using-untrusted-models-to?commentId=XrENSNCXqWMwfek3f)).

This is just a small subset of directions in control. Afaik there will be a significantly more detailed list of control projects and open problems soon.

### Much deeper understanding of scheming

By the time we have AI systems that drastically speed up or replace core researchers at AI lab, I think we should have a much better understanding of scheming. Concretely, we should

1. **Detection tools:** Have significantly better tools to detect scheming in the first place, e.g. a much larger suite of black-box evaluations and better white-box techniques.
2. **How scheming develops:** Have a much better understanding of when and how scheming develops. Concretely, we should understand where power-seeking tendencies come from, how models learn non-myopic tendencies, and when models would be willing to scheme for these tendencies.
3. **Real-world propensities:** Understand how often scheming-related behavior appears in practice. For example, I think it would be very insightful to analyze 100 million real model responses, especially in agentic settings, and see how often models do something like scheming in them. This seems like a low-effort, high-insight project (but requires access to a large amount of real deployment data).
4. **Hidden scheming:** Understand which training methods lead to less scheming vs. less detectible scheming. For example, punishing your model every time it shows scheming behavior may lead to less scheming, or it might just get better at hiding it. My guess is that we could say much more about which situations prioritize one over the other if we studied it more.
5. **Prepare responses:** Think about what we would do in response to different scheming-related evidence. For example, under which circumstances would we do nothing, retrain the model, or throw away the model entirely? Buck Shlegeris has written about this, e.g. [here](https://www.lesswrong.com/posts/YTZAmJKydD5hdRSeG/would-catching-your-ais-trying-to-escape-convince-ai), [here](https://www.lesswrong.com/posts/i2nmBfCXnadeGmhzW/catching-ais-red-handed), and [here](https://www.lesswrong.com/posts/jg3PuE3fYL9jq9zHB/win-continue-lose-scenarios-and-execute-replace-audit).
6. **More capability evals:** Understand how capable models are when they are scheming, e.g. how easy it is for them to subvert oversight or mess with their training in undesired and hidden ways. An example of this would be extended work on the sleeper agents model organisms.

I expect that a lot of this work is on model organisms, i.e. where researchers actively study one particular part of scheming in isolation similar to [Sleeper Agents](https://arxiv.org/abs/2401.05566) or Ryan Greenblatt+Anthropic’s work on [Alignment faking in large language models](https://arxiv.org/abs/2412.14093).

### Evals

Evals are a cornerstone of a lot of frontier safety commitments, and I think they are a useful evidence-gathering tool that can inform other strategies. Within this plan, evals fulfill two important roles.

1. **Support other strategies:**Evals are the default tool to determine whether our monitoring or control approaches are working. My guess is that building the evals for these approaches is at least as much work as coming up with the approach itself. Given the stakes at hand, we would want to have a lot of confidence in these evaluations and have a large range of evals with broad coverage.
2. **General information gathering:**Beyond the support that evals provide for the other components of this plan, they are very useful to give a general overview of the capabilities and propensities that the models have. Concretely, I think we should make progress on the following efforts:
   1. **Capability evaluations:**We should continue to build more and better capability evaluations, especially for AI R&D, scheming, CBRN, cyber, and persuasion. Having a detailed understanding of what current models are capable of continues to seem very important to me.
   2. **Elicitation:**How do we elicit maximal capabilities from a model such that we can make statements about approximate upper bounds? How can we quantify “how hard we tried” or how close we are to maximal elicitation?
   3. **Predictive evals:**What is the correct way to predict capabilities ahead of time? How can we know when we would start seeing signal on a capability benchmark that all models currently get 0 performance on? I’m optimistic about various ideas related to [observational scaling laws](https://arxiv.org/abs/2405.10938), but I think there are many other good things to try.
   4. **Alignment evals:**So far, most efforts have been focused on capability evaluations. I think we now have to start shifting significantly more effort on alignment / propensity evaluations. More and more capability benchmarks show meaningful signal, so we need to start tracking propensities. By default, I would encourage people to build adversarial alignment evals, e.g. honeypots for power-seeking, scheming, non-myopic preferences, and more. Broadly speaking, we should be able to build a detailed “psychological profile” of any new model for their default tendencies, e.g. similar to the [MACHIAVELLI benchmark](https://aypan17.github.io/machiavelli/) but in much more detail.
   5. **Demos:**The information the researchers find has to be communicated to a range of people, e.g. other scientists, decision-makers within AI companies, and policymakers. For some of these, the correct form of communication is a rigorous paper that carefully considers all possible alternative explanations. For others, it is a salient demonstration in a setting that they (or their constituents) intuitively understand and care about. Demos can be the difference between a problem being perceived as theoretical and distant versus real and urgent.

Overall, I think there should be significantly more resources in evals, see e.g. [the evals gap](https://www.apolloresearch.ai/blog/evalsgap) (other safety efforts should also be funded more).

### Security

Improved information and physical security seems like an important layer of defense for many failure modes. We need to ensure that model weights and algorithmic secrets cannot get stolen, that models cannot exfiltrate themselves, and that no internal employees can run large, unmonitored finetuning runs. I think the [report on securing model weights](https://www.rand.org/pubs/research_reports/RRA2849-1.html) is great and we should basically treat its recommendations as a good default (though it’s plausible that more thinking would suggest a slightly different strategy). Buck Shlegeris’ post, “[Access to powerful AI might make computer security radically easier](https://redwoodresearch.substack.com/p/access-to-powerful-ai-might-make),” also makes important recommendations.

I guess that the core challenge under short timelines will be correct prioritization. It is likely impossible to implement everything that would be suggested in the SL5 recommendations of the “securing model weights” report within the next 2-3 years. Thus, triaging seems necessary. I could also imagine that a lot of the security strategies that are important right around the point when an AI company automates their AI R&D have a few years of development time and might not feel immediately required right now, so they will only exist if an AI developer is acting now with a lot of foresight.

Finally, I’d have hoped that the internal infosec teams at frontier AI companies get access to frontier models ~3 months before external deployment both so they can defensively harden their infosec as well as conduct offensive testing. My guess is that this is not the norm, but in a sane world, an AI company would do something like using their own models to improve their own defensive capabilities before they release it. I expect this is largely blocked by inertia and company-internal politics. So, making this a norm as soon as possible would likely go a long way.

Unfortunately, I’m not an expert in security and would welcome concrete suggestions for a short-timeline security strategy from someone who is.

Layer 2
-------

Everything in this layer still seems quite important to me, but it is less important than those in layer 1.

### Improved near-term alignment strategies

I think RLHF and RLAIF empirically work better than I would have expected in ~2020. For example, they make the model more robustly behave as I want it to, the model can infer my intentions better, and the HHH training generalizes further than I had anticipated.

For example, I did not expect that the models would internalize HHH strongly enough to be willing to scheme for it, e.g. in [Alignment faking in large language models](https://arxiv.org/abs/2412.14093) and in our [follow-up experiments on in-context scheming](https://www.lesswrong.com/posts/qGRk7uF92Gcmq2oeK/ablations-for-frontier-models-are-capable-of-in-context). While I think this should be considered evidence that current alignment techniques go “deeper” than some people thought, it also opens up new problems.

Since our existing techniques can already introduce non-myopic and non-corrigible tendencies into the models, I think we should spend significantly more effort ensuring that these techniques keep the models myopic and corrigible. Furthermore, I think we should understand which kind of goals the models get in a lot more detail, e.g. in our [follow-up experiments](https://www.lesswrong.com/posts/qGRk7uF92Gcmq2oeK/ablations-for-frontier-models-are-capable-of-in-context), it seemed that “the models just want to be maximally helpful” was not the best description of the goals revealed preferences and at least to some extent they also showed some self-preservation without this being instrumental to their helpfulness. I would like to understand this in much more detail and build fine-grained “cognitive profiles” that we closely track for various alignment techniques.

I also expect that the strategies for internal and external use should differ meaningfully. For example, making models jailbreak-resistant could decrease their corrigibility. However, if you intend to deploy the model only to highly trusted internal staff, you don’t have to train it against jailbreaks. I’m currently unsure which training techniques you would want to use for agentic long-horizon internal deployments, e.g. because jailbreaks might be less relevant but taking non-power-seeking actions is much more relevant.

Likely, the main bottleneck to success is building tests and environments that are stable enough that we’d be happy to iterate against them (not necessarily train against them, but at least regularly evaluate on them).

### Continued work on interpretability, scalable oversight, superalignment & co

I like efforts going into improving fundamental research in interpretability, scalable oversight, superalignment & co (this is broadly the category for empirical research that is not covered in layer 1) and I want people to continue to make progress on the fundamentals. However, I think in a short-timeline world, figuring out the fundamentals first is too risky of a bet and I deprioritize them in this plan.

There are three types of efforts I would want to see in particular:

1. **Continued fundamental research:**Continuous refinement of conceptual clarity, methods, and evaluation techniques but not on the use cases that we ultimately want them to use for. For example, “[Debating with More Persuasive LLMs Leads to More Truthful Answers](https://arxiv.org/abs/2402.06782)” uses a dataset that has ~zero safety relevance but is a good way to test and showcase the method.
2. **Horizontal applied bets:**Use state-of-the-art tools in these fields and apply them to a use-case that strongly resembles the use-case we expect to find when there is human-level automated R&D. For example, this could be something like “train an SAE on our frontier model and try to make the best possible ‘flag-bad-behavior’-monitor we can build,” or “use the techniques from the debate paper on the environments in [Sabotage Evaluations for Frontier Models](https://arxiv.org/abs/2410.21514v1).”
3. **Preparing for human-level AI R&D:**I think it’s possible that short timeline logic changes how to prioritize research efforts. For example, it might be logical to almost exclusively do conceptual work and write 100 project proposals that can then be executed by the AIs instead of doing a lot of empirical research yourself (I haven’t thought this through in detail, so the counterarguments might be overwhelming).

My current guess is that none of these techniques are good enough that we would want to put a lot of confidence in them but I think they could be used as a supporting argument in an overall defense-in-depth approach. Of course, I’d love to be proven wrong and find out that any of them could be fully load-bearing.

### Reasoning transparency

I think AI companies should make their reasoning around safety plans for human-level AGI more transparent. For example, voluntary commitments like safety frameworks were a good step in the right direction. They allowed externals to understand the broad strokes of these plans and criticize them. I think not every criticism was accurate or helpful, but I expect it to be highly net positive. I also liked Anthropic's “[Three Sketches of ASL-4 Safety Case Components](https://alignment.anthropic.com/2024/safety-cases/)” and would like to see more efforts in this direction.

Realistically, I think the priorities should be roughly:

1. **Communicate the plan internally:**Whatever the best current version of the plan is should be communicated with all important decision-makers within the organization. If the plan is not very developed, that should be communicated as well. In the best case, I think the internal plan should be fully transparent and explicit about assumptions like the safety budget, risk the organization is implicitly willing to take, clear red lines, etc. For example, if the risk tolerance of the leadership is much higher than that of the average employee, then employees should be aware of that, in my opinion.
2. **Communicate the plan with external experts:**I think there are big benefits to communicating these plans with external experts, e.g. from independent organizations, academia, or AI safety institutes. This has many reasons, e.g. specific expertise, uncorrelated thinking, different incentives, and more. Again, I think it would be sensible to be fully transparent with the external experts and e.g. have NDAs with them.
3. **Communicate the plan with the general public:**Morally speaking, I think companies should share their plans in quite a lot of detail with the public. If your organization states that they are building a technology as powerful as AGI that affects approximately everyone, I think it would be reasonable for approximately everyone to be able to understand why they should or shouldn’t expect this technology to be safe. In practice, I understand that PR is typically risk-averse and thus, I don’t expect this to happen in the scope I’d like it to. Even under PR constraints, I think it is entirely possible for an AI developer to publish something significantly more detailed than the [Anthropic RSP](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy) or [safety case sketch](https://alignment.anthropic.com/2024/safety-cases/), and would like to see that.

### Safety first culture

I think an organization that aims to build AGI should ideally have internalized a safety-first approach at all levels. Everyone, from leadership to interns, has to understand the magnitude of what they’re working on and the implications if they make mistakes. The kind of culture I have in mind can likely only be found in militaries today, if at all. I think we’re currently very far away from that culture and not on track to reach it.

A few examples of my desired culture include:

1. Safety has to be deeply integrated into the entire development process. I think some AI companies often treat these as separate processes where they first have a “capabilities phase” where they build the most capable model and then a “safety phase” where they apply their safety procedures afterward. With more capable models, this is incredibly risky since the most capable models might already cause significant harm during development, e.g. attempt to exfiltrate their weights. At a minimum, I think AI companies should move toward continuous safety testing during development, such as running evals at intermediary checkpoints to track behavior over time.
2. I think there should be an obvious understanding within the organization that new capability advances are first used for safety, e.g. for cybersecurity hardening. These norms should be established now, not only when we reach these capabilities.
3. Treat safety as an asset. The more parts of the AI development process can be automated, the more important a safety mindset becomes. Since capability gains are less reliant on humans, integrity will be a very valuable resource for most human researchers. At the point where we have reliable automated researchers and engineers, some seemingly unconventional actions might suddenly become rational. For example, it might be reasonable to fire the N% least trustworthy employees and instead give the remaining (100-N)% more access to compute. The risks of reckless actions just become too big at that point.

I think it’s plausible that the question of whether AI will be the best or worst technology that humanity has built may come down to a few high-stakes decisions that are made with little time and under high pressure. I find it hard to see a world where we make the best decisions unless safety is top of mind for all people involved.

Assuming short timelines, I think it’s likely impossible to reach my desired levels of safety culture. This implies that

1. **We should triage:**If I had to prioritize, I think the most important part of the culture should be that the leadership is in agreement on what evidence they would need to see to pause any further development and actively seek that evidence. Furthermore, they should encourage a culture where pointing out potential safety flaws is seen as expected & positive rather than hindering & negative.
2. **Think about plans that assume that the safety culture is insufficient:**In practice, this likely looks like significant restrictions on most employees since the default assumption is that you cannot trust their decision-making. This is likely bad for employee happiness but might be required in the absence of a military-level safety culture.

Known limitations and open questions
====================================

I already list some of the limitations above, but want to give a bit more context here.

1. **Generic improvements:**As I said in the beginning, this plan should really be seen more as an encouragement to come up with a better plan than a particularly good plan in itself. I’d be particularly interested in missing pieces of layer 1 or people who would prioritize substantially differently, assuming short timelines. I’m less interested in feedback like “If we had substantially more time, I’d do X.”
2. **Explicit assumptions:** A better version of this post would make more concrete explicit assumptions about where the risk comes from, how much risk we’d expect, what our safety budget is, and what risks the AI developer would be willing to take. I think a better plan would have a much stronger connection between these high-level assumptions and the concrete actions taken. For example, I think it would be interesting for someone to do the exercise of “assume our safety budget is X and our risk is Y, which actions seem feasible, and how much risk reduction do we expect to get from this budget compared to not doing anything at all.” This will be hard to quantify but even basic guesstimates would already be informative.
3. **Defense in depth:**The current version is mostly “let’s try different strategies and stack them to reduce risks.” A better version of the plan would choose these different efforts as an explicit defense-in-depth approach where we have strong evidence that the measures are uncorrelated or even anti-correlated such that they cover each other’s weaknesses. I’d be very interested in empirical experiments to compare the failure modes of different approaches in practice and see where and how they are correlated. For example, I’d be keen to know whether the failures of black-box monitors and simple white-box probes are correlated or not.
4. **Details:**The proposed plan is just a high-level sketch. Every single section could be its own 50-page report. I’d love to see really detailed write-ups for each section. For example, I’d be interested to see a really detailed write-up about which monitors to build, how to prioritize them, how to measure their efficacy, how to make them more efficient, and all the other little details that make things hard in practice.
