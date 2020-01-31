from airflow.hooks.postgres_hook import PostgresHook


hook = PostgresHook(postgres_conn_id="PostgresToGoogleCloudStorageOperator")
print(hook.get_records("SELECT * FROM land_registry_price_paid_uk ""LIMIT 10”"))
