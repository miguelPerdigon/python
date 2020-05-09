from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from tasks import task1
from utils import environments

args = {
    'owner': 'Owner Name',
    'depends_on_past': False,
    'start_date': datetime(2018, 9, 1),
    'email': ['miguelperdigon91@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    'Dag',
    default_args=args,
    catchup=False,
    schedule_interval=environments.set_schedule_interval(None) # you can put * * * *  cron value
) as dag:
    task = PythonOperator(
        task_id='task_name',
        provide_context=True,
        python_callable=task1.load,
        op_kwargs={'variable_1': 1}
    )
