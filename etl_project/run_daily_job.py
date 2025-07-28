from marketing_etl.definitions import defs, get_filename

result = defs.get_job_def("daily_gcs_job").execute_in_process(
    run_config={
        "ops": {
            "gcs_to_dataframe": {
                "config": {
                    "file_name": get_filename()  # ← use dynamic filename
                }
            }
        }
    }
)
