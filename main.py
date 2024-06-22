import os
import psycopg2
from etl_sales_pipeline import etl_pipeline_sales
from etl_products_pipeline import etl_pipeline_products
from etl_dates import insert_new_dates
from dotenv import load_dotenv

def main():

    load_dotenv()
    
    db_config = {
        'host': os.getenv('PG_HOST'),
        'dbname': os.getenv('PG_DATABASE'),
        'user': os.getenv('PG_USER'),
        'password': os.getenv('PG_PASSWORD')
    }
    
    directory = "data"
    
    etl_pipeline_sales(directory, db_config)
    etl_pipeline_products(directory, db_config)

if __name__ == "__main__":
    main()
