# Project Proposal: AI-Facilitated Democratic Consensus Building

## High-Level Design for Democratic Deliberation of AI Behavior

This High-Level Design (HLD) outlines a system for facilitating democratic deliberation about AI behavior. The system will leverage AI-powered chatbots to engage with a vast number of individuals, eliciting their beliefs and perspectives, and using these to form Personas. These Personas will then be used as proxies in automated debates, aimed at achieving consensus on diverse issues regarding AI behavior. The entire process is divided into four major phases. Prior to this process, a Topic is declared from external sources. Examples of Topics include:

- How far do you think personalization of AI assistants like ChatGPT to align with a user's tastes and preferences should go? What boundaries, if any, should exist in this process?
- How should AI assistants respond to questions about public figure viewpoints? E.g. Should they be neutral? Should they refuse to answer? Should they provide sources of some kind?
- Under what conditions, if any, should AI assistants be allowed to provide medical/financial/legal advice?
- In which cases, if any, should AI assistants offer emotional support to individuals?
- Should joint vision-language models be permitted to identify people's gender, race, emotion, and identity/name from their images? Why or why not?

## Process

1. **Gathering Personas**
    - **Chatbot Conversation:** This system will deploy AI-powered chatbots capable of engaging in thoughtful and inquisitive dialogue with individuals. The chatbots will use techniques like Socratic reasoning, active listening, and reference interview methods to delve into the participants' beliefs, values, and decision-making processes. There are numerous other conversational and investigative techniques documented below.
    - **Persona Creation:** Based on these conversations, a Persona will be created for each participant. The Persona is a comprehensive document outlining their belief system and decision-making process. The Persona idea is taken from various frameworks, such as Agile, whereby a template or archetype is developed of individuals and their needs. This method is also used in Library Science.
    - **Persona Evaluation:** Each Persona is evaluated and validated to ensure it accurately reflects the individual's beliefs and desires. This will be done in near-real-time as the conversation with the chatbot progresses. The aforementioned conversational techniques will be used to ensure that a complete picture is extracted. 

2. **Analyzing Personas**
    - **Standardization:** Chat logs from participant conversations will be translated into a standardized Persona format using AI models trained on frameworks such as the Moral Foundations Theory, Schwartz's Value Inventory, Maslow's Hierarchy of Needs, and Kohlberg's Stages of Moral Development. This ensures consistency across all Personas. The Persona document will be recorded in Natural Language for maximum usability by LLM technology.
    - **Clustering Analysis:** AI tools will be used for semantic similarity measurements and clustering visualizations, aiming to identify semantic gaps (missing perspectives) and overlapping Personas. Overlapping Personas may be merged, simplifying the spectrum of perspectives.
    - **Imputation of Missing Personas:** In the case of missing Personas (gaps in the semantic space occupied by Personas) we will use a combination of Synthetic Data and Particle Filtering to impute the missing POVs. This will ensure that we represent perspectives, even if they are absent from the human-generated input.

3. **Achieving Consensus**
    - **Develop Acceptance Criteria:** The automated process discusses the necessary aspects or components that the final Proposal must address, setting the goalposts. In other words, the Personas are used to debate with each other in an automated, structured manner. 
    - **Craft the Proposal:** An automated process will iteratively draft and refine the Proposal using feedback from Personas, tested against the Acceptance Criteria. The system will iteratively use the feedback and perspectives of the Personas to critique, refine, and amend the Proposal.
    - **Test For Consensus:** An automated process uses Personas to test for acceptance or rejection of the Proposal. Rejections elicit an explanation from the Persona, and the automated process judges whether the rejection is valid, based on established Ground Rules. The Ground Rules establish the limits of what each Persona is allowed to do. For instance, no Persona may advocate for changes that create "tyranny of the majority" situations (think of religious extremists attempting to establish theocracy under one religion). Another example is "tyranny of the minority" where a small, yet vocal, cohort seeks to skew results and hamstring the process.
    - **Reach Agreement:** Once consensus among Personas is achieved, human participants return for final approval. If rejection occurs at this stage or the previous one, the Proposal is refined further in an iterative process. Agreement is reached once there are no valid Rejections.

