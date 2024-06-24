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

conversionista_etl/
│
├── data/ # Directory containing JSON data files
├── db_design_w_queries/ # Directory containing db-design and queries to create tables for this design
├── sql_queries/ # Directory containing queries to create table for this project and query for populating dates-table
├── etl_sales_pipeline.py # Main ETL script
├── monitor_sales.py # Script to monitor records in sales tables
├── .env # Environment variables for database configuration
├── requirements.txt # Python dependencies
├── README.md # Project documentation