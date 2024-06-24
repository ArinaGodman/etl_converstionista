# Sales ETL Pipeline

This project contains an ETL (Extract, Transform, Load) pipeline for processing sales data from JSON files and loading it into a PostgreSQL database.

## Overview

The ETL pipeline extracts sales data from JSON files, transforms it into a structured format, and loads it into a PostgreSQL database. This process creates both summary and detailed views of sales, facilitating analysis and reporting. The ETL pipeline is automated with the help of Windows Task Scheduler.

In addition to the sales and sales_detail tables, products and dates tables were created and populated from the JSON files.

In the db_design_w_queries directory, you can find a .png file illustrating the potential database structure with more time and information. Queries for creating these tables are also provided in the same directory.


## Project Structure

```plaintext
conversionista_etl/
├── data/                                  # Directory containing JSON data files
├── db_design_w_queries/                   # Directory containing db-design and queries to create tables for this design
│   ├── create_tables.sql                  # SQL script to create the necessary tables accorging to design
│   └── db_diagram.png                     # Database schema diagram
├── sql_queries/                           # Directory containing queries to create tables for this project and a query for    populating dates-table
│   ├── create_table_queries.sql           # SQL script to create the necessary tables for just this project
│   └── populating_dates_table_query.sql   # Query for populating dates-table in this project
├── etl_sales_pipeline.py                  # Main ETL script
├── populating_products.py                 # Script for populating products-table from json-files
├── visual.py                              # Script for creating a few visuals of sales-data
├── .env                                   # Environment variables for database configuration
├── requirements.txt                       # Python dependencies
├── README.md                              # Project documentation