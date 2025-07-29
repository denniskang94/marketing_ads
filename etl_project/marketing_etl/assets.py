# marketing_etl/assets.py

from dagster import asset, AssetExecutionContext, AssetIn
import pandas as pd

from marketing_etl.gcs import read_csv_from_gcs
from marketing_etl.snowflake_utils import upload_df_to_snowflake


@asset(config_schema={"file_name": str})
def gcs_to_dataframe(context: AssetExecutionContext) -> pd.DataFrame:
    bucket = "ads_data_dennis"
    file_name = context.op_config["file_name"]

    df = read_csv_from_gcs(bucket, file_name)
    context.log.info(f"✅ Loaded {file_name}, shape: {df.shape}")
    return df


@asset(ins={"df": AssetIn("gcs_to_dataframe")})
def upload_to_snowflake(df: pd.DataFrame) -> None:
    table_name = "GCS_UPLOAD"
    upload_df_to_snowflake(df, table_name)

