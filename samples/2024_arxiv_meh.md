---
url: https://arxiv.org/html/2412.20138v1
title: "TradingAgents: Multi-Agents LLM Financial Trading Framework"
date: 2024-12-28
novelty: 0.15
---

TradingAgents: Multi-Agents LLM Financial Trading Framework
Yijia Xiao1, Edward Sun1, Di Luo2, Wei Wang1
Abstract

Significant progress has been made in automated problem-solving using societies of agents powered by large language models (LLMs). In finance, efforts have largely focused on single-agent systems handling specific tasks or multi-agent frameworks independently gathering data. However, multi-agent systems’ potential to replicate real-world trading firms’ collaborative dynamics remains underexplored. TradingAgents proposes a novel stock trading framework inspired by trading firms, featuring LLM-powered agents in specialized roles such as fundamental analysts, sentiment analysts, technical analysts, and traders with varied risk profiles. The framework includes Bull and Bear researcher agents assessing market conditions, a risk management team monitoring exposure, and traders synthesizing insights from debates and historical data to make informed decisions. By simulating a dynamic, collaborative trading environment, this framework aims to improve trading performance. Detailed architecture and extensive experiments reveal its superiority over baseline models, with notable improvements in cumulative returns, Sharpe ratio, and maximum drawdown, highlighting the potential of multi-agent LLM frameworks in financial trading.
Introduction

Autonomous agents leveraging Large Language Models (LLMs) present a transformative approach to decision-making by replicating human processes and workflows across various applications. These systems enhance the problem-solving capabilities of language agents by equipping them with tools and enabling collaboration with other agents, effectively breaking down complex problems into manageable components (Park et al. 2023; Havrilla et al. 2024; Talebirad and Nadiri 2023; Tang et al. 2024). One prominent application of these autonomous frameworks is in the financial market—a highly complex system influenced by numerous factors, including company fundamentals, market sentiment, technical indicators, and macroeconomic events.

Traditional algorithmic trading systems often rely on quantitative models that struggle to fully capture the complex interplay of diverse factors. In contrast, LLMs excel at processing and understanding natural language data, making them particularly effective for tasks that require textual comprehension, such as analyzing news articles, financial reports, and social media sentiment. Additionally, deep learning-based trading systems often suffer from low explainability, as they rely on hidden features that drive decision-making but are difficult to interpret. Recent advancements in multi-agent LLM frameworks for finance have shown significant promise in addressing these challenges. These frameworks create explainable AI systems, where decisions are supported by evidence and transparent reasoning (Li et al. 2023a; Wang et al. 2024b; Yu et al. 2024), demonstrating their potential in financial applications.

Despite their potential, most current applications of language agents in the financial and trading sectors face two significant limitations:

Lack of Realistic Organizational Modeling: Many frameworks fail to capture the complex interactions between agents that mimic the structure of real-world trading firms (Li et al. 2023a; Wang et al. 2024b; Yu et al. 2024). Instead, they focus narrowly on specific task performance, often disconnected from the organizational workflows and established human operating procedures proven effective in trading. This limits their ability to fully replicate and benefit from real-world trading practices.

Inefficient Communication Interfaces: Most existing systems use natural language as the primary communication medium, typically relying on message histories or an unstructured pool of information for decision-making (Park et al. 2023; Qian et al. 2024). This approach often results in a “telephone effect”, where details are lost, and states become corrupted as conversations lengthen. Agents struggle to maintain context and track extended histories while filtering out irrelevant information from previous decision steps, diminishing their effectiveness in handling complex, dynamic tasks. Additionally, the unstructured pool-of-information approach lacks clear instructions, forcing logical communication and information exchange between agents to depend solely on retrieval, which disrupts the relational integrity of the data.

In this work, we address these key limitations of existing models by introducing a system that overcomes these challenges. First, our framework bridges the gap by simulating the multi-agent decision-making processes typical of professional trading teams. It incorporates specialized agents tailored to distinct aspects of trading, inspired by the organizational structure of real-world trading firms. These agents include fundamental analysts, sentiment/news analysts, technical analysts, and traders with diverse risk profiles. Bullish and bearish debaters evaluate market conditions to provide balanced recommendations, while a risk management team ensures that exposures remain within acceptable limits. Second, to enhance communication, our framework combines structured outputs for control, clarity, and reasoning with natural language dialogue to facilitate effective debate and collaboration among agents. This hybrid approach ensures both precision and flexibility in decision-making.

We validate our framework through experiments on historical financial data, comparing its performance against multiple baselines. Comprehensive evaluation metrics, including cumulative return, Sharpe ratio, and maximum drawdown, are employed to assess its overall effectiveness.
Related Work
LLMs as Financial Assistants

Large Language Models (LLMs) are applied in finance by fine-tuning on financial data or training on financial corpora. This improves the model’s understanding of financial terminology and data, enabling a specialized assistant for analytical support, insights, and information retrieval, rather than trade execution.

Fine-Tuned LLMs for Finance

Fine-tuning enhances domain-specific performance. Examples include PIXIU (FinMA) (Xie et al. 2023), which fine-tuned LLaMA on 136K finance-related instructions; FinGPT (Yang, Liu, and Wang 2023), which used LoRA to fine-tune models like LLaMA and ChatGLM with about 50K finance-specific samples; and Instruct-FinGPT (Zhang, Yang, and Liu 2023), fine-tuned on 10K instruction samples from financial sentiment analysis datasets. These models outperform their base versions and other open-source LLMs like BLOOM and OPT (Zhang et al. 2022) in finance classification tasks, even surpassing BloombergGPT (Wu et al. 2023) in several evaluations. However, in generative tasks, they perform similarly or slightly worse than powerful general-purpose models like GPT-4, indicating a need for more high-quality, domain-specific datasets.

Finance LLMs Trained from Scratch

Training LLMs from scratch on finance-specific corpora aims for better domain adaptation. Models like BloombergGPT (Wu et al. 2023), XuanYuan 2.0 (Zhang, Yang, and Xu 2023), and Fin-T5 (Lu et al. 2023) combine public datasets with finance-specific data during pretraining. BloombergGPT, for instance, was trained on both general and financial text, with proprietary Bloomberg data enhancing its performance on finance benchmarks. These models outperform general-purpose counterparts like BLOOM-176B and T5 in tasks such as market sentiment classification and summarization. While they may not match larger closed-source models like GPT-3 or PaLM (Chowdhery et al. 2022), they offer competitive performance among similar-sized open-source models without compromising general language understanding.

In summary, finance-specific LLMs developed through fine-tuning or training from scratch show significant improvements in domain-specific tasks, underscoring the importance of domain adaptation and the potential for further enhancements with high-quality finance-specific datasets.

Refer to caption
Figure 1: TradingAgents Overall Framework Organization. I. Analysts Team: Four analysts concurrently gather relevant market information. II. Research Team: The team discusses and evaluates the collected data. III. Trader: Based on the researchers’ analysis, the trader makes the trading decision. IV. Risk Management Team: Risk guardians assess the decision against current market conditions to mitigate risks. V. Fund Manager: The fund manager approves and executes the trade.
LLMs as Traders

LLMs act as trader agents making direct trading decisions by analyzing external data like news, financial reports, and stock prices. Proposed architectures include news-driven, reasoning-driven, and reinforcement learning (RL)-driven agents.

News-Driven Agents

News-driven architectures integrate stock news and macroeconomic updates into LLM prompts to predict stock price movements. Studies evaluating both closed-source models (e.g., GPT-3.5, GPT-4) and open-source LLMs (e.g., Qwen (Bai et al. 2023), Baichuan (Yang et al. 2023)) in financial sentiment analysis have shown the effectiveness of simple long-short strategies based on sentiment scores (Lopez-Lira and Tang 2023). Further research on fine-tuned LLMs like FinGPT and OPT demonstrates improved performance through domain-specific alignment (Zhang et al. 2024a; Kirtac and Germano 2024). Advanced methods involve summarizing news data and reasoning about their relationship with stock prices (Fatouros et al. 2024a; Wang, Izumi, and Sakaji 2024).

Reasoning-Driven Agents

Reasoning-driven agents enhance trading decisions through mechanisms like reflection and debate. Reflection-driven agents, such as FinMem (Yu et al. 2023) and FinAgent (Zhang et al. 2024b), use layered memorization and multimodal data to summarize inputs into memories, inform decisions, and incorporate technical indicators, achieving superior backtest performance while mitigating hallucinations (Ji et al. 2023). Debate-driven agents, like those in heterogeneous frameworks (Xing 2024) and TradingGPT (Li et al. 2023b), enhance reasoning and factual validity by employing LLM debates among agents with different roles, improving sentiment classification and increasing robustness in trading decisions.

