{{ config(materialized='table') }}

SELECT 
    COUNT(DISTINCT symbol) AS unique_symbol_count
FROM 
    DATA_SCIENCE.UWA6XV_RAW.MARCH_10_2025
