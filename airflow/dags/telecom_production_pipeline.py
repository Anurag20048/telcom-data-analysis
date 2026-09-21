from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
with DAG("telecom_production_pipeline",start_date=datetime(2026,1,1),schedule="@daily",catchup=False,tags=["telecom","etl","quality"]) as dag:
    ingest=BashOperator(task_id="ingest",bash_command="cd /opt/telecom && python scripts/generate_data.py")
    quality=BashOperator(task_id="data_quality_gate",bash_command="cd /opt/telecom && python -m src.quality.validate")
    transform=BashOperator(task_id="build_customer_360",bash_command="cd /opt/telecom && python -m src.transform.build_gold")
    load=BashOperator(task_id="load_postgres",bash_command="cd /opt/telecom && python -m src.ingestion.load_postgres")
    ingest >> quality >> transform >> load
