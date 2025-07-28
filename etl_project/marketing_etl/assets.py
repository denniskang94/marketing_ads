from dagster import asset, AssetIn, Config
from google.cloud import storage
import pandas as pd
from io import StringIO

class GCSConfig(Config):
    file_name: str

@asset
def gcs_to_dataframe(config: GCSConfig) -> pd.DataFrame:
    bucket_name = "ads_data_dennis"  # fixed bucket

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(config.file_name)

    data = blob.download_as_text()
    df = pd.read_csv(StringIO(data))

    print(f"✅ Loaded {config.file_name}, shape: {df.shape}")
    return df