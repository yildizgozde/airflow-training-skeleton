import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.python_operator import PythonOperator
import datetime

persons={"Mon": "Bob", "Tue": "Joe", "Wed": "Alice", "Thu": "Joe", "Fri": "Alice", "Sat": "Bob", "Sun": "Alice"}


def _print_weekday(execution_date, **context):
    print(execution_date.strftime("%a"))

def _get_weekday(execution_date, **context):
    person=persons.get(execution_date.strftime("%a"))
    return "email_{person}".format(person.lower())

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

with DAG(dag_id='branching', default_args=args,) as dag:
    print_days = PythonOperator(task_id="print_weekdays", python_callable=_print_weekday, provide_context=True,)
    branching = BranchPythonOperator(task_id="branching", python_callable=_get_weekday, provide_context=True,)
    final_task = DummyOperator(task_id="final_task",trigger_rule="none_failed")
    for person in persons.values():
        branching >> DummyOperator(task_id='email_'+ person.lower()) >> final_task

print_days >> branching
