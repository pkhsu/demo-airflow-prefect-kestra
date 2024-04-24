from datetime import datetime
from airflow.models import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="airflow_date_dag",
    start_date=datetime(year=2023, month=7, day=10),
    catchup=False
) as dag:
    task_get_datetime = BashOperator(
      task_id="get_datetime",
      bash_command="date"
    )