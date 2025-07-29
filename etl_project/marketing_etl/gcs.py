import pandas as pd
from google.cloud import storage
from io import StringIO
from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_ads_filename() -> str:
    """Returns a filename like 'ads_20210728.csv' (4 years ago from today)."""
    run_date = datetime.today() - relativedelta(years=4)
    return f"ads_{run_date.strftime('%Y%m%d')}.csv"


def read_csv_from_gcs(bucket_name: str, file_name: str) -> pd.DataFrame:
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    data = blob.download_as_text()
    df = pd.read_csv(StringIO(data))

    return df

if __name__ == "__main__":
    bucket = "ads_data_dennis"
    filename = get_ads_filename()
    print(f"📄 Fetching file: {filename}")

    df = read_csv_from_gcs(bucket, filename)

    print(f"✅ DataFrame loaded with shape: {df.shape}")
    print(df.head())