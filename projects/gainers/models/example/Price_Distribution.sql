{{ config(materialized='table') }}

SELECT
  symbol,
  MIN(price) AS min_price,
  AVG(price) AS avg_price,
  MEDIAN (price) AS median_price,
  MAX(price) AS max_price
FROM
  DATA_SCIENCE.UWA6XV_RAW.MARCH_10_2025
GROUP BY
  symbol
ORDER BY
  symbol
