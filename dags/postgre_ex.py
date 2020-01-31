from airflow.hooks.postgres_hook import PostgresHook

def _get_table():
    hook = PostgresHook(postgres_conn_id="PostgresToGoogleCloudStorageOperator")
    print(hook.get_records("SELECT * FROM land_registry_price_paid_uk ""LIMIT 10”"))

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

with DAG(dag_id='postgre', default_args=args,) as dag:
    print_days = PythonOperator(task_id="print_table_content", python_callable=_get_table,)
