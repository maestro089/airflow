from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator  import PythonOperator
from datetime import datetime
import time 

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "start_date": datetime(2022, 1, 1),
    "retries": 1,
}

dag = DAG(
    "test_dag",
    default_args=default_args,
    description="A simple DAG for Airflow",
    schedule_interval="1 * * * *",
    catchup=False,
)

def PrintMessage(ti):
    print("Hello, world!")
    ti.xcom_push(key="PrintMessage", value={"key": "value"})

def PrintMessage2(ti):
    value = ti.xcom_pull(key="PrintMessage")
    print(value)


task = PythonOperator(task_id="python_task", python_callable=PrintMessage, dag=dag)
task2 = PythonOperator(task_id="python_task2", python_callable=PrintMessage2, dag=dag)

task >> task2