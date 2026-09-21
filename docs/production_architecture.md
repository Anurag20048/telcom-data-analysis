# Production Architecture

Sources -> Kafka / Batch Ingestion -> Bronze -> Quality Gate -> Silver -> Spark/dbt -> Gold -> PostgreSQL/BI.

Streaming:
Kafka -> PySpark Structured Streaming -> event-time windows -> operational metrics.

Orchestration: Airflow.
CI/CD: GitHub Actions.
Monitoring: Prometheus + Grafana.
Infrastructure: Docker.

Production extensions would include cloud object storage, CDC, secrets management, alerting, partitioning and workload-scale testing.
