# Sales ETL Pipeline

This project contains an ETL (Extract, Transform, Load) pipeline for processing sales data from JSON files and loading it into a PostgreSQL database.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Potential Database Schema](#database-schema)

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
├── README.md                              # Project documentation
├── requirements.txt                       # Required packages
```

## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Sales_ETL_Pipeline.git
    cd Sales_ETL_Pipeline
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database connection:**
    - Create a `.env` file in the root directory and add your PostgreSQL database configuration:
    ```
    PG_HOST=your_host
    PG_DATABASE=your_database
    PG_USER=your_username
    PG_PASSWORD=your_password
    ```

## Usage

Follow these steps to set up and run the ETL pipeline:

1. **Run SQL Scripts to Create Tables**

   Execute the SQL scripts located in the `sql_queries/` directory to create the necessary tables in your PostgreSQL database. Ensure you have connected to your database before running these scripts.

   ```bash
   psql -U username -d database_name -a -f sql_queries/create_tables.sql

   Replace username with your PostgreSQL username and database_name with the name of your database.
