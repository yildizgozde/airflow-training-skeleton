

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
import datetime

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

with DAG(dag_id='airflow_cron_ex', default_args=args,schedule_interval='45 13 * * MON,WED,FRI',) as dag:
    t1 = DummyOperator(task_id="task1")
    t2 = DummyOperator(task_id="task2")
    t3 = DummyOperator(task_id="task3")
    t4 = DummyOperator(task_id="task4")
    t5 = DummyOperator(task_id="task5")

t1 >> t2 >> [t3, t4] >> t5




import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

import datetime

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}
def _print_exec_date(**context):
    print(context["execution_date"])

with DAG(dag_id='context_ex', default_args=args,) as dag:
    print_exec_date = PythonOperator(task_id="print_execution_date", python_callable=_print_exec_date, provide_context=True)
    wait_1 = BashOperator(task_id="wait_1", bash_command="sleep 1")
    wait_5 = BashOperator(task_id="wait_5", bash_command="sleep 5")
    wait_10 = BashOperator(task_id="wait_10", bash_command="sleep 10")
    the_end = DummyOperator(task_id="the_end")


print_exec_date >> [wait_1,wait_5,wait_10] >> the_end


