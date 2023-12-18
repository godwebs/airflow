from airflow import DAG
from airflow.decorators import task
import pendulum
import datetime

with DAG(
    dag_id="dags_python_show_templates",
    schedule="30 9 * * 1",
    start_date=pendulum.datetime(2023, 12, 3, tz="Asia/Seoul"),
    catchup=True
) as dag:
    
    @task(task_id="python_task")
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_templates()