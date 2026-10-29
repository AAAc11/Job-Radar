from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from airflow.models import Variable

default_args = {
    'owner': 'anna',
    'start_date': datetime(2024, 1, 1),
}

with DAG('job_radar_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    
    test_task = DockerOperator(
        task_id='run_etl',
        image='job_radar_etl',
        auto_remove='force',
        network_mode='bridge',
        docker_url='unix:///var/run/docker.sock',
        environment={'PYTHONUNBUFFERED': '1', 
                     'DB_USER': Variable.get("DB_USER"), 
                     'DB_PASSWORD': Variable.get("DB_PASSWORD"), 
                     'DB_NAME': Variable.get("DB_NAME"),
                     'AWS_ACCESS_KEY_ID': Variable.get("AWS_ACCESS_KEY_ID"), 
                     'AWS_SECRET_ACCESS_KEY': Variable.get("AWS_SECRET_ACCESS_KEY"),
                     'AWS_REGION': Variable.get("AWS_REGION")},
    )