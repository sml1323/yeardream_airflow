from airflow import DAG
import pendulum
from airflow.operators.empty import EmptyOperator
with Dag(
    dag_id="my_dag_name",
    start_date=pendulum.datetime(2024, 6, 17, tz="Asia/Seoul"),
    schedule="* * 25 * *",
    catchup=False
)as dag:
    task1 = EmptyOperator(
        task_id = "task1"

    )

task1 
