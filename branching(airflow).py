import random
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow import DAG
default_args={
    'owner':'Krishna'
}
def get_name(ti):
    ti.xcom_push(key='name',value='Krishna')

def print_hi(ti):
    name=ti.xcom_pull(task_ids='get_data',key='name')
    print(f"HI,I am {name}")

def print_hello(ti):
    name=ti.xcom_pull(task_ids='get_data',key='name')
    print(f"Hello , I am {name}")

def branch_func():
    if random.random()<0.5:
        return 'print_hi'
    else:
        return 'print_hello'

with DAG(
    default_args=default_args,
    dag_id='dag_branching',
    start_date=datetime(2024,5,9),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    task_get_data=PythonOperator(
        task_id="get_data",
        python_callable=get_name,
        retries=3,
        retry_delay=timedelta(seconds=10)
    )

    branch_op=BranchPythonOperator(
        task_id='branch_task',
        python_callable=branch_func
    )

    task2=PythonOperator(
        task_id='print_hi',
        python_callable=print_hi
    )

    task3=PythonOperator(
        task_id="print_hello",
        python_callable=print_hello
    )

    task_get_data>>branch_op>>[task2,task3]
