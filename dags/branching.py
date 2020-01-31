import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator

import datetime

def _get_weekday(execution_date, **context):
    print(execution_date.strftime("%a"))

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

with DAG(dag_id='branching', default_args=args,) as dag:
    branching = BranchPythonOperator(task_id="branching", python_callable=_get_weekday, provide_context=True,)

# Weekdays_person_to_email={0: "Bob", 1: "Joe", 2: "Alice", 3: "Joe", 4: "Alice", 5: "Bob", 6: "Alice"}
# days = ["Mon", "Tue", "Wed","Thu", "Fri", "Sat", "Sun"]
# for day in days:
#     branching >> DummyOperator(task_id=day, dag=dag)
# join = DummyOperator(
#     task_id="join",
#     trigger_rule="none_failed")