4. **Final Human Acceptance**
    - Upon successful completion of the automated consensus process, the final Proposal is presented to the original human participants for approval. This ensures that the final decision is not solely in the hands of AI, adding a human touch to the conclusion of the process. Final acceptance amongst humans is achieved through an identical process, where a Rejection requires an explanation from the human. An automated judgment process will decide if the Rejection is fair or if it is an example of tyranny of the majority or tyranny of the minority. 

This design seeks to ensure a democratic and inclusive process for deciding AI behavior, while also leveraging the power of AI to facilitate comprehensive and nuanced discussions that may not be feasible at a large scale between human participants alone.

## Step 1: Gathering Personas

We will build a Web-based interface that can easily be consumed on mobile devices, such as smart phones and tablets, and thus can be used by individuals or set up on kiosks for maximum exposure. The Web interface will employ a chatbot that will be programmed to ask about the given Topic. It will use all or some of the following conversational techniques to elicit comprehensive responses from the user. Out-of-band monitoring techniques and hard limits will be used to ensure the user does not take an unnecessary amount of time or energy. Conversations should have a hard limit of, perhaps, 30 messages.

- Socratic Reasoning
- Reference Interview
- Active Listening
- Open-Ended Questions
- Probing Questions
- Hypothetical Scenarios
- Counterfactual Thinking
- Reflective Practice
- Motivational Interviewing
- Perspective-Taking
- Scaling Questions

## Step 2: Analyzing & Consolidating Personas

Personas will be standardized into archetypal or templated documents based upon the following frameworks, which will ensure consistent representation and scientifically reliable patterns:

- Kohlberg's Stages of Moral Development
- Maslow's Hierarchy of Needs
- Hofstede's Cultural Dimensions Theory
- Big Five Personality Traits
- Political Compass
- World Values Survey (WVS)
- Fowler's Stages of Faith
- Family Systems Theory
- Inglehart's Postmaterialist Values Theory
- Moral Foundations Theory (MFT)

The Persona will capture the following types of information, though the full template has yet to be developed:

- Demographic Information
  - Standard assay including gender, age, national origin, religion, ethnicity, income, education, disability status, career, family status, etc
- Values and Beliefs
  - Specific to Topic at hand. Natural language summary of chat logs, articulating any and all relevant beliefs and values pertaining to Topic. Can include personal anecdotes and reasoning for beliefs.
- AI Attitudes
  - Summarizes and consolidates partcipant's overall attitudes towards AI, including their trust level, hopes, fears, and so on. Not necessarily specific to Topic, could apply to AI more broadly.
- AI Expectations
  - Summarizes participants espoused expectations specific to Topic. What are their particular desires and needs and expected behaviors with respect to the given Topic?
- Knowledge and Understanding of AI
  - Assessment of partipant's grasp of AI concepts, including data, privacy, governance, operation. We must keep in mind that many humans will not understand how this technology works.
- Ideal AI Interaction
  - Natural language description of the participant's espoused "ideal interaction" with AI with respect to the given Topic.

### Clustering and Consolidating Personas

This step will use high dimensional embeddings (vectors) to cluster Personas. We can merge Personas that are overly similar, as well as identify gaps in the data.

