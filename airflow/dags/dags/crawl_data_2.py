from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 5, 19, 15),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'crawl_data_3',
    default_args=default_args,
    description='Crawl 5 times in ethereum blockchain 2',
    schedule_interval=timedelta(minutes=30),
)

def print_hello():
    print("hello")

run_script_tasks = [
    BashOperator(
        task_id=f'craw_data_{i}',
        bash_command='/Users/azoom/Desktop/project3/scripts/run_crawl.sh ',
        dag=dag,
    ) for i in range(1, 5)
]

group_trx = BashOperator(
    task_id='group_trx',
    bash_command='/Users/azoom/Desktop/project3/client/group_trx.sh ',
    dag=dag,
)

# Set dependencies
for i in range(3):
    run_script_tasks[i] >> run_script_tasks[i + 1]
run_script_tasks[3] >> group_trx