import json
from datetime import datetime
from airflow.models import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator

def save_users(ti) -> None:
    users = ti.xcom_pull(task_ids="get_users", key='return_value')
    if users:
        with open("/opt/airflow/logs/users.json", "w") as f:
            json.dump(users, f)
        print("Users data saved to file.")
    else:
        print("No users data found in XCom.")

with DAG(
    dag_id="airflow_user_api_dag",
    start_date=datetime(2023, 7, 10),
    schedule_interval="@hourly", # Add scheduled config @once, @hourly, @daily, @weekly, @monthly, @yearly or cron
    catchup=False
) as dag:
    task_get = SimpleHttpOperator(
        task_id="get_users",
        http_conn_id="users_api",
        endpoint="users/",
        method="GET",
        response_filter=lambda response: json.loads(response.text)
    )

    task_save = PythonOperator(
        task_id="save_users",
        python_callable=save_users
    )

    # 设置任务依赖
    task_get >> task_save
