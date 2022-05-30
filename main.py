from fastapi import FastAPI
import streamlit as st

app  = FastAPI()

@app.get("/")
def read_all_measures():
    return None