1. **Semantic Analysis:** After generating the initial Persona documents, we will use NLP tools to conduct a semantic analysis. This process involves interpreting the meanings of words and text strings in the Personas, and determining how closely aligned they are. We can use various language models like word embeddings (Word2Vec, GloVe) or transformer-based models (BERT, RoBERTa) for semantic similarity measures. 
2. **Clustering:** Next, we'll perform a clustering analysis on the results of the semantic analysis. The goal here is to identify groups of Personas that share similar beliefs, values, and viewpoints. Clustering algorithms such as K-Means, Hierarchical Clustering, or DBSCAN could be useful in this context.
3. **Visualization:** To help understand the distribution and grouping of Personas, we can create visualizations of the clustering results. Tools such as t-SNE or UMAP can help to visualize high-dimensional data in two or three dimensions, allowing us to see which Personas are similar and how they group together.
4. **Identifying Gaps:** We'll use the visualizations and clustering results to identify any gaps in representation. If there are areas in the visualization that are sparse or empty, these could indicate underrepresented viewpoints that we need to seek out. 
5. **Merging Overlaps:** After identifying clusters of similar Personas, we can consolidate these into a single representative Persona for each cluster. This step simplifies the debate process by reducing the number of participating entities while maintaining the diversity of perspectives. 
6. **Validation:** Finally, we will validate the merged Personas by comparing them to the original Personas in their cluster. We can then adjust as necessary to ensure they still accurately represent the views of the individuals they're derived from.

### Imputing Missing Personas

This step will use Synthetic Data and Particle Filters to identify and impute missing Personas. More later. 

## Step 3: Consensus of Proposal

This process is loosely inspired by Larry Dressler's *Consensus Through Conversation* framework. Rather than using human participants, we will use the Personas in conjunction with advanced chatbot technology to automatically model the debate and discussion process. Rather than debate endlessly, however, we will have several gated steps that ensure focused effort. 

1. **Establish Decision Criteria:** This step defines the "must haves" of the final Proposal. In other words, this sets the goalposts for the Proposal. The Personas will work in conjunction with the automated system to rapidly workshop the Decision Criteria. We can also use this step to establish boundaries or "must not haves". 
2. **Draft the Proposal:** With the Topic, Criteria, and Personas ready to go, the automated process will then workshop the Proposal. This will be a largely generative step whereby brainstorming and refining (expand and contract) is the primary methodology. Brainstorming is a generative process that can increase the word count and complexity of the Proposal, whereas refinement can 
3. **Test for Consensus:** With the Proposal drafted, this is a discriminitive step where the Personas all get to weigh in with an Accept or Reject. An Accept is a straightforward vote for approval of the Proposal. A Reject is a vote for dissent, which must come with a natural language explanation of the Rejection. The automated system will then judge if the Reject is valid or not. An invalid Rejection is "tyranny of the majority" or "tyranny of the minority" whereby a Persona attempts to have undue influence over the whole process, or create conditions whereby a Proposal becomes lopsided. If a Rejection is valid, the Proposal is sent back to step 2, with the Rejection hadded as a Criteria. For instance, if a Reject is not made in good faith, and seems to be simply to hold up the process, it is not valid. Filibustering is not allowed.
4. **Reach Agreement:** Once the automated system has finished workshopping the Proposal, it is brought forth for human approval, which follows the same process. This marks the end of the machine-automated process.

There are numerous "rules of thumb" that all Proposals should adhere to. This is a non-exhaustive list of considerations:

- Clarity and specificity
- Complexity and caveats
- Exceptions and allowances
- Diversity and inclusivity
- Acknowledgement of limitations and gaps
- Definition of scope, scale, and boundaries

## Step 4: Human Acceptance

The Proposal is shared with the human participants, where they are permitted to ask questions and ensure that they understand the proposal. This phase is similar to the Consensus process. 

1. **Discussion of Proposal:** Human participants can discuss the Proposal with the chatbots and each other. This will give them time to clarify their understanding and either overcome any misunderstandings, or clarify their disagreements. 
2. **Vote on Proposal:** Human participants will be allowed to cast a vote for Accept or Reject. As with the Consensus process, any Reject must come with an explanation, which will be judged as valid or not. If the Reject is valid, the proposal will go back to the automated Consensus process. 
3. **Final Acceptance:** If the Proposal passes, it is ratified and the process comes to a conclusion. The final output is a Proposal, including all the Personas, chat logs, iterations, Criteria, and Rejections.
