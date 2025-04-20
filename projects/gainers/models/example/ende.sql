{{ config(materialized='table') }}

SELECT EN,DE 
FROM DATA_SCIENCE.UWA6XV_RAW.NUMBERS
