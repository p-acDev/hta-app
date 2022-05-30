import streamlit as st
import requests

st.write("# Bienvenue sur votre suivi d'hypertension")


if st.button("Get mesures"):
    res = requests.get('http://127.0.0.1:8000/mesures')
    st.write(res.content)