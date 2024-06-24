import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
import os

load_dotenv()

db_config = {
    'host': os.getenv('PG_HOST'),
    'dbname': os.getenv('PG_DATABASE'),
    'user': os.getenv('PG_USER'),
    'password': os.getenv('PG_PASSWORD')
}

# Plot 1: Total Sales per Day (Bar Plot)
with psycopg2.connect(**db_config) as conn:
    with conn.cursor() as cur:
        query_total_sales_per_day = """
        SELECT
            event_date,
            SUM(total_sales) AS total_sales
        FROM sales
        GROUP BY event_date
        ORDER BY event_date
        """
        cur.execute(query_total_sales_per_day)
        rows = cur.fetchall()
        df_total_sales_per_day = pd.DataFrame(rows, columns=['event_date', 'total_sales'])

plt.figure(figsize=(12, 6))
sns.barplot(data=df_total_sales_per_day, x='event_date', y='total_sales')
plt.title('Total Sales per Day')
plt.xlabel('Date')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Item Category Distribution Based on Total Quantity Sold (Pie Chart)
with psycopg2.connect(**db_config) as conn:
    with conn.cursor() as cur:
        query_item_category_distribution = """
        SELECT
            C.item_category,
            SUM(B.item_quantity) AS total_quantity_sold
        FROM sales AS A
        JOIN sales_detail AS B ON A.ecommerce_transaction_id = B.ecommerce_transaction_id
        JOIN products AS C ON B.item_id = C.item_id
        GROUP BY C.item_category
        ORDER BY total_quantity_sold DESC
        LIMIT 10
        """
        cur.execute(query_item_category_distribution)
        rows = cur.fetchall()
        df_item_category_distribution = pd.DataFrame(rows, columns=['item_category', 'total_quantity_sold'])

plt.figure(figsize=(8, 8))
plt.pie(df_item_category_distribution['total_quantity_sold'], labels=None, autopct='%1.1f%%', startangle=140)
plt.title('Item Category Distribution Based on Total Quantity Sold.\n 10 most sold categories')
plt.axis('equal')

plt.legend(df_item_category_distribution['item_category'], loc='best', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()
