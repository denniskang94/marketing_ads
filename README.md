📊 Marketing ETL Pipeline
This project extracts daily marketing performance data from Google Cloud Storage (GCS), processes it using Pandas, and loads it into Snowflake for downstream analytics.

🧰 Tech Stack
Python
Dagster – Workflow orchestration
Google Cloud Storage (GCS) – Raw data source
Snowflake – Data warehouse destination
DBT (optional) – Data transformation layer
Poetry – Dependency management

🚀 Key Features
- Automated daily ETL using Dagster schedules
- Dynamic file name resolution for fetching GCS files
- Data upload to a Snowflake staging table
- .env-based configuration for environment flexibility

✅ Wha's been done
- Downloaded sample marketing dataset from Kaggle manually.
- Split the dataset into daily files (e.g., 20240501.csv, 20240502.csv) using a Python script and uploaded them to a GCS bucket.
- Developed Dagster assets that:
- Dynamically fetch the correct file from GCS
- Process the CSV with Pandas
- Load the transformed data into a Snowflake staging table.

🛠️ Work in Progress
- Treat uploaded file in Snowflake as the raw data source and use DBT models to build Medallion architecture (Bronze → Silver → Gold)
- Visualize finding using Apache Superset and show insights.
