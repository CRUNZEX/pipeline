from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator

default_args = {
    'owner': 'airflow',
    'description': 'Use of the DockerOperator',
    'depend_on_past': False,
    'start_date': datetime(2018, 1, 3),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('dag-testing', default_args=default_args, schedule_interval="5 * * * *", catchup=False) as dag:
    t1 = BashOperator(
        task_id='print_current_date',
        bash_command='date'
    )

    t2 = DockerOperator(
        task_id='docker_command',
        image='centos:latest',
        api_version='1.37',
        auto_remove=True,
        command="/bin/sleep 30",
        docker_url="tcp://docker-socket-proxy:2375",
        network_mode="bridge"
    )

    t_ty = DockerOperator(
        task_id='docker-shkool-run',
        image='docker_test',
        api_version='1.37',
        auto_remove=True,
        command="/bin/sleep 30",
        docker_url="tcp://docker-socket-proxy:2375",
        network_mode="bridge"
    )

    t3 = BashOperator(
        task_id='print_hello',
        bash_command='echo "hello world"'
    )

    # pipeline
    t1 >> t2 >> t_ty >> t3
