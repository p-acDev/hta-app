from airflow import DAG
from airflow.models import Variable
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
import datetime
import time
import os
import requests
import pandas as pd
from dateutil import parser
import os
import matplotlib.pyplot as plt

def get_all_data(task_instance):
    # get back the data via requests
    
    if os.environ.get("ENV_TYPE") == 'dev':
        host = os.environ.get("RASP_HOST")
    elif os.environ.get("ENV_TYPE") == 'prod':
        host = 'backend' # i.e container
    
    r = requests.get(f'http://{host}:{os.environ.get("BACKEND_PORT")}/api/mesure')
    data = r.json()
    
    task_instance.xcom_push(
        key="mesures_data",
        value=data
    )
    
    return data

def create_df(task_instance):
    
    data = task_instance.xcom_pull(key='mesures_data', task_ids=['get_data'])
    
    # transform into dataframe
    df = pd.DataFrame(data[0]) # [0] because certainly xcom return a list of values
    df['datetime'] = df['date_mesure'].apply(lambda elem:parser.parse(elem))
    df = df.drop(columns='date_mesure')

    # store file
    df.to_csv('/opt/airflow/data/data.csv')
        
    return None

def create_plot():
    
    df = pd.read_csv('/opt/airflow/data/data.csv')
    
    # create box plots
    plt.subplot(1, 2, 1)
    plt.boxplot(x='systolic',
            data=df,
            showmeans=True,
            )
    plt.xlabel('Systolique')
    plt.ylabel('mmHg')
    
    plt.subplot(1, 2, 2)
    plt.boxplot(x='diastolic',
            data=df,
            showmeans=True
            )
    plt.xlabel('Diastolique')
    plt.ylabel('mmHg')
    
    plt.suptitle(datetime.datetime.now())
    
    plt.tight_layout()
    
    plt.savefig('/opt/airflow/data/boxplot.png')
    
    return None

def create_report():
    
    df = pd.read_csv('/opt/airflow/data/data.csv')
    
    df_report = df[['systolic', 'diastolic']]
    
    df_report.to_csv('/opt/airflow/data/report.txt', sep=" ", index=False)
    
    with open("/opt/airflow/data/report.txt", 'a') as f:
        f.write(f"\n\nDate fichier: {datetime.datetime.now()}")
    
    return None


my_dag = DAG(
    dag_id='data_pipeline_hta_api',
    description="DAG pour l'extraction des données de HTA ",
    tags=['hta-api'],
    #schedule_interval=datetime.timedelta(seconds=10),
    default_args={
        'owner': 'airflow',
        'start_date': days_ago(2),
    },
    catchup=False
)

task_extract = PythonOperator(
    task_id='get_data',
    dag=my_dag,
    python_callable=get_all_data
)

task_transform = PythonOperator(
    task_id='transform_data',
    dag=my_dag,
    python_callable=create_df
)

task_create_plot = PythonOperator(
    task_id='create_plot',
    dag=my_dag,
    python_callable=create_plot
)

task_create_report = PythonOperator(
    task_id='create_report',
    dag=my_dag,
    python_callable=create_report
)

task_extract >> task_transform >> [task_create_plot, task_create_report]