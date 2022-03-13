from fastapi import FastAPI

app  = FastAPI()

@app.get('/status')
def check_status():
    return 1


