{{ config(materialized='table') }}


SELECT
  "Campaign_Type",
  SUM(CAST(REPLACE(REPLACE("Acquisition_Cost", '$', ''), ',', '') AS FLOAT)) AS ad_spend
FROM {{ source('marketing_ads', 'gcs_upload') }}
WHERE "Channel_Used" = 'Google Ads'
GROUP BY "Campaign_Type"