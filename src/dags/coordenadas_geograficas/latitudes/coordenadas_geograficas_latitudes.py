import os
import pendulum

from airflow.sdk import dag

from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow.sdk import Variable

@dag(
    schedule="*/5 * * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    catchup=False,
    tags=["pyspark", "minio", "iceberg"],
)
def coordenadas_geograficas_latitudes():

    PapermillOperator(
        task_id="run_coordenadas_geograficas_latitudes",
        input_nb=os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "notebooks", "workspace.ipynb"
        ),
        output_nb="/opt/airflow/logs/notebooks/out-coordenadas_geograficas_latitudes-{{ logical_date }}.ipynb",
        parameters={
            "minio_connection": Variable.get("minio_connection"),
            "nessie_connection": Variable.get("nessie_connection")
        },
    )


coordenadas_geograficas_latitudes()
