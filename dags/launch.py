#!/usr/bin/env python3.7
import json
import pathlib
import posixpath
import airflow
import requests
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.hooks.base_hook import BaseHook
from airflow.operators.bash_operator import BaseOperator
from airflow.utils.decorators import apply_defaults


args = {"owner": "Gozde", "start_date": airflow.utils.dates.days_ago(1)}
dag = DAG(dag_id="fetch_data_launchers", default_args=args, schedule_interval="0 0 * * *")

class HttpHook(BaseHook):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    def get_results(self):
        url=f'https://launchlibrary.net/1.4/launch?startdate={self.t1}&enddate={self.t2}'
        req = requests.get(url).json()
        print(req)
        return req
        

class LaunchLibraryOperator(BaseOperator):
    @apply_defaults
    def __init__(self,t1,t2,*args,**kwargs):
        super(LaunchLibraryOperator, self).__init__(*args, **kwargs)
        self.result_path = "/Users/gyildiz/Desktop/3stweek/airflow-training-skeleton"  
        self.t1 = t1
        self.t2 = t2

    def execute(self, context):
        hook = HttpHook(self.t1, self.t2)
        with open(posixpath.join(self.result_path, "launches.json"), "w") as f:
            f.write(hook.get_results())
             GoogleCloudStorageHook(google_cloud_storage_conn_id='google_conn_default').upload(bucket="launchbucket",object=f,filename="json_file")
        


download_rocket_launches = LaunchLibraryOperator(
    task_id="download_rocket_launches", 
    t1 = "2015-03-20",
    t2 = "2015-05-05",
    dag=dag)






