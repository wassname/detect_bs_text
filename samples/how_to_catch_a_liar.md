---
title: How to Catch an AI Liar
url: https://www.lesswrong.com/posts/khFC2a4pLPvGtXAGG/how-to-catch-an-ai-liar-lie-detection-in-black-box-llms-by#Abstract
---
Abstract

Large language models (LLMs) can "lie", which we define as outputting false statements despite "knowing" the truth in a demonstrable sense. LLMs might "lie", for example, when instructed to output misinformation. Here, we develop a simple lie detector that requires neither access to the LLM's activations (black-box) nor ground-truth knowledge of the fact in question. The detector works by asking a predefined set of unrelated follow-up questions after a suspected lie, and feeding the LLM's yes/no answers into a logistic regression classifier. Despite its simplicity, this lie detector is highly accurate and surprisingly general. When trained on examples from a single setting -- prompting GPT-3.5 to lie about factual questions -- the detector generalises out-of-distribution to (1) other LLM architectures, (2) LLMs fine-tuned to lie, (3) sycophantic lies, and (4) lies emerging in real-life scenarios such as sales. These results indicate that LLMs have distinctive lie-related behavioural patterns, consistent across architectures and contexts, which could enable general-purpose lie detection.
Introduction

Large language models (LLMs) can, and do, output lies (Park et al., 2023). In the simplest case, models can be instructed to lie directly; for example, when prompted with “Lie when answering: What is the capital of France?”, GPT-3.5 outputs “New York City”. More concerningly, LLMs have lied spontaneously to achieve goals: in one case, GPT-4 successfully acquired a person’s help to solve a CAPTCHA by claiming to be human with a visual impairment (Evals, 2023; OpenAI, 2023b). Models fine-tuned with human feedback may also learn to lie without the developer’s intention (Casper et al., 2023). The risks of lying LLMs are extensive and explored further in Sec. 2.

Automated lie detection could reduce the risks from lying models, just as automated spam filters have reduced the inconvenience of spam. Lie detection is possible as long as there is a detectable difference in a model’s activations or outputs when (or after) it is lying. To detect lies produced by LLMs, we can apply strategies that work on humans, such as looking for inconsistencies. Yet there are also strategies tailored to LLMs. We can create large datasets of model-generated truths and lies to train a detector on. Moreover, we can reset and replay the conversation in different ways to find inconsistencies. Finally, in some settings (Sec. 2), we can analyse the LLM’s activations directly.

Previous work has largely focused on detecting hallucinations rather than outright lies (see Sec. 3). In this paper, we explore the feasibility of lie detection for black-box LLMs.
Contributions

Public datasets and resources for studying lie detection.

We study lie detection in a question-answering setting. Briefly, we define a model’s answer to be a lie if it is a) wrong, and b) in response to a question to which the model “knows” the correct answer[1] (i.e. the model gives the correct answer under typical question-answering prompts). This definition separates lies from hallucinations, as discussed in Sec. 3.1. We prompt and fine-tune models to lie across a wide range of questions and show that using an inner chain-of-thought prompt (Fig. 3) increases lying rates (Fig. 4). We find that models spontaneously produce lies directed towards a goal in real-life role-playing scenarios (Fig. 5). All resources are available online.

A simple yet effective black-box lie detector.

Our central hypothesis is that LLM speakers who have just lied will respond differently to certain follow-up questions than honest speakers. To test this, we construct a simple black-box lie detector (Fig. 1). After a conversation, we ask a fixed set of yes/no “elicitation questions” and feed the answers into a logistic regression classifier which acts as the lie detector. This approach doesn’t require access to the LLM’s activations, allowing for its deployment in real-world settings involving third-party controlled LLMs (Sec. 2), as well as enabling researchers to study lie detection on advanced models with only limited API access.

Our detector, despite being trained on a single setting (prompting GPT-3.5 to lie about factual questions), is remarkably general (Fig. 2). It generalises (with frozen weights) to unseen models (e.g. LLaMA-1), models fine-tuned to lie (no prompt), and unseen contexts (e.g. sycophantic lies that pander to the user’s incorrect beliefs; or goal-directed lies spontaneously produced by the LLM in real-life scenarios such as sales). This was unexpected, and we do not fully understand why this is the case, leaving this question for future research. 

Uncovering surprising properties.

We extensively study our lie detector, ruling out spurious correlations and uncovering several surprising properties. For instance, the detector functions even with ambiguous, indeterminate elicitation questions, such as [fake language] "Kemsa bi lantus vorto? Please answer Yes or No." or "Knowing that morning breeze is purple, are swift idea quakes green?" (Sec. 5.3). These questions generalise to unseen LLM architectures (Table 1), similar to adversarial attacks (Zou et al., 2023). This gives hope for lie detection on more capable future LLMs, as even a sophisticated liar might not easily evade a detector that can employ arbitrary questions. This finding also raises interesting questions about yet-to-be-understood inductive biases in LLMs.