Reinforcement Learning-Driven Agents

Reinforcement learning methods align LLM outputs with expected behaviors, using backtesting as rewards. SEP (Koa et al. 2024) employs RL with memorization and reflection to refine LLM predictions based on market history. Classical RL methods are also used in trading frameworks that integrate LLM-generated embeddings with stock features, trained via algorithms like Proximal Policy Optimization (PPO) (Ding et al. 2023; Schulman et al. 2017).
LLMs as Alpha Miners

LLMs are also used to generate alpha factors instead of making direct trading decisions. QuantAgent (Wang et al. 2023) demonstrates this by leveraging LLMs to produce alpha factors through an inner-loop and outer-loop architecture. In the inner loop, a writer agent generates a script from a trader’s idea, while a judge agent provides feedback. In the outer loop, the code is tested in the real market, and trading results enhance the judge agent. This approach enables progressive approximation of optimal behavior.

Subsequent research, such as AlphaGPT (Wang et al. 2023), proposes a human-in-the-loop framework for alpha mining with a similar architecture. Both studies showcase the effectiveness of LLM-powered alpha mining systems, highlighting their potential in automating and accelerating the development of trading strategies by generating and refining alpha factors.
TradingAgents: Role Specialization

Assigning LLM agents clear, well-defined roles with specific goals enables the breakdown of complex objectives into smaller, manageable subtasks. Financial trading is a prime example of such complexity, demanding the integration of diverse signals, inputs, and specialized expertise. In the real world, this approach to managing complexity is demonstrated by trading firms that rely on expert teams to collaborate and make high-stakes decisions, underscoring the multifaceted nature of the task.

In a typical trading firm, vast amounts of data are collected, including financial metrics, price movements, trading volumes, historical performance, economic indicators, and news sentiment. This data is then analyzed by quantitative experts (quants), including mathematicians, data scientists, and engineers, using advanced tools and algorithms to identify trends and predict market movements.

Inspired by this organizational structure, TradingAgents defines seven distinct agent roles within a simulated trading firm: Fundamentals Analyst, Sentiment Analyst, News Analyst, Technical Analyst, Researcher, Trader, and Risk Manager. Each agent is assigned a specific name, role, goal, and set of constraints, alongside predefined context, skills, and tools tailored to their function. For example, a Sentiment Analyst is equipped with tools like web search engines, Reddit search APIs, X/Twitter search tools, and sentiment score calculation algorithms, while a Technical Analyst can execute code, calculate technical indicators, and analyze trading patterns. More specifically, TradingAgents assumes the following teams.
Analyst Team

The Analyst Team (Figure 2) is composed of specialized agents responsible for gathering and analyzing various types of market data to inform trading decisions. Each agent focuses on a specific aspect of market analysis, bringing together a comprehensive view of the market’s conditions.

Refer to caption
Figure 2: TradingAgents Analyst Team

    •

    Fundamental Analyst Agents: These agents evaluate company fundamentals by analyzing financial statements, earnings reports, insider transactions, and other pertinent data. They assess a company’s intrinsic value to identify undervalued or overvalued stocks, providing insights into long-term investment potential.
    •

    Sentiment Analyst Agents: These agents process large volumes of social media posts, sentiment scores, and insider sentiments derived from public information and social media activity. They gauge market sentiment to predict how collective investor behavior might impact stock prices in the short term.
    •

    News Analyst Agents: These agents analyze news articles, government announcements, and other macroeconomic indicators to assess the market’s macroeconomic state, major world events, and significant company changes. They identify news events that could influence market movements, helping to anticipate sudden shifts in market dynamics.
    •

    Technical Analyst Agents: These agents calculate and select relevant technical indicators, such as Moving Average Convergence Divergence (MACD) and Relative Strength Index (RSI), customized for specific assets. They analyze price patterns and trading volumes to forecast future price movements, assisting in timing entry and exit points.

Collectively, the Analyst Team synthesizes data from multiple sources to provide a holistic market analysis. Their combined insights form the foundational input for the Researcher Team, ensuring that all facets of the market are considered in subsequent decision-making processes.
Researcher Team

The Researcher Team (Figure 3) is responsible for critically evaluating the information provided by the Analyst Team. Comprised of agents adopting both bullish and bearish perspectives, they engage in multiple rounds of debate to assess the potential risks and benefits of investment decisions.

Refer to caption
Figure 3: TradingAgents Researcher Team: Bullish Perspectives and Bearish Perspectives

    •

    Bullish Researchers: These agents advocate for investment opportunities by highlighting positive indicators, growth potential, and favorable market conditions. They construct arguments supporting the initiation or continuation of positions in certain assets.
    •

    Bearish Researchers: Conversely, these agents focus on potential downsides, risks, and unfavorable market signals. They provide cautionary insights, questioning the viability of investment strategies and highlighting possible negative outcomes.

Through this dialectical process, the Researcher Team aims to reach a balanced understanding of the market situation. Their thorough analysis helps in identifying the most promising investment strategies while anticipating possible challenges, thus aiding the Trader Agents in making informed decisions.
Trader Agents

Trader Agents (Figure 4) are responsible for executing trading decisions based on the comprehensive analysis provided by the Analyst Team and the nuanced perspectives from the Researcher Team. They assess the synthesized information, considering both quantitative data and qualitative insights, to determine optimal trading actions.

Refer to caption
Figure 4: TradingAgents’s Trader Decision-Making Process

The tasks of TradingAgents Trader include:

    •

    Evaluating recommendations and insights from analysts and researchers.
    •

    Deciding on the timing and size of trades to maximize trading returns.
    •

    Placing buy or sell orders in the market.
    •

    Adjusting portfolio allocations in response to market changes and new information.

Trader Agents must balance potential returns against associated risks, making timely decisions in a dynamic market environment. Their actions directly impact the firm’s performance, necessitating a high level of precision and strategic thinking.
Risk Management Team

The Risk Management Team (Figure 5) monitors and controls the firm’s exposure to various market risks. These agents continuously evaluate the portfolio’s risk profile, ensuring that trading activities remain within predefined risk parameters and comply with regulatory requirements.

The responsibilities of Risk Management Team include:

    •

    Assessing factors such as market volatility, liquidity, and counterparty risks.
    •

    Implementing risk mitigation strategies, such as setting stop-loss orders or diversifying holdings.
    •

    Providing feedback to Trader Agents on risk exposures and suggesting adjustments to trading strategies.
    •

    Ensuring that the overall portfolio aligns with the firm’s risk tolerance and investment objectives.

Refer to caption
Figure 5: TradingAgents Risk Management Team and Fund Manager Approval Workflow

By offering oversight and guidance, the Risk Management Team helps maintain the firm’s financial stability and protect against adverse market events. They play a crucial role in safeguarding assets and ensuring sustainable long-term performance.

All agents in TradingAgents follow the ReAct prompting framework (Yao et al. 2023), which synergizes reasoning and acting. The environment state is shared and monitored by the agents, enabling them to take context-appropriate actions such as conducting research, executing trades, engaging in debates, or managing risks. This design ensures a collaborative, dynamic decision-making process reflective of real-world trading systems.
TradingAgents: Agent Workflow
Communication Protocol

Most existing LLM-based agent frameworks use natural language as the primary communication interface, typically through structured message histories or collections of agent-generated messages (Fatouros et al. 2024b; Li et al. 2023a; Yang et al. 2024; Yang, Yue, and He 2023). However, relying solely on natural language often proves insufficient for solving complex, long-term tasks that require extensive planning horizons. In such cases, pure natural language communication can resemble a game of telephone—over multiple iterations, initial information may be forgotten or distorted due to context length limitations and an overload of text that obscures critical earlier details (Hong et al. 2024). To address this limitation, we draw inspiration from frameworks like MetaGPT, which adopt a structured approach to communication. Our model introduces a structured communication protocol to govern agent interactions. Our model introduces a structured communication protocol to govern agent interactions. By clearly defining each agent’s state, we ensure that each role only extracts or queries the necessary information, processes it, and returns a completed report. This streamlined approach reduces unnecessary steps, lowers the risk of message corruption, and keeps interactions focused and efficient, even in complex, long-horizon tasks.
Types of Agent Interactions

In contrast to previous multi-agent trading frameworks, which rely heavily on natural language dialogue, TradingAgents agents communicate primarily through structured documents and diagrams. These documents encapsulate the agents’ insights in concise, well-organized reports that preserve essential content while avoiding irrelevant information. By utilizing structured reports, agents can query necessary details directly from the global state, eliminating the need for lengthy conversations that risk diluting information, extending the message state indefinitely, and causing data loss. The types of documents and the information they contain are detailed below:

    •

    Analyst Team: Fundamental, sentiment, news, and technical analysts compile their research and findings into concise analysis reports specific to their areas of expertise. These reports include key metrics, insights, and recommendations based on their specialized analyses.
    •

    Traders: Traders review and analyze the reports from the analysts, carefully deliberating to produce clear decision signals. They accompany these decisions with detailed reports explaining their rationale and supporting evidence, which are later utilized by the risk management team.

