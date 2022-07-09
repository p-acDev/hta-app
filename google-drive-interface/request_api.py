import requests
import os
from dotenv import load_dotenv
# to get all env data from .env 
load_dotenv()

def get_all_data():
    # get back the data via requests
    
    if os.environ.get("ENV_TYPE") == 'dev':
        host = '192.168.1.21'
    elif os.environ.get("ENV_TYPE") == 'prod':
        host = 'backend' # i.e container
    
    r = requests.get(f'http://{host}:{os.environ.get("BACKEND_PORT")}/api/mesure')
    data = r.json()
    
    return data