import os
import pendulum

from airflow.sdk import dag

from airflow.providers.papermill.operators.papermill import PapermillOperator

@dag(
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    catchup=False,
    tags=["teste", "papermill"],
)
def teste_papermill():

    PapermillOperator(
        task_id="run_teste_papermill",
        input_nb=os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "notebooks", "workspace.ipynb"
        ),
        output_nb="/opt/airflow/logs/notebooks/out-teste_papermill-{{ logical_date }}.ipynb",
        parameters={
            "msgs": "Ran from Airflow at {{ logical_date }}!",
        },
    )


teste_papermill()
