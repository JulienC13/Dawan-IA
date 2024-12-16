from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

if "input_value" not in st.session_state:
    st.session_state.input_value = ""

def submit():
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": st.session_state.input_value}]
        )
        st.write(completion.choices[0].message.content)
        st.session_state.input_value = ""
    except Exception as e:
        st.error(f"Erreur : {e}")

st.text_input("Entrez un message :", key="input_value", on_change=submit)
