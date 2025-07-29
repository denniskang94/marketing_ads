from dagster import (
    define_asset_job,
    Definitions,
    ScheduleDefinition,
)
from dagster._core.storage.fs_io_manager import fs_io_manager  # ✅ import this

from marketing_etl.assets import gcs_to_dataframe, upload_to_snowflake
from marketing_etl.gcs import get_ads_filename

gcs_to_snowflake_job = define_asset_job(
    name="gcs_to_snowflake_job",
    selection=[upload_to_snowflake],
)

daily_schedule = ScheduleDefinition(
    job=gcs_to_snowflake_job,
    cron_schedule="0 6 * * *",  # daily at 6 AM UTC
    run_config=lambda _: {
        "assets": {
            "gcs_to_dataframe": {
                "config": {
                    "file_name": get_ads_filename()
                }
            }
        }
    }
)

defs = Definitions(
    assets=[gcs_to_dataframe, upload_to_snowflake],
    jobs=[gcs_to_snowflake_job],
    schedules=[daily_schedule],
    resources={
        "io_manager": fs_io_manager  # ✅ use filesystem IO manager
    }
)
