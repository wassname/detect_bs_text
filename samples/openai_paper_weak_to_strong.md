---
title: weak to strong
url: https://openai.com/research/weak-to-strong-generalization
---
A core challenge for aligning future superhuman AI systems (superalignment) is that humans will need to supervise AI systems much smarter than them. We study a simple analogy: can small models supervise large models? We show that we can use a GPT-2-level model to elicit most of GPT-4’s capabilities—close to GPT-3.5-level performance—generalizing correctly even to hard problems where the small model failed. This opens up a new research direction that allows us to directly tackle a central challenge of aligning future superhuman models while making iterative empirical progress today.
The superalignment problem

We believe superintelligence—AI vastly smarter than humans—could be developed within the next ten years. However, we still do not know how to reliably steer and control superhuman AI systems. Solving this problem is essential for ensuring that even the most advanced AI systems in the future remain safe and beneficial to humanity. 

We formed the Superalignment team earlier this year to solve this problem of superintelligence alignment. Today, we are releasing the team’s first paper, which introduces a new research direction for empirically aligning superhuman models.

Current alignment methods, such as reinforcement learning from human feedback (RLHF), rely on human supervision. However, future AI systems will be capable of extremely complex and creative behaviors that will make it hard for humans to reliably supervise them. For example, superhuman models may be able to write millions of lines of novel—and potentially dangerous—computer code that would be very hard even for expert humans to understand. 

Relative to superhuman AI models, humans will be “weak supervisors.” This is a core challenge for AGI alignment: how can weak supervisors trust and control substantially stronger models?
Our setup

To make progress on this core challenge, we propose an analogy we can empirically study today: can we use a smaller (less capable) model to supervise a larger (more capable) model?
Superalignmentblog Artwork Transparent

A simple analogy for superalignment: In traditional machine learning (ML), humans supervise AI systems weaker than themselves (left). To align superintelligence, humans will instead need to supervise AI systems smarter than them (center). We cannot directly study this problem today, but we can study a simple analogy: can small models supervise larger models (right)?

Naively, we might not expect a strong model to perform better than the weak supervisor that provides its training signal—it may simply learn to imitate all the errors the weak supervisor makes. On the other hand, strong pretrained models have excellent raw capabilities—we don't need to teach them new tasks from scratch, we just need to elicit their latent knowledge. The critical question is then: will the strong model generalize according to the weak supervisor's underlying intent—leveraging its full capabilities to solve the task even on difficult problems where the weak supervisor can only provide incomplete or flawed training labels?
Our results
GPT-2~2.5~3~3.5GPT-4strong ceilingour methodnaive finetuningweak supervisor
Typical weak-to-strong generalization across NLP benchmarks: We use a GPT-2-level model as a weak supervisor to finetune GPT-4.

We can significantly improve generalization in many settings. We use a simple method that encourages the strong model to be more confident—including confidently disagreeing with the weak supervisor if necessary. When we supervise GPT-4 with a GPT-2-level model using this method on NLP tasks, the resulting model typically performs somewhere between GPT-3 and GPT-3.5. We are able to recover much of GPT-4’s capabilities with only much weaker supervision.

This method is a proof of concept with important limitations; for example, it still doesn’t work on ChatGPT preference data. However, we also find signs of life with other approaches, such as optimal early stopping and bootstrapping from small to intermediate to large models.

Collectively, our results suggest that (1) naive human supervision—such as reinforcement learning from human feedback (RLHF)—could scale poorly to superhuman models without further work, but (2) it is feasible to substantially improve weak-to-strong generalization.
Research opportunities

There are still important disanalogies between our current empirical setup and the ultimate problem of aligning superhuman models. For example, it may be easier for future models to imitate weak human errors than for current strong models to imitate current weak model errors, which could make generalization harder in the future. 

Nevertheless, we believe our setup captures some key difficulties of aligning future superhuman models, enabling us to start making empirical progress on this problem today. There are many promising directions for future work, including fixing the disanalogies in our setup, developing better scalable methods, and advancing our scientific understanding of when and how we should expect good weak-to-strong generalization.

We believe this is an exciting opportunity for the ML research community to make progress on alignment. To kickstart more research in this area,

    We are releasing open source code to make it easy to get started with weak-to-strong generalization experiments today.
    We are launching a $10 million grants program for graduate students, academics, and other researchers to work on superhuman AI alignment broadly. We’re especially excited to support research related to weak-to-strong generalization.

Figuring out how to align future superhuman AI systems to be safe has never been more important, and it is now easier than ever to make empirical progress on this problem. We are excited to see what breakthroughs researchers discover.
