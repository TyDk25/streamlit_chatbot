from openai import OpenAI

# Used to get API key from openai
client = OpenAI()


def chat_bot(prompt) -> str:
    """
    :param prompt: Question you want to ask.
    :return: response from bot.
    """

    # Connects to ChatGPT3.5 to answer prompts.
    messages = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
        ],

    )

    return messages.choices[0].message.content.strip()


if __name__ == '__main__':
    print('Enter quit, exit or bye to stop the chatbot.')
    while True:
        your_entry = input('You: ')
        # Used to break while loop and quit the program.
        if your_entry.lower() in ['quit', 'exit', 'bye']:
            break

        response = chat_bot(your_entry)

        # Prints response from chatbot.
        print(f'ChatBot: {response}')
