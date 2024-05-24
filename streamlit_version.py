import streamlit as st
from openai import OpenAI

st.title("Tyrone's Assistant :)")

client = OpenAI()
# If there is no value in the session state, assign ChatGPT3.5 to it.
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Creates an empty list to store messages to store chat history.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Iterates over messages list to print content.
# Dependent on role.
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input('Enter a chat...')

if prompt is not None:
    # Appends content to list
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    # Assigns assistant role to ChatGPT API.
    with st.chat_message("assistant"):
        # Create chat stream to ChatGPT API, provides previous messages.
        stream = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        # Write response from the bot to Streamlit App.
        response = st.write_stream(stream)
        # Appends response from bot to list
    st.session_state.messages.append({"role": "assistant", "content": response})
