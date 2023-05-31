import os
from datetime import datetime, timedelta

from docker.types import Mount

from airflow import DAG
from airflow.utils.dates import days_ago

from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator

with DAG(
        dag_id='my_dag', #name
        start_date=days_ago(0),
        schedule_interval="@daily",
        tags=["Test"]
    ) as dag:

    task0 = BashOperator(
        task_id='Excute',
        bash_command='echo "yoooo"',
        dag=dag,
    )

    # task1 = BashOperator(
    #     task_id='Extract-Native',
    #     bash_command='python3 /opt/airflow/dags/extract.py',
    #     dag=dag,
    # )
    #  
    # t2 = DockerOperator(
    #     task_id='docker_command_sleep',
    #     image='docker_image_task:latest',
    #     container_name='task___command_sleep',
    #     api_version='auto',
    #     auto_remove=True,
    #     command="echo test",
    #     docker_url="unix://var/run/docker.sock",
    #     network_mode="bridge"
    # )

    t1 = DockerOperator(
        task_id='docker_extract',
        image='docker_extract',
        api_version='1.37',
        auto_remove=True,
        command="/bin/sleep 30",
        docker_url="tcp://docker-socket-proxy:2375",
        network_mode="bridge"
    )

    t2 = DockerOperator(
        task_id='docker_transform',
        image='docker_transform',
        api_version='1.37',
        auto_remove=True,
        command="/bin/sleep 30",
        docker_url="tcp://docker-socket-proxy:2375",
        network_mode="bridge"
    )

    t3 = DockerOperator(
        task_id='docker_load',
        image='docker_load',
        api_version='1.37',
        auto_remove=True,
        command="/bin/sleep 30",
        docker_url="tcp://docker-socket-proxy:2375",
        network_mode="bridge"
    )

    # task1_2 = DockerOperator(
    #     task_id='Extract-Docker',
    #     image='my_etl:test',
    #     container_name='etl',
    #     api_version='auto',
    #     # network_mode="bridge",
    #     mount_tmp_dir = False,
    #     mounts=[Mount(source=os.getcwd() + "../data/source",target="/opt/airflow/data/source",type="bind")],
    #     docker_url='unix://docker-proxy:2375',
    #     command='python extract.py',
    #     auto_remove=True,
    # )

    # task2 = BashOperator(
    #     task_id='Transform',
    #     bash_command='python /opt/airflow/dags/transform.py',
    #     dag=dag,
    # )
    # task3 = BashOperator(
    #     task_id='Load',
    #     bash_command='python /opt/airflow/dags/load.py',
    #     dag=dag
    # )

    # task0 >> t2 >> task2 >> task3
    task0 >> t1 >> t2 >> t3
    # task0 >> task1_2 >> task2