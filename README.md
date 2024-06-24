# Sales ETL Pipeline

This project contains an ETL (Extract, Transform, Load) pipeline for processing sales data from JSON files and loading it into a PostgreSQL database.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Monitoring](#monitoring)
- [Contributing](#contributing)
- [License](#license)

## Overview

The ETL pipeline extracts sales data from JSON files, transforms it into a structured format, and loads it into a PostgreSQL database. The pipeline processes data to create summary and detail views of sales transactions, making it easier to perform analysis and reporting.

## Project Structure

```plaintext
conversionista_etl/
├── data/                         # Directory containing JSON data files
├── db_design_w_queries/          # Directory containing db-design and queries to create tables for this design
│   ├── create_tables.sql         # SQL script to create the necessary tables accorging to design
│   └── db_diagram.png            # Database schema diagram
├── sql_queries/                  # Directory containing queries to create tables for this project and a query for    populating dates-table
│   ├── create_table_queries.sql  # SQL script to create the necessary tables for just this project
│   └── populating_dates_table_query.sql   # Query for populating dates-table in this project
├── etl_sales_pipeline.py         # Main ETL script
├── .env                          # Environment variables for database configuration
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation