# Power BI Dashboard

Connect Power BI Desktop to PostgreSQL at localhost:5432, database telecom.

Primary model: gold.customer_360.

Recommended pages:
1. Executive Overview
2. Customer 360
3. Telecom Operations
4. Streaming / Pipeline Monitoring

Suggested DAX:
```DAX
Total Customers = DISTINCTCOUNT(customer_360[customer_id])
Recharge Revenue = SUM(customer_360[total_recharge])
Total Data GB = SUM(customer_360[total_data_gb])
Total Complaints = SUM(customer_360[complaint_count])
Avg Resolution Days = AVERAGE(customer_360[avg_resolution_days])
```

A .pbix file is intentionally not committed because Power BI Desktop artifacts are binary. This document defines the data model and dashboard contract.
