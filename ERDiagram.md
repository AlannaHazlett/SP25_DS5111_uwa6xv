# Lab-08: Database Design

## Introduction

This report will outline the structure of our database. The data in our database represents stock data of gainer stocks collected three times a day for 5 days. The tables formed will help answer analysis questions. 

## Use Cases

**Use Case 1: Price Distribution**

In order to understand the price of gainers we calculate key statistics about their prices, such as minimum, average, median, and max price while on the gainer list. The `Price_Distribution` table represents this data. 

**Use Case 2: Frequency of Stock on the Gainer List**

Often we want to know if a stock has been consistently on the gainer list or if has only made the list a few times. Is the stock consistently growing or is it having a single moment of significant growth? This can be answered with the `Unique_Stocks` table, as it will list every stock that has been on the gainer list with a frequency count of the number of times it made that list. 

## Methods

**Data Collection**

This data was collected on an Ubuntu system utilizing a crontab file. The crontab file made use of a makefile which collects the data using Chrome stable headless browser to collect the HTML from the Wall Street Journal and Yahoo websites. 

**Data Processing**
   
The HTML was then converted into a csv file and normalized so data from the Wall Street Journal and Yahoo would contain the same features by utilizing python and pandas. 

**Data Ingestion**

The normalized csvs were uploaded from the Ubuntu system via DBT-core and DBT-snowflake into the cloud database within Snowflake. 

## Summary

The Entity Relationship Diagram below helps us understand the structure of our database that is designed to gain better understanding of our stock data. Currently the data is only from the gainer lists from Wall Street Journal and Yahoo, but future analysis could include other stocks from the broader market. 

```mermaiderDiagram
erDiagram    
    Unique_Stocks{
        string symbol
        int frequency
    }
    Combined_Table||--o{Price_Distribution: "aggregates to"
    Combined_Table ||--|| Unique_Stocks: "aggregates to"
    Combined_Table{
        string symbol
        float price
        float price_change
        float price_percent_change
    }
    Price_Distribution {
    string symbol
    float min_price
    float avg_price
    float median_price
    float max_price
}
    Raw_Yahoo ||--||Combined_Table: "helps form"
    Raw_Yahoo {
        string symbol
        float price
        float price_change
        float price_percent_change
    }
    Raw_WSJ ||--||Combined_Table: "helps form"
    Raw_WSJ {
        string symbol
        float price
        float price_change
        float price_percent_change
    }
```
