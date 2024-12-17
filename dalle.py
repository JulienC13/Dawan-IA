from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

prompt = st.text_input("Entrez une description pour generer une image avec DALL-E :")

if st.button("Generer l'image"):
    if prompt:
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            image_url = response.data[0].url
            
            st.image(image_url, caption="Image generee par DALL-E", use_container_width=True)
            

        except Exception as e:
            st.error(f"Erreur : {e}")
    else:
        st.warning("Veuillez entrer une description pour generer une image.")
