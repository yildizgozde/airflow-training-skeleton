import airflow
from airflow.models import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.postgres_to_gcs_operator import PostgresToGoogleCloudStorageOperator



with DAG(**args) as dag:
    pgsl_to_gcs = PostgresToGoogleCloudStorageOperator(
        task_id="postgres_to_gcs",
        sql="SELECT * FROM land_registry_price_paid_uk ""LIMIT 10”",
        bucket="iamtestingmyairflow",
        filename="airflow_file",
        postgres_conn_id="PostgresToGoogleCloudStorageOperator"
    )


