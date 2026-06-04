import streamlit as st # type: ignore
import google.generativeai as genai # type: ignore

# Gemini API Key from secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="MUDASIR Chatbot")

st.title("💬 MUDASIR Chatbot")
st.caption("Developer: MUDASIR")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        answer = response.text
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )