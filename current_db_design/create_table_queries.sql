-- Create products table
CREATE TABLE IF NOT EXISTS products (
    item_id VARCHAR(255) PRIMARY KEY,
    item_name VARCHAR(255),
    item_brand VARCHAR(255),
    item_category VARCHAR(255),
    item_category2 VARCHAR(255),
    item_category3 VARCHAR(255),
    price_in_usd NUMERIC,
    price NUMERIC
);

-- Create Dates table
CREATE TABLE IF NOT EXISTS dates (
    date DATE PRIMARY KEY,
    day INTEGER,
    month INTEGER,
    year INTEGER,
    weekday TEXT
);

-- Create sales table
CREATE TABLE IF NOT EXISTS sales (
    ecommerce_transaction_id VARCHAR(255) PRIMARY KEY,
    event_date DATE,
    event_value_in_usd NUMERIC,
    user_pseudo_id VARCHAR(255),
    item_quantity NUMERIC,
    total_sales NUMERIC(10,2),
    total_sales_in_usd NUMERIC(10,2),
    FOREIGN KEY (event_date) REFERENCES dates(date)
);

-- Create sales_detail table
CREATE TABLE IF NOT EXISTS sales_detail (
    detail_id SERIAL PRIMARY KEY,
    ecommerce_transaction_id VARCHAR(255),
    item_id VARCHAR(255),
    item_quantity NUMERIC,
    item_price NUMERIC,
    FOREIGN KEY (item_id) REFERENCES products(item_id),
    FOREIGN KEY (ecommerce_transaction_id) REFERENCES sales(ecommerce_transaction_id)
);
