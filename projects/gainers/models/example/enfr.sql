{{ config(materialized='table') }}

SELECT EN,FR
FROM DATA_SCIENCE.UWA6XV_RAW.NUMBERS
