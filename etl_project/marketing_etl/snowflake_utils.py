
import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv
from snowflake.connector.pandas_tools import write_pandas

load_dotenv()

def upload_df_to_snowflake(df: pd.DataFrame, table_name: str):
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )

    try:
        success, nchunks, nrows, _ = write_pandas(
            conn,
            df,
            table_name.upper(),
            auto_create_table=True  # ✅ This is the fix!
        )
        print(f"✅ Uploaded {nrows} rows to {table_name}")
    except Exception as e:
        print("❌ Upload failed:", e)
    finally:
        conn.close()