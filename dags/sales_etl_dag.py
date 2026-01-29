from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "retries": 1,
}

with DAG(
    dag_id="sales_etl_pipeline",
    default_args=default_args,
    description="Automated Sales ETL Pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    extract_task = BashOperator(
        task_id="extract_raw_data",
        bash_command="python /opt/airflow/scripts/extract.py",
    )

    clean_task = BashOperator(
        task_id="clean_and_validate_data",
        bash_command="python /opt/airflow/scripts/clean.py",
    )

    load_task = BashOperator(
        task_id="load_fact_sales",
        bash_command="python /opt/airflow/scripts/load.py",
    )

    extract_task >> clean_task >> load_task