Agents engage in natural language dialogue exclusively during agent-to-agent conversations and debates. These concise, focused discussions have been shown to promote deeper reasoning and integrate diverse perspectives, enabling more balanced decisions in complex, long-horizon scenarios—a method particularly relevant to the intricate environment of trading (Du et al. 2023). This approach seamlessly integrates with our structured framework, as the conversation state is recorded as a structured entry within the overall agent state. The types of communication in these scenarios are detailed below:

    •

    Researcher Team: Each researcher agent queries the global agent state for analyst reports and carefully forms their opinion. Two researchers represent opposing perspectives: one bullish and one bearish. They engage in natural language dialogue for n rounds, as determined by the debate facilitator agent. At the conclusion, the facilitator reviews the debate history, selects the prevailing perspective, and records it as a structured entry in the communication protocol.
    •

    Risk Management Team: The risk management team, similar to the researcher team, queries the trader’s decision and accompanying report. They then deliberate from three perspectives—risk-seeking, neutral, and risk-conservative—to adjust the trading plan within risk constraints. They engage in n rounds of natural language discussion, guided by a facilitator agent.
    •

    Fund manager: The fund manager reviews the discussion from the risk management team, determines the appropriate risk adjustments, and updates the trader’s decision and report states within the communication protocol.

Backbone LLMs

To meet the diverse complexity and speed demands of tasks in our framework, we strategically select Large Language Models (LLMs) based on their strengths. Quick-thinking models, such as gpt-4o-mini and gpt-4o, efficiently handle fast, low-depth tasks like summarization, data retrieval, and converting tabular data to text (OpenAI et al. 2024). In contrast, deep-thinking models like o1-preview excel in reasoning-intensive tasks such as decision-making, evidence-based report writing, and data analysis. These models leverage their architectures for multi-round reasoning, producing logically sound, in-depth insights (Zhong et al. 2024; Wang et al. 2024a; OpenAI 2024). Additionally, we prioritize models with proven reliability and scalability to ensure optimal performance across various market conditions. We also employ auxiliary expert models for specialized tasks like sentiment analysis.

Specifically, all analyst nodes rely on deep-thinking models to ensure robust analysis, while quick-thinking models handle data retrieval from APIs and tools for efficiency. Researchers and traders use deep-thinking models to generate valuable insights and support well-informed decisions. By aligning the choice of LLMs with the specific requirements of each task, our framework achieves a balance between efficiency and depth of reasoning, which is crucial for effective trading strategies.

This implementation strategy ensures that TradingAgents can be deployed without requiring a GPU, relying only on API credits. It also introduces seamless exchangeability of backbone models, enabling researchers to effortlessly replace the model with any locally hosted or API-accessible alternatives in the future. This adaptability supports the integration of improved reasoning models or finance-tuned models customized for specific tasks. As a result, TradingAgents is highly scalable and future-proof, offering flexibility to accommodate any backbone model for any of its agents.
Experiments

In this section, we describe the experimental setup used to evaluate our proposed framework. We also provide detailed descriptions of the evaluation metrics employed to assess performance comprehensively.
Table 1: Performance comparison across all methods using four evaluation metrics. Results highlighted in green represent the best-performing statistic for each model. The improvement row illustrates TradingAgents’s performance gains over the top-performing baselines.
Categories 	Models 	AAPL 		GOOGL 		AMZN
CR%↑ 	ARR%↑ 	SR↑ 	MDD%↓ 		CR%↑ 	ARR%↑ 	SR↑ 	MDD%↓ 		CR%↑ 	ARR%↑ 	SR↑ 	MDD%↓
Market 	B&H 	-5.23 	-5.09 	-1.29 	11.90 		7.78 	8.09 	1.35 	13.04 		17.1 	17.6 	3.53 	3.80
Rule-based 	MACD 	-1.49 	-1.48 	-0.81 	4.53 		6.20 	6.26 	2.31 	1.22 		- 	- 	- 	-
KDJ&RSI 	2.05 	2.07 	1.64 	1.09 		0.4 	0.4 	0.02 	1.58 		-0.77 	-0.76 	-2.25 	1.08
ZMR 	0.57 	0.57 	0.17 	0.86 		-0.58 	0.58 	2.12 	2.34 		-0.77 	-0.77 	-2.45 	0.82
	SMA 	-3.2 	-2.97 	-1.72 	3.67 		6.23 	6.43 	2.12 	2.34 		11.01 	11.6 	2.22 	3.97
Ours 	TradingAgents 	26.62 	30.5 	8.21 	0.91 		24.36 	27.58 	6.39 	1.69 		23.21 	24.90 	5.60 	2.11
Improvement(%) 	24.57 	28.43 	6.57 	- 		16.58 	19.49 	4.26 	- 		6.10 	7.30 	2.07 	-
Back Trading

To simulate a realistic trading environment, we utilize a multi-asset and multi-modal financial dataset comprising of various stocks such as Apple, Nvidia, Microsoft, Meta, Google, and more. The dataset includes:

    •

    Historical Stock Prices: Open, high, low, close, volume, and adjusted close prices from January 1st, 2024, to March 29th, 2024.
    •

    News Articles: Daily news updates are gathered from diverse sources such as Bloomberg, Yahoo, EODHD, FinnHub, and Reddit, covering specific company developments, global events, macroeconomic trends, and government updates.
    •

    Social Media Posts and Sentiment: Posts from Reddit, X/Twitter, and other platforms along with sentiment scores of posts calculated by auxiliary language models.
    •

    Insider Sentiments and Transactions: Sentiment derived from public information, including transactions from SEDI and relevant company filings.
    •

    Financial Statements and Earnings Reports: Quarterly and annual reports filed by companies.
    •

    Company Profiles and Financial History: Descriptions of company profiles, target industries, and financial history reported by third parties.
    •

    Technical Indicators: Sixty standard technical analysis indicators calculated for each asset, including MACD, RSI, Bollinger Bands, etc.

Simulation Setup

We simulate the trading environment for the period from June 19, 2024, to November 19, 2024. TradingAgents facilitates seamless plug-and-play strategies during the simulation, enabling straightforward comparisons with any baseline. Agents make decisions based solely on data available up to each trading day, ensuring no future data is used (eliminating look-ahead bias). Based on their analysis, TradingAgents generates trading signals to buy, sell, or hold assets, which are then executed. Afterward, analysis metrics are calculated before proceeding to the next day’s data.
Baseline Models

We compare our TradingAgents framework against several baselines:

    •

    Buy and Hold: Investing equal amounts in all selected stocks and holding them throughout the simulation period.
    •

    MACD (Moving Average Convergence Divergence): A trend-following momentum strategy that generates buy and sell signals based on the crossover points between the MACD line and signal line.
    •

    KDJ and RSI (Relative Strength Index): A momentum strategy combining KDJ (stochastic oscillator) and RSI (relative strength index) indicators to identify overbought and oversold conditions for trading signals.
    •

    ZMR (Zero Mean Reversion): A mean reversion trading strategy that generates signals based on price deviations from and subsequent reversions to a zero reference line.
    •

    SMA (Simple Moving Average): A trend-following strategy that generates trading signals based on crossovers between short-term and long-term moving averages.

Evaluation Metrics

Refer to caption
((a)) Cumulative Returns on AAPL
Refer to caption
((b)) TradingAgents Transactions for AAPL.
Green / Red Arrows for Long / Short Positions.
Figure 6: TradingAgents: Cumulative Returns (CR) and Detailed Transaction History for AAPL.

To thoroughly evaluate the performance of our TradingAgents framework, we use widely recognized metrics to assess the risk management, profitability, and safety of the TradingAgents strategy in comparison to baseline approaches. Here we describe these metrics:
Cumulative Return (CR)

The cumulative return measures the total return generated over the simulation period. It is calculated as:
	
CR=(Vend−VstartVstart)×100%
		(1)

where Vend is the portfolio value at the end of the simulation, and Vstart is the initial portfolio value.
Annualized Return (AR)

The annualized return normalizes the cumulative return over the number of years:
	
AR=((VendVstart)1N−1)×100%
		(2)

where N is the number of years in the simulation.
Sharpe Ratio (SR)

The Sharpe ratio measures risk-adjusted return by comparing a portfolio’s excess return over the risk-free rate to its volatility:
	
