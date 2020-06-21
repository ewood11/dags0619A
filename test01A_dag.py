from airflow.operators import PythonOperator
from airflow.models import DAG
from datetime import datetime, timedelta
args = {'owner':'airflow', 'start_date' : datetime(2020, 6, 11), 'retries': 2, 'retry_delay': timedelta(minutes=1) }
dags = DAG('test01A_dag', default_args = args)
def print_context(val):
    print(val)
def print_text():
    print('Hello-World01A_CPC2_airflow_print_text_Fn_200611_1am')
t1 = PythonOperator(task_id='multitask1',op_kwargs={'val':{'CPC201A_dag_test01A_key1':12345_01A, 'CPC2_dag_test_key2':7890123}}, python_callable=print_context, dag = dags)
t2 = PythonOperator(task_id='multitask2', python_callable=print_text, dag=dags)
t2.set_upstream(t1)
