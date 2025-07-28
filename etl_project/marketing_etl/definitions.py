
from dateutil.relativedelta import relativedelta


from dagster import Definitions, define_asset_job, ScheduleDefinition
from marketing_etl.assets import gcs_to_dataframe
from datetime import datetime, timedelta

def get_filename():
    run_date = datetime.today() - relativedelta(years=4)  
    return f"ads_{run_date.strftime('%Y%m%d')}.csv"


daily_job = define_asset_job("daily_gcs_job", selection=[gcs_to_dataframe])

daily_schedule = ScheduleDefinition(
    job=daily_job,
    cron_schedule="0 6 * * *",  # every day at 6 AM
    run_config_fn=lambda _: {"ops": {"gcs_to_dataframe": {"config": {"file_name": get_filename()}}}},
)

defs = Definitions(
    assets=[gcs_to_dataframe],
    schedules=[daily_schedule],
    jobs=[daily_job],
)