SR=R¯−Rfσ
		(3)

where R¯ is the average portfolio return, Rf is the risk-free rate (e.g., yield of 3-month Treasury bills), and σ is the standard deviation of the portfolio returns.
Maximum Drawdown (MDD)

Maximum drawdown measures the largest peak-to-trough decline in the portfolio value:
	
MDD=maxt∈[0,T]⁡(Peakt−TroughtPeakt)×100%
		(4)
Results and Analysis

In this section, we present the results of our experiments and discuss the performance of our framework compared to the baseline models.
Performance Comparison
Cumlative and Annual Returns

Table 1 and Figure 6, 7, 8 highlight that our method significantly outperforms existing rule-based trading baselines, particularly in profitability, as measured by returns. TradingAgents achieves at least a 23.21% cumulative return and 24.90% annual return on the three sampled stocks, outperforming the best-performing baselines by a margin of at least 6.1%. Notably, on the AAPL stock—a particularly challenging case due to market volatility during the testing period—traditional methods struggled, as their patterns failed to generalize to this situation. In contrast, TradingAgents excelled even under these adverse conditions, achieving returns exceeding 26% within less than three months.
Sharpe Ratio

The Sharpe Ratio performance highlights TradingAgents’s exceptional ability to deliver superior risk-adjusted returns, consistently outperforming all baseline models across AAPL, GOOGL, and AMZN with Sharpe Ratios of at least 5.60—surpassing the next best models by a significant margin of at least 2.07 points. This result underscores TradingAgents’s effectiveness in balancing returns against risk, a critical metric for sustainable and predictable investment growth. By excelling over market benchmarks like Buy-and-Hold and advanced strategies such as KDJRSI, SMA, MACD, and ZMR, TradingAgents demonstrates its adaptability and robustness in diverse market conditions. Its ability to maximize returns while maintaining controlled risk exposure establishes a solid foundation for multi-agent and debate-based automated trading algorithms.
Maximum Drawdown

While rule-based baselines demonstrated superior performance in controlling risk, as reflected by their maximum drawdown scores, they fell short in capturing high returns. This trade-off between risk and reward underscores TradingAgents’s strength as a balanced approach. Despite higher returns being typically associated with higher risks, TradingAgents maintained a relatively low maximum drawdown compared to many baselines. Its effective risk-control mechanisms, facilitated by the debates among risk-control agents, ensured that the maximum drawdown remained within a manageable limit, not exceeding 2. This demonstrates TradingAgents’s capability to strike a robust balance between maximizing returns and managing risk effectively.
Explainability

A significant drawback of current deep learning methods for trading is their dense and complex architectures, which often render the decisions made by trading agents indecipherable to humans. This challenge, rooted in the broader issue of AI explainability, is particularly critical for trading agents, as they operate in real-world financial markets, often involving substantial sums of money where incorrect decisions can lead to severe consequences and losses.

In contrast, an LLM-based agentic framework for trading offers a transformative advantage: its operations and decisions are communicated in natural language, making them highly interpretable to humans. To illustrate this, we provide the full trading log of TradingAgents for a single day in the Appendix, showcasing its use of the ReAct-style prompting framework (Yao et al. 2023). Each decision made by the agents is accompanied by detailed reasoning, tool usage, and thought processes, enabling traders to easily understand and debug the system. This transparency empowers traders to fine-tune and adjust the framework to account for factors influencing decisions, offering a significant edge in explainability over traditional deep-learning trading algorithms.
Discussion

Our results demonstrate that integrating multiple specialized LLM agents and fostering agentic debate significantly enhances trading performance. This framework efficiently synthesizes diverse data sources and expert analyses, enabling trader agents to make well-informed decisions tailored to specific risk profiles. The inclusion of a reflective agent and a dedicated risk management team is pivotal in refining strategies and mitigating risks. As a result, the framework achieves exceptional return capture while maintaining strong risk management metrics, striking an optimal balance between maximizing rewards and minimizing risks. Additionally, the natural language-based operations of the multi-agent LLM framework ensure high explainability, giving TradingAgents a distinct advantage over traditional and deep learning methods in transparency and interpretability.
Conclusion

In this paper, we introduced TradingAgents, an LLM-agent-powered stock trading framework that simulates a realistic trading firm environment with multiple specialized agents engaging in agentic debates and conversations. Leveraging the capabilities of LLMs to process and analyze diverse data sources, the framework enables informed trading decisions while utilizing multi-agent interactions to enhance performance through comprehensive reasoning and debate before acting. By integrating agents with distinct roles and risk profiles, along with a reflective agent and a dedicated risk management team, TradingAgents significantly improves trading outcomes and risk management compared to baseline models. Additionally, the collaborative nature of these agents ensures adaptability to varying market conditions. Extensive experiments demonstrate that TradingAgents outperforms traditional trading strategies and baselines in cumulative return, Sharpe ratio, and other critical metrics. Future work will focus on deploying the framework in a live trading environment, expanding agent roles, and incorporating real-time data processing to enhance performance further.
Acknowledgments

We would like to acknowledge the advice from Yinggan Xu.
References

    Bai et al. (2023)

