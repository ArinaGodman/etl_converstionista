import pandas as pd
import numpy as np
import json
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_config = {
        'host': os.getenv('PG_HOST'),
        'dbname': os.getenv('PG_DATABASE'),
        'user': os.getenv('PG_USER'),
        'password': os.getenv('PG_PASSWORD')
    }
    
directory = "data"

def extract_data_products(directory):
    data_frames = []
    
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                data = json.load(file)
                df = pd.json_normalize(data, sep='_')
                
                df_purchase = df.explode('items').reset_index(drop=True)
                
                if 'items' in df_purchase.columns:
                    items_df = pd.json_normalize(df_purchase['items'])
                    
                    selected_columns = [
                        'item_id',
                        'item_name',
                        'item_brand',
                        'item_category',
                        'item_category2',
                        'item_category3',
                        'price_in_usd',
                        'price'
                    ]
                    
                    items_df = items_df[selected_columns]
                    
                    data_frames.append(items_df)
    
    if not data_frames:
        raise Exception("No valid items data found in the specified directory.")
    
    combined_items_df = pd.concat(data_frames, ignore_index=True)
    return combined_items_df

def transform_data_products(products_data):
    patterns_to_replace = [r'(not set)', r'not_available', r'nan','()']
    
    for col in products_data.columns:
        if products_data[col].dtype == 'object':
            for pattern in patterns_to_replace:
                products_data[col] = products_data[col].str.replace(pattern,'', regex=True)
        else:
            products_data[col] = products_data[col].replace(patterns_to_replace, np.nan)
    
    products_data['item_name'] = products_data['item_name'].str.rstrip('_')
    
    unique_items_df = products_data.drop_duplicates(subset=['item_id', 'item_name']).copy()
    
    unique_items_df = unique_items_df.dropna(subset=['item_id'])

    convert_types = {
        'item_id': 'string', 
        'price_in_usd': 'float',  
        'price': 'float',  
        'item_name': 'string',  
        'item_brand': 'string',  
        'item_category': 'category', 
        'item_category2': 'category', 
        'item_category3': 'category'  
    }

    for col, dtype in convert_types.items():
        if col in unique_items_df.columns:
            unique_items_df[col] = unique_items_df[col].astype(dtype)
        
    return unique_items_df


def load_data_products(conn, data):

    insert_query = '''
    INSERT INTO products (
        item_id, 
        item_name,
        item_brand, 
        item_category, 
        item_category2, 
        item_category3, 
        price_in_usd,
        price
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''

    with conn.cursor() as cur:

        for idx, row in data.iterrows():
            item_id = row['item_id']

            cur.execute(insert_query, (
                row['item_id'],
                row['item_name'],
                row['item_brand'],
                row['item_category'],
                row['item_category2'],
                row['item_category3'],
                row['price_in_usd'],
                row['price']
            ))

        conn.commit()
        print("Data loaded successfully into 'products' table.")

        cur.execute('''
        SELECT COUNT(*) AS total_records
        FROM products;
        ''')

        total_records = cur.fetchone()[0]
        print(f"Total number of records in 'products' table: {total_records}")

def populating_products(directory, db_config):
    try:
        # Extract
        data = extract_data_products(directory)
        
        # Transform
        transformed_data = transform_data_products(data)
            
        # Load
        with psycopg2.connect(**db_config) as conn:
            load_data_products(conn, transformed_data)

    except Exception as e:
        print(f"An error occurred: {e}")

populating_products(directory, db_config)
