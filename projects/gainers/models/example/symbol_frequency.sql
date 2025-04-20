{{ config(materialized='table') }}

SELECT
  symbol,
  COUNT(*) AS occurrence_count
FROM
  DATA_SCIENCE.UWA6XV_RAW.MARCH_10_2025
GROUP BY
  symbol
ORDER BY
  occurrence_count DESC