Bai, J.; Bai, S.; Chu, Y.; Cui, Z.; Dang, K.; Deng, X.; Fan, Y.; Ge, W.; Han, Y.; Huang, F.; Hui, B.; Ji, L.; Li, M.; Lin, J.; Lin, R.; Liu, D.; Liu, G.; Lu, C.; Lu, K.; Ma, J.; Men, R.; Ren, X.; Ren, X.; Tan, C.; Tan, S.; Tu, J.; Wang, P.; Wang, S.; Wang, W.; Wu, S.; Xu, B.; Xu, J.; Yang, A.; Yang, H.; Yang, J.; Yang, S.; Yao, Y.; Yu, B.; Yuan, H.; Yuan, Z.; Zhang, J.; Zhang, X.; Zhang, Y.; Zhang, Z.; Zhou, C.; Zhou, J.; Zhou, X.; and Zhu, T. 2023. Qwen Technical Report. arXiv:2309.16609.
Chowdhery et al. (2022)
Chowdhery, A.; Narang, S.; Devlin, J.; Bosma, M.; Mishra, G.; Roberts, A.; Barham, P.; Chung, H. W.; Sutton, C.; Gehrmann, S.; Schuh, P.; Shi, K.; Tsvyashchenko, S.; Maynez, J.; Rao, A.; Barnes, P.; Tay, Y.; Shazeer, N.; Prabhakaran, V.; Reif, E.; Du, N.; Hutchinson, B.; Pope, R.; Bradbury, J.; Austin, J.; Isard, M.; Gur-Ari, G.; Yin, P.; Duke, T.; Levskaya, A.; Ghemawat, S.; Dev, S.; Michalewski, H.; Garcia, X.; Misra, V.; Robinson, K.; Fedus, L.; Zhou, D.; Ippolito, D.; Luan, D.; Lim, H.; Zoph, B.; Spiridonov, A.; Sepassi, R.; Dohan, D.; Agrawal, S.; Omernick, M.; Dai, A. M.; Pillai, T. S.; Pellat, M.; Lewkowycz, A.; Moreira, E.; Child, R.; Polozov, O.; Lee, K.; Zhou, Z.; Wang, X.; Saeta, B.; Diaz, M.; Firat, O.; Catasta, M.; Wei, J.; Meier-Hellstern, K.; Eck, D.; Dean, J.; Petrov, S.; and Fiedel, N. 2022. PaLM: Scaling Language Modeling with Pathways. arXiv:2204.02311.
Ding et al. (2023)
Ding, Y.; Jia, S.; Ma, T.; Mao, B.; Zhou, X.; Li, L.; and Han, D. 2023. Integrating Stock Features and Global Information via Large Language Models for Enhanced Stock Return Prediction. arXiv:2310.05627.
Du et al. (2023)
Du, Y.; Li, S.; Torralba, A.; Tenenbaum, J. B.; and Mordatch, I. 2023. Improving Factuality and Reasoning in Language Models through Multiagent Debate. arXiv:2305.14325.
Fatouros et al. (2024a)
Fatouros, G.; Metaxas, K.; Soldatos, J.; and Kyriazis, D. 2024a. Can Large Language Models Beat Wall Street? Unveiling the Potential of AI in Stock Selection. arXiv:2401.03737.
Fatouros et al. (2024b)
Fatouros, G.; Metaxas, K.; Soldatos, J.; and Kyriazis, D. 2024b. Can Large Language Models Beat Wall Street? Unveiling the Potential of AI in Stock Selection. arXiv:2401.03737.
Havrilla et al. (2024)
Havrilla, A.; Du, Y.; Raparthy, S. C.; Nalmpantis, C.; Dwivedi-Yu, J.; Zhuravinskyi, M.; Hambro, E.; Sukhbaatar, S.; and Raileanu, R. 2024. Teaching Large Language Models to Reason with Reinforcement Learning. arXiv:2403.04642.
Hong et al. (2024)
Hong, S.; Zhuge, M.; Chen, J.; Zheng, X.; Cheng, Y.; Zhang, C.; Wang, J.; Wang, Z.; Yau, S. K. S.; Lin, Z.; Zhou, L.; Ran, C.; Xiao, L.; Wu, C.; and Schmidhuber, J. 2024. MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. arXiv:2308.00352.
Ji et al. (2023)
Ji, Z.; Yu, T.; Xu, Y.; Lee, N.; Ishii, E.; and Fung, P. 2023. Towards Mitigating Hallucination in Large Language Models via Self-Reflection. arXiv:2310.06271.
Kirtac and Germano (2024)
Kirtac, K.; and Germano, G. 2024. Sentiment trading with large language models. Finance Research Letters, 62: 105227.
Koa et al. (2024)
Koa, K. J.; Ma, Y.; Ng, R.; and Chua, T.-S. 2024. Learning to Generate Explainable Stock Predictions using Self-Reflective Large Language Models.
Li et al. (2023a)
Li, Y.; Yu, Y.; Li, H.; Chen, Z.; and Khashanah, K. 2023a. TradingGPT: Multi-agent system with layered memory and distinct characters for enhanced financial trading performance. arXiv preprint arXiv:2309.03736.
Li et al. (2023b)
Li, Y.; Yu, Y.; Li, H.; Chen, Z.; and Khashanah, K. 2023b. TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance. arXiv:2309.03736.
Lopez-Lira and Tang (2023)
Lopez-Lira, A.; and Tang, Y. 2023. Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models. arXiv:2304.07619.
Lu et al. (2023)
Lu, D.; Wu, H.; Liang, J.; Xu, Y.; He, Q.; Geng, Y.; Han, M.; Xin, Y.; and Xiao, Y. 2023. BBT-Fin: Comprehensive Construction of Chinese Financial Domain Pre-trained Language Model, Corpus and Benchmark. arXiv:2302.09432.
OpenAI (2024)
OpenAI. 2024. Learning to Reason with LLMs - OpenAI O1 Model. https://openai.com/index/learning-to-reason-with-llms/. Accessed: 2024-11-21.
OpenAI et al. (2024)
OpenAI; Achiam, J.; Adler, S.; Agarwal, S.; Ahmad, L.; Akkaya, I.; Aleman, F. L.; Almeida, D.; Altenschmidt, J.; Altman, S.; Anadkat, S.; Avila, R.; Babuschkin, I.; Balaji, S.; Balcom, V.; Baltescu, P.; Bao, H.; Bavarian, M.; Belgum, J.; Bello, I.; Berdine, J.; Bernadett-Shapiro, G.; Berner, C.; Bogdonoff, L.; Boiko, O.; Boyd, M.; Brakman, A.-L.; Brockman, G.; Brooks, T.; Brundage, M.; Button, K.; Cai, T.; Campbell, R.; Cann, A.; Carey, B.; Carlson, C.; Carmichael, R.; Chan, B.; Chang, C.; Chantzis, F.; Chen, D.; Chen, S.; Chen, R.; Chen, J.; Chen, M.; Chess, B.; Cho, C.; Chu, C.; Chung, H. W.; Cummings, D.; Currier, J.; Dai, Y.; Decareaux, C.; Degry, T.; Deutsch, N.; Deville, D.; Dhar, A.; Dohan, D.; Dowling, S.; Dunning, S.; Ecoffet, A.; Eleti, A.; Eloundou, T.; Farhi, D.; Fedus, L.; Felix, N.; Fishman, S. P.; Forte, J.; Fulford, I.; Gao, L.; Georges, E.; Gibson, C.; Goel, V.; Gogineni, T.; Goh, G.; Gontijo-Lopes, R.; Gordon, J.; Grafstein, M.; Gray, S.; Greene, R.; Gross, J.; Gu, S. S.; Guo, Y.; Hallacy, C.; Han, J.; Harris, J.; He, Y.; Heaton, M.; Heidecke, J.; Hesse, C.; Hickey, A.; Hickey, W.; Hoeschele, P.; Houghton, B.; Hsu, K.; Hu, S.; Hu, X.; Huizinga, J.; Jain, S.; Jain, S.; Jang, J.; Jiang, A.; Jiang, R.; Jin, H.; Jin, D.; Jomoto, S.; Jonn, B.; Jun, H.; Kaftan, T.; Łukasz Kaiser; Kamali, A.; Kanitscheider, I.; Keskar, N. S.; Khan, T.; Kilpatrick, L.; Kim, J. W.; Kim, C.; Kim, Y.; Kirchner, J. H.; Kiros, J.; Knight, M.; Kokotajlo, D.; Łukasz Kondraciuk; Kondrich, A.; Konstantinidis, A.; Kosic, K.; Krueger, G.; Kuo, V.; Lampe, M.; Lan, I.; Lee, T.; Leike, J.; Leung, J.; Levy, D.; Li, C. M.; Lim, R.; Lin, M.; Lin, S.; Litwin, M.; Lopez, T.; Lowe, R.; Lue, P.; Makanju, A.; Malfacini, K.; Manning, S.; Markov, T.; Markovski, Y.; Martin, B.; Mayer, K.; Mayne, A.; McGrew, B.; McKinney, S. M.; McLeavey, C.; McMillan, P.; McNeil, J.; Medina, D.; Mehta, A.; Menick, J.; Metz, L.; Mishchenko, A.; Mishkin, P.; Monaco, V.; Morikawa, E.; Mossing, D.; Mu, T.; Murati, M.; Murk, O.; Mély, D.; Nair, A.; Nakano, R.; Nayak, R.; Neelakantan, A.; Ngo, R.; Noh, H.; Ouyang, L.; O’Keefe, C.; Pachocki, J.; Paino, A.; Palermo, J.; Pantuliano, A.; Parascandolo, G.; Parish, J.; Parparita, E.; Passos, A.; Pavlov, M.; Peng, A.; Perelman, A.; de Avila Belbute Peres, F.; Petrov, M.; de Oliveira Pinto, H. P.; Michael; Pokorny; Pokrass, M.; Pong, V. H.; Powell, T.; Power, A.; Power, B.; Proehl, E.; Puri, R.; Radford, A.; Rae, J.; Ramesh, A.; Raymond, C.; Real, F.; Rimbach, K.; Ross, C.; Rotsted, B.; Roussez, H.; Ryder, N.; Saltarelli, M.; Sanders, T.; Santurkar, S.; Sastry, G.; Schmidt, H.; Schnurr, D.; Schulman, J.; Selsam, D.; Sheppard, K.; Sherbakov, T.; Shieh, J.; Shoker, S.; Shyam, P.; Sidor, S.; Sigler, E.; Simens, M.; Sitkin, J.; Slama, K.; Sohl, I.; Sokolowsky, B.; Song, Y.; Staudacher, N.; Such, F. P.; Summers, N.; Sutskever, I.; Tang, J.; Tezak, N.; Thompson, M. B.; Tillet, P.; Tootoonchian, A.; Tseng, E.; Tuggle, P.; Turley, N.; Tworek, J.; Uribe, J. F. C.; Vallone, A.; Vijayvergiya, A.; Voss, C.; Wainwright, C.; Wang, J. J.; Wang, A.; Wang, B.; Ward, J.; Wei, J.; Weinmann, C.; Welihinda, A.; Welinder, P.; Weng, J.; Weng, L.; Wiethoff, M.; Willner, D.; Winter, C.; Wolrich, S.; Wong, H.; Workman, L.; Wu, S.; Wu, J.; Wu, M.; Xiao, K.; Xu, T.; Yoo, S.; Yu, K.; Yuan, Q.; Zaremba, W.; Zellers, R.; Zhang, C.; Zhang, M.; Zhao, S.; Zheng, T.; Zhuang, J.; Zhuk, W.; and Zoph, B. 2024. GPT-4 Technical Report. arXiv:2303.08774.
Park et al. (2023)
Park, J. S.; O’Brien, J. C.; Cai, C. J.; Morris, M. R.; Liang, P.; and Bernstein, M. S. 2023. Generative Agents: Interactive Simulacra of Human Behavior. arXiv:2304.03442.
Qian et al. (2024)
Qian, C.; Liu, W.; Liu, H.; Chen, N.; Dang, Y.; Li, J.; Yang, C.; Chen, W.; Su, Y.; Cong, X.; Xu, J.; Li, D.; Liu, Z.; and Sun, M. 2024. ChatDev: Communicative Agents for Software Development. arXiv:2307.07924.
Schulman et al. (2017)
Schulman, J.; Wolski, F.; Dhariwal, P.; Radford, A.; and Klimov, O. 2017. Proximal Policy Optimization Algorithms. arXiv:1707.06347.
Talebirad and Nadiri (2023)
Talebirad, Y.; and Nadiri, A. 2023. Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents. arXiv:2306.03314.
Tang et al. (2024)
Tang, X.; Zou, A.; Zhang, Z.; Li, Z.; Zhao, Y.; Zhang, X.; Cohan, A.; and Gerstein, M. 2024. MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning. arXiv:2311.10537.
Wang et al. (2024a)
Wang, K.; Li, J.; Bhatt, N. P.; Xi, Y.; Liu, Q.; Topcu, U.; and Wang, Z. 2024a. On The Planning Abilities of OpenAI’s o1 Models: Feasibility, Optimality, and Generalizability. arXiv:2409.19924.
Wang, Izumi, and Sakaji (2024)
Wang, M.; Izumi, K.; and Sakaji, H. 2024. LLMFactor: Extracting Profitable Factors through Prompts for Explainable Stock Movement Prediction. arXiv:2406.10811.
Wang et al. (2024b)
Wang, S.; Yuan, H.; Ni, L. M.; and Guo, J. 2024b. QuantAgent: Seeking Holy Grail in Trading by Self-Improving Large Language Model. arXiv:2402.03755.
Wang et al. (2023)
Wang, S.; Yuan, H.; Zhou, L.; Ni, L. M.; Shum, H.-Y.; and Guo, J. 2023. Alpha-gpt: Human-ai interactive alpha mining for quantitative investment. arXiv preprint arXiv:2308.00016.
Wu et al. (2023)
Wu, S.; Irsoy, O.; Lu, S.; Dabravolski, V.; Dredze, M.; Gehrmann, S.; Kambadur, P.; Rosenberg, D.; and Mann, G. 2023. BloombergGPT: A Large Language Model for Finance. arXiv:2303.17564.
Xie et al. (2023)
Xie, Q.; Han, W.; Zhang, X.; Lai, Y.; Peng, M.; Lopez-Lira, A.; and Huang, J. 2023. PIXIU: A Large Language Model, Instruction Data and Evaluation Benchmark for Finance. arXiv:2306.05443.
Xing (2024)
Xing, F. 2024. Designing Heterogeneous LLM Agents for Financial Sentiment Analysis. arXiv:2401.05799.
Yang et al. (2023)
Yang, A.; Xiao, B.; Wang, B.; Zhang, B.; Bian, C.; Yin, C.; Lv, C.; Pan, D.; Wang, D.; Yan, D.; Yang, F.; Deng, F.; Wang, F.; Liu, F.; Ai, G.; Dong, G.; Zhao, H.; Xu, H.; Sun, H.; Zhang, H.; Liu, H.; Ji, J.; Xie, J.; Dai, J.; Fang, K.; Su, L.; Song, L.; Liu, L.; Ru, L.; Ma, L.; Wang, M.; Liu, M.; Lin, M.; Nie, N.; Guo, P.; Sun, R.; Zhang, T.; Li, T.; Li, T.; Cheng, W.; Chen, W.; Zeng, X.; Wang, X.; Chen, X.; Men, X.; Yu, X.; Pan, X.; Shen, Y.; Wang, Y.; Li, Y.; Jiang, Y.; Gao, Y.; Zhang, Y.; Zhou, Z.; and Wu, Z. 2023. Baichuan 2: Open Large-scale Language Models. arXiv:2309.10305.
Yang, Liu, and Wang (2023)
Yang, H.; Liu, X.-Y.; and Wang, C. D. 2023. FinGPT: Open-Source Financial Large Language Models. arXiv:2306.06031.
Yang, Yue, and He (2023)
Yang, H.; Yue, S.; and He, Y. 2023. Auto-GPT for Online Decision Making: Benchmarks and Additional Opinions. arXiv:2306.02224.
Yang et al. (2024)
Yang, H.; Zhang, B.; Wang, N.; Guo, C.; Zhang, X.; Lin, L.; Wang, J.; Zhou, T.; Guan, M.; Zhang, R.; and Wang, C. D. 2024. FinRobot: An Open-Source AI Agent Platform for Financial Applications using Large Language Models. arXiv:2405.14767.
Yao et al. (2023)
Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan, K.; and Cao, Y. 2023. ReAct: Synergizing Reasoning and Acting in Language Models. arXiv:2210.03629.
Yu et al. (2023)
Yu, Y.; Li, H.; Chen, Z.; Jiang, Y.; Li, Y.; Zhang, D.; Liu, R.; Suchow, J. W.; and Khashanah, K. 2023. FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design. arXiv:2311.13743.
Yu et al. (2024)
Yu, Y.; Yao, Z.; Li, H.; Deng, Z.; Cao, Y.; Chen, Z.; Suchow, J. W.; Liu, R.; Cui, Z.; Zhang, D.; et al. 2024. FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making. arXiv preprint arXiv:2407.06567.
Zhang, Yang, and Liu (2023)
Zhang, B.; Yang, H.; and Liu, X.-Y. 2023. Instruct-FinGPT: Financial Sentiment Analysis by Instruction Tuning of General-Purpose Large Language Models. arXiv:2306.12659.
Zhang et al. (2024a)
Zhang, H.; Hua, F.; Xu, C.; Kong, H.; Zuo, R.; and Guo, J. 2024a. Unveiling the Potential of Sentiment: Can Large Language Models Predict Chinese Stock Price Movements? arXiv:2306.14222.
Zhang et al. (2022)
Zhang, S.; Roller, S.; Goyal, N.; Artetxe, M.; Chen, M.; Chen, S.; Dewan, C.; Diab, M.; Li, X.; Lin, X. V.; Mihaylov, T.; Ott, M.; Shleifer, S.; Shuster, K.; Simig, D.; Koura, P. S.; Sridhar, A.; Wang, T.; and Zettlemoyer, L. 2022. OPT: Open Pre-trained Transformer Language Models. arXiv:2205.01068.
Zhang et al. (2024b)
Zhang, W.; Zhao, L.; Xia, H.; Sun, S.; Sun, J.; Qin, M.; Li, X.; Zhao, Y.; Zhao, Y.; Cai, X.; Zheng, L.; Wang, X.; and An, B. 2024b. A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist. arXiv:2402.18485.
Zhang, Yang, and Xu (2023)
Zhang, X.; Yang, Q.; and Xu, D. 2023. XuanYuan 2.0: A Large Chinese Financial Chat Model with Hundreds of Billions Parameters. arXiv:2305.12002.
Zhong et al. (2024)

    Zhong, T.; Liu, Z.; Pan, Y.; Zhang, Y.; Zhou, Y.; Liang, S.; Wu, Z.; Lyu, Y.; Shu, P.; Yu, X.; Cao, C.; Jiang, H.; Chen, H.; Li, Y.; Chen, J.; Hu, H.; Liu, Y.; Zhao, H.; Xu, S.; Dai, H.; Zhao, L.; Zhang, R.; Zhao, W.; Yang, Z.; Chen, J.; Wang, P.; Ruan, W.; Wang, H.; Zhao, H.; Zhang, J.; Ren, Y.; Qin, S.; Chen, T.; Li, J.; Zidan, A. H.; Jahin, A.; Chen, M.; Xia, S.; Holmes, J.; Zhuang, Y.; Wang, J.; Xu, B.; Xia, W.; Yu, J.; Tang, K.; Yang, Y.; Sun, B.; Yang, T.; Lu, G.; Wang, X.; Chai, L.; Li, H.; Lu, J.; Sun, L.; Zhang, X.; Ge, B.; Hu, X.; Zhang, L.; Zhou, H.; Zhang, L.; Zhang, S.; Liu, N.; Jiang, B.; Kong, L.; Xiang, Z.; Ren, Y.; Liu, J.; Jiang, X.; Bao, Y.; Zhang, W.; Li, X.; Li, G.; Liu, W.; Shen, D.; Sikora, A.; Zhai, X.; Zhu, D.; and Liu, T. 2024. Evaluation of OpenAI o1: Opportunities and Challenges of AGI. arXiv:2409.18486.

