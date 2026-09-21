import time
from prometheus_client import Counter, Gauge, start_http_server
PIPELINE_RUNS=Counter("telecom_pipeline_runs_total","Pipeline runs")
RECORDS_PROCESSED=Counter("telecom_records_processed_total","Records processed")
RECORDS_REJECTED=Counter("telecom_records_rejected_total","Records rejected")
PIPELINE_DURATION=Gauge("telecom_pipeline_duration_seconds","Last pipeline duration")
PIPELINE_UP=Gauge("telecom_pipeline_up","Pipeline health")
if __name__=="__main__":
    start_http_server(8000); PIPELINE_UP.set(1)
    while True:
        PIPELINE_RUNS.inc(); RECORDS_PROCESSED.inc(1000); PIPELINE_DURATION.set(1.2); time.sleep(15)
