CREATE TABLE "products" (
  "item_id" varchar(255) PRIMARY KEY,
  "item_name" varchar(255),
  "item_brand" varchar(255),
  "item_category" varchar(255),
  "item_category2" varchar(255),
  "item_category3" varchar(255),
  "price_in_usd" numeric,
  "price" numeric
);

CREATE TABLE "dates" (
  "date" date PRIMARY KEY,
  "day" int,
  "month" int,
  "year" int,
  "weekday" text
);

CREATE TABLE "users" (
  "user_id" varchar(255) PRIMARY KEY,
  "user_name" varchar(255),
  "user_email" varchar(255),
  "user_country" varchar(255)
);

CREATE TABLE "sales" (
  "order_id" varchar(255) PRIMARY KEY,
  "ecommerce_transaction_id" varchar(255),
  "event_date" date,
  "event_value_in_usd" numeric,
  "user_id" varchar(255),
  "item_quantity" numeric,
  "total_sales" numeric(10,2),
  "total_sales_in_usd" numeric(10,2)
);

CREATE TABLE "transactions" (
  "ecommerce_transaction_id" varchar(255) PRIMARY KEY,
  "transaction_amount" numeric(10,2),
  "transaction_type" varchar(50),
  "transaction_status" varchar(50)
);

CREATE TABLE "sales_detail" (
  "detail_id" serial PRIMARY KEY,
  "order_id" varchar(255),
  "item_id" varchar(255),
  "item_quantity" numeric,
  "item_price" numeric
);

ALTER TABLE "sales" ADD FOREIGN KEY ("ecommerce_transaction_id") REFERENCES "transactions" ("ecommerce_transaction_id");

ALTER TABLE "sales" ADD FOREIGN KEY ("event_date") REFERENCES "dates" ("date");

ALTER TABLE "sales" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "sales_detail" ADD FOREIGN KEY ("order_id") REFERENCES "sales" ("order_id");

ALTER TABLE "sales_detail" ADD FOREIGN KEY ("item_id") REFERENCES "products" ("item_id");
