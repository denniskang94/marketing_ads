# Marketing ETL Pipeline

This project extracts marketing performance data from Google Cloud Storage (GCS), processes it with Pandas, and loads it into Snowflake for downstream analytics.

## 🧰 Tech Stack

- Python
- Dagster (orchestration)
- Google Cloud Storage (source)
- Snowflake (destination)
- DBT (optional)
- Poetry (dependency management)

## 🚀 Features

- Scheduled daily job using Dagster
- Dynamic file name resolution for GCS data
- Upload to Snowflake staging table
- Configurable with `.env` file
