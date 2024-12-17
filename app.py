import streamlit as st

st.set_page_config(page_title="IA Multi-Fonction", page_icon="🤖")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à :", ["Chat avec OpenAI", "Générer une image avec DALL-E"])

if page == "Chat avec OpenAI":
    st.title("Chat avec OpenAI")
    exec(open("main.py").read())

elif page == "Générer une image avec DALL-E":
    st.title("Générer une image avec DALL-E")
    exec(open("dalle.py").read())
