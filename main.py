from fastapi import FastAPI
from database import get_data

app = FastAPI()

@app.get('/mesures')
def get_mesures():
    data = get_data()
    return data
