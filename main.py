from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def new_message(content: str):
    with st.chat_message("user"):
        st.write(content)
    st.session_state.messages.append({"role": "user", "content": content})

    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages
            )
            assistant_reply = response.choices[0].message.content
            st.write(assistant_reply)
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
        except Exception as e:
            st.error(f"Erreur : {e}")

value = st.chat_input("Votre message ici")

if value:
    new_message(value)