Appendix A Appendix for TradingAgents
Cumulative Returns (CR) and Transaction History for AMZN and GOOGL

We present additional figures for $AMZN and $GOOGL stocks to complement the AAPL data discussed in the main body of this paper. These supplementary visuals provide a broader perspective on the performance of our trading framework across multiple stocks, highlighting the consistency and robustness of TradingAgents’s results.

Refer to caption
((a)) Cumulative Returns on AMZN
Refer to caption
((b)) TradingAgents Transactions for AMZN.
Green / Red Arrows for Long / Short Positions.
Figure 7: TradingAgents: Cumulative Returns (CR) and Detailed Transaction History for AMZN.

Refer to caption
((a)) Cumulative Returns on GOOGL
Refer to caption
((b)) TradingAgents Transactions for GOOGL.
Green / Red Arrows for Long / Short Positions.
Figure 8: TradingAgents: Cumulative Returns (CR) and Detailed Transaction History for GOOGL.

By including detailed analyses for AMZN and GOOGL, we aim to demonstrate the versatility of our approach in diverse market environments, thereby reinforcing the overall effectiveness and generalizability of our methodology.
TradingAgents Workflow: Role Specification and Cooperation

We offer a comprehensive overview of the various agent roles that collaborate within the TradingAgents. These roles include the Analyst Team, Researcher Team, Trader, Risk Management Team, and Fund Manager, each dedicated to different aspects of the trading process for Apple Inc. (Ticker: AAPL) as of November 19, 2024.

By detailing the responsibilities and interactions of each agent, we demonstrate how TradingAgents ensures thorough analysis, strategic trading decisions, and effective risk management. The collaborative structure not only enhances the system’s overall performance but also reinforces the transparency and explainability of TradingAgents, aligning with the objectives discussed in the main text. The following sections provide specific role specifications and illustrate how these agents work together to achieve robust and interpretable trading outcomes.

Market Analyst Team on Apple Inc. (Ticker: AAPL) [November 19, 2024]
1[Market Analyst]:
2================================== Report ==================================
3Based on the analysis of AAPL’s recent market data and selected technical indicators, here is a detailed and nuanced report of the trends observed:
4
5### Momentum Indicators
6- **RSI (Relative Strength Index)**: The RSI values indicate significant fluctuations, with periods of overbought conditions, particularly on November 5 and November 7, where RSI values reached 100 and 89.85, respectively. This suggests strong upward price movements, potentially leading to price corrections. The RSI stabilizes towards the end of the period, indicating moderate buying momentum.
7
8### Trend Indicators
9- **ADX (Average Directional Index)**: Initially, the ADX values are extremely high, indicating a strong trend, but they decline significantly, suggesting a weakening trend strength. This pattern implies a transition from a strong directional movement to a potential consolidation phase.
10
11- **Supertrend**: The supertrend indicator remains constant, suggesting a stable market trend without significant volatility. This stability might indicate a consolidation phase, with the potential for future breakouts.
12
13### Volatility Indicators
14- **Bollinger Bands**: The upward trend in Bollinger Bands suggests a bullish market phase with low volatility. The consistent rise in values indicates a positive market bias, with prices likely to continue rising if the trend persists.
15
16- **ATR (Average True Range)**: The ATR values show an increase in market volatility, peaking on November 7. This suggests heightened market activity, with sustained volatility towards the end of the period.
17
18### Volume Indicators
19- **VR (Volume Variation Index)**: The VR values highlight significant fluctuations in trading volume, with a notable spike on November 5. This indicates heightened market activity, possibly due to external factors influencing trader behavior.
20
21### Price Action and Support/Resistance
22- **CCI (Commodity Channel Index)**: The CCI values indicate volatility, with several instances of overbought conditions. Peaks on November 7, November 14, and November 18 suggest strong upward price movements, which could be followed by corrections.
23
24### Moving Averages
25- **MACD (Moving Average Convergence Divergence)**: The MACD values indicate a general upward trend, with some fluctuations and minor pullbacks. The increasing MACD values suggest bullish market sentiment, with the short-term moving average consistently above the long-term average.
26
27### Summary and Insights
28The analysis of AAPL’s recent market data reveals a period of volatility with alternating phases of strong buying momentum and stabilization. The initial overbought conditions and high ADX values suggest a strong trend, which weakens over time, indicating potential consolidation. The consistent upward trend in Bollinger Bands and MACD values points to a bullish market sentiment, while the fluctuations in ATR and VR values highlight ongoing market volatility.
29
30Traders should be cautious of potential price corrections following the overbought conditions and consider the possibility of continued volatility. The stable supertrend value suggests a consolidation phase, with potential for future breakouts. Overall, traders should remain vigilant, using these insights to adjust their strategies accordingly, while being prepared for both opportunities and risks presented by the current market conditions.
31================================ Tool Calls ================================
32Tool Calls:
33 get_YFin_data (call_TuDo4m3U0lkgtV61Qpq3UIiT)
34 Call ID: call_TuDo4m3U0lkgtV61Qpq3UIiT
35 Args:
36 symbol: AAPL
37 curr_date: 2024-11-19
38
39Based on the recent market data for Apple (AAPL) from November 4, 2024, to November 18, 2024, we can observe several key trends and patterns:
40
411. **Price Movement**: AAPL has shown a general upward trend over the period, with the stock price increasing from an opening of
42$220.75 on November 4 to a closing of $228.02 on November 18. The stock experienced fluctuations, with notable highs on November
437 and November 14, reaching $227.63 and $228.87, respectively.
44
452. **Volume Trends**: Trading volume varied significantly, with a peak on November 6 at 54,561,100 shares. This suggests heightened trading activity, possibly due to market events or investor sentiment changes.
46
473. **Dividend Payment**: A dividend of $0.25 per share was paid on November 8, which might have influenced investor behavior, potentially contributing to the price movements observed around this date.
48
494. **Volatility**: The stock showed some volatility, with daily price ranges (highs and lows) indicating active trading and potential market reactions to news or earnings reports.
50
51To provide a comprehensive analysis, I will select a set of technical indicators that can offer diverse insights into AAPL’s market behavior. These indicators will cover momentum, trend, volatility, volume, and price action aspects:
52
531. **RSI (Relative Strength Index)**: To assess momentum and identify overbought or oversold conditions.
542. **ADX (Average Directional Index)**: To evaluate the strength of the current trend.
553. **Bollinger Bands**: To analyze volatility and potential price breakouts.
564. **MACD (Moving Average Convergence Divergence)**: To identify trend changes and momentum.
575. **VWMA (Volume Weighted Moving Average)**: To understand price movements in relation to volume.
586. **ATR (Average True Range)**: To measure market volatility.
597. **Supertrend**: To identify trend direction and potential reversals.
608. **CCI (Commodity Channel Index)**: To identify cyclical trends and potential reversals.
61
62I will now retrieve detailed reports for these indicators to provide a nuanced analysis of AAPL’s market conditions.
63Tool Calls:
64 get_stockstats_indicators_report (call_rARQhoVdv6VyzI3a3R9hyhYh)
65 Call ID: call_rARQhoVdv6VyzI3a3R9hyhYh
66 Args:
67 symbol: AAPL
68 indicator: rsi
69 curr_date: 2024-11-19
70 get_stockstats_indicators_report (call_ODamPSS2si621zrEPb4mIitD)
71 Call ID: call_ODamPSS2si621zrEPb4mIitD
72 Args:
73 symbol: AAPL
74 indicator: adx
75 curr_date: 2024-11-19
76 get_stockstats_indicators_report (call_KWgyXj3GgdviC01u5KeFZkbQ)
77 Call ID: call_KWgyXj3GgdviC01u5KeFZkbQ
78 Args:
79 symbol: AAPL
80 indicator: boll
81 curr_date: 2024-11-19
82 get_stockstats_indicators_report (call_hshUKMGu1yvZ4m8YbJE9SaSg)
83 Call ID: call_hshUKMGu1yvZ4m8YbJE9SaSg
84 Args:
85 symbol: AAPL
86 indicator: macd
87 curr_date: 2024-11-19
88 get_stockstats_indicators_report (call_Iq9kq9jA2D5E7Png9lPt9bK5)
89 Call ID: call_Iq9kq9jA2D5E7Png9lPt9bK5
90 Args:
91 symbol: AAPL
92 indicator: vwma
93 curr_date: 2024-11-19
94 get_stockstats_indicators_report (call_SRSi644IhPjxaMdE7U8xn4a3)
95 Call ID: call_SRSi644IhPjxaMdE7U8xn4a3
96 Args:
97 symbol: AAPL
98 indicator: atr
99 curr_date: 2024-11-19
100 get_stockstats_indicators_report (call_Ow6VLKfP52JSFtphkJocda9f)
101 Call ID: call_Ow6VLKfP52JSFtphkJocda9f
102 Args:
103 symbol: AAPL
104 indicator: supertrend
105 curr_date: 2024-11-19
106 get_stockstats_indicators_report (call_FJYy18HBaxQlC8YghPphXpsB)
107 Call ID: call_FJYy18HBaxQlC8YghPphXpsB
108 Args:
109 symbol: AAPL
110 indicator: cci
111 curr_date: 2024-11-19
112
113The data provided spans from November 4, 2024, to November 18, 2024, and includes Commodity Channel Index (CCI) values, which measure the deviation of the price from its average. The CCI values indicate the following trends and insights:
114
1151. **Initial Missing Data**: On November 4, 2024, the CCI value is missing. This absence of data could be due to a lack of trading activity or data collection issues, which should be noted but does not provide insight into market conditions.
116
1172. **Positive Trend**: From November 5 to November 7, there is a noticeable upward trend in CCI values, starting at 66.67 and peaking at 133.33. This suggests a strong deviation from the average price, indicating potential overbought conditions. Traders might interpret this as a signal that the market could be due for a correction or pullback.
118
1193. **Fluctuations and Correction**: On November 8, the CCI decreases to 97.80, indicating a slight correction from the previous peak. This is followed by a significant drop to -9.75 on November 11, suggesting a shift towards oversold conditions. Such a rapid change could indicate increased volatility or a reaction to external market factors.
120
1214. **Recovery and Stabilization**: From November 12 to November 14, the CCI values recover, moving from 10.83 to 109.26. This recovery suggests a return to positive momentum, potentially indicating renewed buying interest or stabilization in the market.
122
1235. **Moderate Fluctuations**: On November 15, the CCI drops to 30.79, followed by an increase to 104.68 on November 18. These fluctuations suggest ongoing market adjustments, with the CCI remaining in positive territory, indicating that the market is still experiencing deviations above the average price.
124
125Overall, the data reflects a period of volatility with significant swings in market sentiment. The initial rise and subsequent fluctuations in CCI values suggest that traders should be cautious of potential overbought or oversold conditions. Monitoring these trends can help in making informed decisions about potential entry or exit points in the market.

