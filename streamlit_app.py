import streamlit as st # type: ignore
from openai import OpenAI # type: ignore

# Title
st.title("💬 Chatbot")

st.write(
    "This is a simple chatbot powered by OpenAI."
)

# API Key Input
openai_api_key = st.text_input(
    "OpenAI API Key",
    type="password"
)

if not openai_api_key:
    st.info("Please enter your OpenAI API key.", icon="🗝️")
    st.stop()

# OpenAI Client
client = OpenAI(api_key=openai_api_key)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
prompt = st.chat_input("Ask me anything...")

if prompt:
    # User Message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant Response
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        answer = response.choices[0].message.content
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )