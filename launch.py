#!/usr/bin/env python3.7
import json
import pathlib
import posixpath
import airflow
import requests
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.http_operator import SimpleHttpOperator



args = {"owner": "Gozde", "start_date": airflow.utils.dates.days_ago(1)}
dag = DAG(dag_id="fetch_data_launchers", default_args=args, schedule_interval="0 0 * * *")

class HttpHook(BaseHook):
    def __init__(self, t1, t2):
        self.method = method
        url=f'https://launchlibrary.net/1.4/launch?startdate={self.t1}&enddate={self.t2}'
        req = requests.get(url).json()
        return req
        

class LaunchLibraryOperator(BaseOperator):
    @apply_defaults
    def __init__(self,t1,t2,*args,**kwargs):
        super(LaunchLibraryOperator, self).__init__(*args, **kwargs)
        result_path = "/Users/gyildiz/Desktop/3stweek/airflow-training-skeleton"  
    def execute(self, context):
        hook = HttpHook(self.t1, self,t2)
        with open(posixpath.join(result_path, "launches.json"), "w") as f:
            f.write(hook)


download_rocket_launches = LaunchLibraryOperator(
    task_id="download_rocket_launches", 
    conn_id="launchlibrary", 
    endpoint="launch", 
    params={"startdate": :{{t1}}}, "enddate": "{{t2}}"}, 
    result_bucket="mydata", 
    result_key="/data/rocket_launches/ds={{ds}}/launches.json",
    dag=dag}






