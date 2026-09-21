# Interview Story

## 30-second answer
I built an end-to-end telecom data platform that ingests customer, recharge, usage and complaint data, validates it through a quality gate, transforms it into a Customer 360 Gold model, and publishes analytical data to PostgreSQL. I also designed Kafka and PySpark streaming paths, Airflow orchestration, dbt transformations, GitHub Actions CI/CD, and Prometheus/Grafana monitoring.

## Engineering decisions
- Kafka decouples event producers from consumers.
- Event IDs support idempotent processing.
- Event timestamps support event-time processing.
- Spark handles distributed workloads and streaming windows.
- Bronze/Silver/Gold separates raw, validated and business-ready data.
- Airflow provides dependency-aware scheduling.
- dbt provides tested warehouse transformations.
- CI prevents broken data pipelines from reaching main.
- Monitoring exposes pipeline health and processing metrics.

## Scaling answer
At billion-row scale, I would move raw data to object storage, use partitioned columnar formats, incremental/CDC ingestion, distributed Spark processing, appropriate Kafka partitioning and a cloud warehouse/lakehouse. I would also add secrets management, alerting and load testing.
