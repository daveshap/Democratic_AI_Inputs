import os
import openai
from time import time, sleep
import textwrap
import sys
import yaml


###     file operations


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()


def save_yaml(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, allow_unicode=True)


def open_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data


###     API functions


def chatbot(conversation, model="gpt-4", temperature=0):
    max_retry = 7
    retry = 0
    while True:
        try:
            response = openai.ChatCompletion.create(model=model, messages=conversation, temperature=temperature)
            text = response['choices'][0]['message']['content']
            return text, response['usage']['total_tokens']
        except Exception as oops:
            print(f'\n\nError communicating with OpenAI: "{oops}"')
            if 'maximum context length' in str(oops):
                a = conversation.pop(0)
                print('\n\n DEBUG: Trimming oldest message')
                continue
            retry += 1
            if retry >= max_retry:
                print(f"\n\nExiting due to excessive errors in API: {oops}")
                exit(1)
            print(f'\n\nRetrying in {2 ** (retry - 1) * 5} seconds...')
            sleep(2 ** (retry - 1) * 5)


###     CHAT FUNCTIONS


def get_user_input():
    # get user input
    text = input('\n\n\nUSER:\n')
    
    # check if scratchpad updated, continue
    if 'DONE' in text:
        print('\n\n\nThank you for participating in this survey! Your results have been saved. Program will exit in 5 seconds.')
        sleep(5)
        exit(0)
    if text == '':
        # empty submission, probably on accident
        None
    else:
        return text


def compose_conversation(ALL_MESSAGES, text, system_message):
    # continue with composing conversation and response
    ALL_MESSAGES.append({'role': 'user', 'content': text})
    conversation = list()
    conversation += ALL_MESSAGES
    conversation.append({'role': 'system', 'content': system_message})
    return conversation


def yaml_to_text(data):
    text = ""
    for entry in data:
        text += f"{entry['role'].upper()}: {entry['content']}\n\n\n"
    return text



if __name__ == '__main__':
    # instantiate chatbot, variables
    research_question = open_file('question.txt')
    openai.api_key = open_file('key_openai.txt').strip()
    system_message = open_file('system_consolidate.txt').replace('<<QUESTION>>', research_question)
    conversation = list()
    files = os.listdir('chat_logs')
    print('\n\n\n******    Previous Chat Logs    ******\n\n')
    for i in files:
        print(i)
    filename = input('\n\nPlease enter the chat log to summarize and evaluate: ')
    data = open_yaml(f"chat_logs/{filename}")
    formatted_text = yaml_to_text(data)
    ALL_MESSAGES = list()
    conversation = compose_conversation(ALL_MESSAGES, formatted_text, system_message)
    response, tokens = chatbot(conversation)
    print('\n\n\nEvaluation:\n\n')
    print(response)
    final_output = f'QUESTION: {research_question}\n\n{response}'
    save_file(f'evaluations/{filename}', final_output)