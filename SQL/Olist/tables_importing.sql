-- To know your current_directory:
-- select @@datadir;

-- To know your uploads directory " place your files in this directory ":
-- SHOW VARIABLES LIKE "secure_file_priv"; 

-- Start uploading all files to tables:
-- change the path of each file after you copy the files into "secure_file_priv" location.
-- olist_geolocation_dataset to geolocation:
LOAD DATA INFILE 'C:\\olist_geolocation_dataset.csv' 
INTO TABLE geolocation
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- product_category_name_translation to category:
LOAD DATA INFILE 'C:\\product_category_name_translation.csv' 
INTO TABLE category
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- olist_sellers_dataset to sellers:
LOAD DATA INFILE 'C:\\olist_sellers_dataset.csv' 
INTO TABLE sellers
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- olist_products_dataset to products:
LOAD DATA INFILE 'C:\\olist_products_dataset.csv' 
INTO TABLE products
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(product_id, product_category_name, @product_name_lenght, @product_description_lenght, @product_photos_qty, @product_weight_g, @product_length_cm, @product_height_cm, @product_width_cm)
SET product_name_lenght = IF(@product_name_lenght = '', NULL, @product_name_lenght),
	product_description_lenght = IF(@product_description_lenght = '', NULL, @product_description_lenght),
	product_photos_qty = IF(@product_photos_qty = '', NULL, @product_photos_qty),
	product_weight_g = IF(@product_weight_g = '', NULL, @product_weight_g),
	product_length_cm = IF(@product_length_cm = '', NULL, @product_length_cm),
	product_height_cm = IF(@product_height_cm = '', NULL, @product_height_cm),
	product_width_cm = IF(@product_width_cm = '', NULL, @product_width_cm)
;

-- olist_customers_dataset to customers:
LOAD DATA INFILE 'C:\\olist_customers_dataset.csv' 
INTO TABLE customers
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- olist_orders_dataset to orders:
LOAD DATA INFILE 'C:\\olist_orders_dataset.csv' 
INTO TABLE orders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(order_id, customer_id ,order_status ,@order_purchase_timestamp ,@order_approved_at ,@order_delivered_carrier_date ,@order_delivered_customer_date ,@order_estimated_delivery_date)
SET order_purchase_timestamp = IF(@order_purchase_timestamp = '', NULL, @order_purchase_timestamp),
	order_approved_at = IF(@order_approved_at = '', NULL, @order_approved_at),
	order_delivered_carrier_date = IF(@order_delivered_carrier_date = '', NULL, @order_delivered_carrier_date),
	order_delivered_customer_date = IF(@order_delivered_customer_date = '', NULL, @order_delivered_customer_date),
	order_estimated_delivery_date = IF(@order_estimated_delivery_date = '', NULL, @order_estimated_delivery_date)
;

-- olist_order_items_dataset to items:
LOAD DATA INFILE 'C:\\olist_order_items_dataset.csv' 
INTO TABLE items
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- olist_order_payments_dataset to payments:
LOAD DATA INFILE 'C:\\olist_order_payments_dataset.csv' 
INTO TABLE payments
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- olist_order_reviews_dataset to reviews:
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\olist_order_reviews_dataset.csv' 
INTO TABLE reviews
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
