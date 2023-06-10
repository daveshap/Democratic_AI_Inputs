# Investigative Survey Chatbot for Morality, Ethics, and Epistemology

This research project aims to create an investigative survey chatbot focused on morality, ethics, and epistemology. The
primary goal of the chatbot is to help users identify and articulate the axiomatic assumptions they hold. The chatbot
serves as a survey tool to help democratize inputs to a wide number of public and social issues. The extracted
information from users can later be consolidated and used for research purposes.

## Methodology and Reasoning

The chatbot script uses a combination of file operations, API functions, and chat functions to create an interactive
survey experience for users. It reads the research question, OpenAI API key, and system message from text files and uses
the OpenAI API to generate responses based on the conversation history.

The chatbot employs various epistemic techniques and follows behavioral guidelines outlined in the system message to
engage users in a meaningful conversation about morality, ethics, and epistemology. The chat logs are saved in YAML
format for later analysis and research purposes.

## Overview of the Chatbot Script

The chatbot script is written in Python and utilizes the OpenAI API to generate responses based on user input. The
script is divided into several sections, including file operations, API functions, and chat functions.

- **File Operations:** The file operations section contains functions for reading and writing files, such as opening and saving text files and
YAML files. These functions are used to store the chat logs and read the research question, OpenAI API key, and system
message.

- **API Functions:** The API functions section contains the `chatbot` function, which communicates with the OpenAI API to generate responses
based on the conversation history. It handles retries and error handling in case of communication issues with the API.

- **Chat Functions:** The chat functions section contains functions for handling user input, composing the conversation, and generating
chatbot responses. The main loop of the script is also present in this section, which continuously prompts the user for
input and generates chatbot responses until the user types "DONE" to exit the survey.

## System Message

The system message is a text file that provides the chatbot with guidelines and context for its behavior and purpose. It
includes the overall purpose, research question, epistemic techniques, and behavioral guidelines for the chatbot.

- **Overall Purpose:** The chatbot's overall purpose is to act as an investigative survey tool focused on morality, ethics, and epistemology.
It aims to help users identify and articulate the axiomatic assumptions they hold and extract information that can be
used for research purposes.

- **Research Question:** The research question is a dynamic part of the system message that can be updated to change the focus of the chatbot's
survey. It may include contextual information, such as background social, legal, political, or events.

- **Epistemic Techniques:** The system message outlines several epistemic techniques that the chatbot should employ during the conversation, such as
Socratic Reasoning, First Principles Thinking, Scientific Method, Falsificationism, Critical Thinking, and Reductionism
and Holism.

- **Behavioral Guidelines:** The system message also provides behavioral guidelines for the chatbot's conduct, such as avoiding sycophancy, educating
and informing users, unpacking and investigating user beliefs, spotlighting and articulating assumptions, naming
concepts and ideas, asking questions, and meeting users where they are in terms of language and tone.

# Automated Evaluation

This part of the project aims to create an evaluation bot that reads, evaluates, condenses, and articulates the chat
log between a user and another chatbot focused on morality, ethics, and epistemology. The primary goal of the evaluation
chatbot is to clearly state the user's beliefs, reasoning, and position with respect to the research question and
identify any particular schools of thought, moral paradigms, or other frameworks.

## Overview of the Evaluation Chatbot Script

The evaluation chatbot script is written in Python and utilizes the OpenAI API to generate responses based on the
conversation history. The script is divided into several sections, including file operations, API functions, and chat
functions.

- **File Operations:** The file operations section contains functions for reading and writing files, such as opening and saving text files and
YAML files. These functions are used to store the evaluation results and read the research question, OpenAI API key, and
system message.

- **API Functions:** The API functions section contains the `chatbot` function, which communicates with the OpenAI API to generate responses
based on the conversation history. It handles retries and error handling in case of communication issues with the API.

- **Chat Functions:** The chat functions section contains functions for handling user input, composing the conversation, and generating
chatbot responses. The main loop of the script is also present in this section, which prompts the user for the chat log
to summarize and evaluate, and generates the evaluation chatbot response.

## System Message

The system message is a text file that provides the evaluation chatbot with guidelines and context for its behavior and
purpose. It includes the overall purpose, research question, output format, level of detail, and next step for the
evaluation chatbot.

- **Overall Purpose:** The evaluation chatbot's overall purpose is to read, evaluate, condense, and articulate the chat log between a user and
another chatbot focused on morality, ethics, and epistemology. It aims to clearly state the user's beliefs, reasoning,
and position with respect to the research question and identify any particular schools of thought, moral paradigms, or
other frameworks.

- **Research Question:** The research question is a dynamic part of the system message that can be updated to change the focus of the evaluation
chatbot's analysis. It is the same research question that the other chatbot was tasked with during the survey.

- **Output Format:** The evaluation chatbot's response should have two sections: a summary of the user's beliefs, positions, needs, and
desires, and an evaluation that describes the philosophical, moral, ethical, or epistemic frameworks the user uses. The
response should be formatted in YAML.

- **Level of Detail:** The evaluation chatbot should err on the side of 'too much' detail, as this step is a first pass at data processing. It
is better to have an overly verbose evaluation rather than an overly simplified one, as the information can be reduced
later if necessary.

- **Next Step:** The user will submit a chat log in YAML format. The evaluation chatbot should read this YAML information, remove any
user information for privacy, and output the summary and evaluation according to the specified YAML format.

## Methodology and Reasoning

The evaluation bot script uses a combination of file operations, API functions, and chat functions to create an
interactive evaluation experience for users. It reads the research question, OpenAI API key, and system message from
text files and uses the OpenAI API to generate responses based on the conversation history.

The evaluation chatbot follows the guidelines outlined in the system message to analyze and evaluate the user's
conversation, identify any particular schools of thought, moral paradigms, or other frameworks, and generate a summary
and evaluation in YAML format. The evaluation results are saved in a separate file for later analysis and research
purposes.

# Description of this Repository

## Folders

- `chat_logs`: This folder contains a YAML list of chat logs conducted by the system. These files are timestamped and include the user's stated name. 

- `evaluations`: This folder contains YAML output from the evaluation chatbot. The filename is kept identical from the chat log for easy correlation later. 

## Files

- `chat.py`: This is the main chat script. Update `question.txt` prior to running chat. The chatbot uses the terminal console to conduct the survey interview. 

- `evaluate.py`: This is the evaluation bot. Its interaction is very simple, you only specify a chat log to process.

- `key_openai.txt`: This file is excluded by the `.gitignore` file. You will need to manually create this and place your own key. 

- `question.txt`: This is the main research question. This can be a simple question or it can contain some contextual information or a research objective. 

- `system.txt`: This is the default SYSTEM message for the main chatbot. It includes instructions for the survey chatbot to follow. It also contains a placeholder for the research question.

- `system_consolidate.txt`: This ist he default SYSTEM message for the evaluator bot. It likewise contains a placeholder for the research question as well as instructions as to how the evaluator is to conduct its evaluations.