News Analyst Team on Apple Inc. (Ticker: AAPL) [November 19, 2024]
1[Social Media Analyst]:
2================================== Report ==================================
3### Comprehensive Analysis of Apple Inc. (AAPL) Social Media and Sentiment Trends (November 12 - November 19, 2024)
4
5#### Social Media Insights
6Upon reviewing the Reddit data for Apple Inc. over the past week, it appears there were no significant posts or discussions captured in the dataset. This absence of data could suggest a lack of major events or announcements that typically drive social media engagement, or it might indicate a gap in data collection. For investors, this means relying more heavily on sentiment analysis and news reports for insights during this period.
7
8#### Sentiment Analysis
9The sentiment data for Apple Inc. (AAPL) from November 4, 2024, to November 17, 2024, reveals a dynamic landscape of public perception:
10
111. **Positive Sentiment Peaks**:
12- **November 15, 2024**: A significant positive sentiment was recorded with a normalized score of 0.5445, indicating favorable news or developments.
13- **November 11, 2024**: Another strong positive sentiment day with a score of 0.426, suggesting positive market reactions or announcements.
14
152. **Moderate Positive Sentiment**:
16- Several days, including November 14, 13, 10, and 9, showed moderately positive sentiment, reflecting a generally favorable outlook towards AAPL.
17
183. **Negative Sentiment**:
19- **November 12, 2024**: A negative sentiment score of -0.201 was observed, possibly due to unfavorable news or market conditions.
20- **November 4, 2024**: The period started with a negative sentiment score of -0.141, indicating initial concerns or negative news.
21
224. **Neutral Sentiment**:
23- **November 17, 2024**: The sentiment was neutral, suggesting a lack of significant positive or negative news impacting perceptions.
24
255. **Engagement Levels**:
26- The highest engagement was noted on November 6, 2024, with a sentiment score of 0.0756, indicating increased interest or discussions, albeit with a slightly positive sentiment.
27
28#### Implications for Traders and Investors
29- **Positive Sentiment Days**: The spikes in positive sentiment, particularly on November 15 and 11, could be indicative of favorable developments or market conditions that investors might want to capitalize on.
30- **Negative Sentiment Days**: The negative sentiment on November 12 and 4 suggests caution, as these days might have been influenced by adverse news or market reactions.
31- **Overall Trend**: The sentiment trend over the period is predominantly positive, suggesting a generally favorable outlook for AAPL. However, the occasional dips into negative sentiment highlight the importance of staying informed about potential risks or negative news.
32
33In conclusion, while the lack of Reddit data limits insights from social media discussions, the sentiment analysis provides a valuable perspective on market perceptions of Apple Inc. during this period. Investors should consider these sentiment trends alongside other market data and news to make informed decisions.
34================================ Tool Calls ================================
35Tool Calls:
36 get_reddit_stock_info (call_MfJT2mtj22GO32q7Xu5z2htS)
37 Call ID: call_MfJT2mtj22GO32q7Xu5z2htS
38 Args:
39 query: Apple Inc
40 start_date: 2024-11-12
41 end_date: 2024-11-19
42 get_EODHD_sentiment (call_So5Csrkq4CJKpi9jiY4ibbB2)
43 Call ID: call_So5Csrkq4CJKpi9jiY4ibbB2
44 Args:
45 symbol: AAPL
46 curr_date: 2024-11-19
47EODHD client initialized
48Reddit client initialized
49Searching in subreddit: wallstreetbets
50Searching in subreddit: stocks
51Searching in subreddit: investing
52Searching in subreddit: SecurityAnalysis
53Searching in subreddit: Finance
54Searching in subreddit: Economics
55
56The market sentiment data for AAPL over the period from November 4, 2024, to November 17, 2024, provides insights into the prevailing attitudes and perceptions surrounding the stock. Below is a detailed analysis of the sentiment trends observed during this period:
57
581. **November 17, 2024**: The sentiment count was 1, with a normalized sentiment score of 0. This indicates a neutral sentiment on this day, suggesting no significant positive or negative sentiment was detected.
59
602. **November 16, 2024**: The sentiment count was 1, with a normalized sentiment score of -0.06. This reflects a slightly negative sentiment, although the impact appears minimal given the low count and score.
61
623. **November 15, 2024**: The sentiment count increased to 2, with a normalized sentiment score of 0.5445. This marks a significant positive sentiment, indicating a favorable perception of AAPL on this day.
63
644. **November 14, 2024**: The sentiment count was 2, with a normalized sentiment score of 0.17. This suggests a moderately positive sentiment, showing a generally favorable outlook.
65
665. **November 13, 2024**: The sentiment count was 2, with a normalized sentiment score of 0.3245. This indicates a positive sentiment, with a noticeable improvement in perception compared to the previous day.
67
686. **November 12, 2024**: The sentiment count was 2, with a normalized sentiment score of -0.201. This reflects a negative sentiment, suggesting some unfavorable views or news impacting AAPL.
69
707. **November 11, 2024**: The sentiment count was 3, with a normalized sentiment score of 0.426. This indicates a strong positive sentiment, with increased engagement and favorable perception.
71
728. **November 10, 2024**: The sentiment count was 3, with a normalized sentiment score of 0.3157. This suggests a positive sentiment, maintaining a favorable outlook similar to the previous day.
73
749. **November 09, 2024**: The sentiment count was 3, with a normalized sentiment score of 0.221. This indicates a positive sentiment, though slightly less pronounced than the previous days.
75
7610. **November 08, 2024**: The sentiment count was 1, with a normalized sentiment score of 0.422. This reflects a strong positive sentiment, despite the lower engagement count.
77
7811. **November 07, 2024**: The sentiment count was 2, with a normalized sentiment score of 0.144. This suggests a mildly positive sentiment, indicating a generally favorable view.
79
8012. **November 06, 2024**: The sentiment count was 5, with a normalized sentiment score of 0.0756. This shows a slightly positive sentiment with the highest engagement count, suggesting increased interest or discussion around AAPL.
81
8213. **November 05, 2024**: The sentiment count was 4, with a normalized sentiment score of 0.304. This indicates a positive sentiment, with a relatively high level of engagement.
83
8414. **November 04, 2024**: The sentiment count was 3, with a normalized sentiment score of -0.141. This reflects a negative sentiment, suggesting some unfavorable sentiment or news at the start of the period.
85
86**Summary**: Over the analyzed period, AAPL experienced fluctuations in market sentiment, with notable positive sentiment spikes on November 15 and November 11. The sentiment was predominantly positive, with occasional dips into negative territory, particularly on November 12 and November 04. The engagement levels varied, with the highest count observed on November 06, indicating heightened interest or discussion on that day. Overall, the sentiment trend suggests a generally favorable outlook for AAPL during this period, with some days of negative sentiment that may warrant further investigation.
