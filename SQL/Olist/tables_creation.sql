CREATE DATABASE IF NOT EXISTS olist;

USE olist;

DROP TABLE IF EXISTS geolocation, category, sellers, products, customers, orders, items, payments, reviews;

CREATE TABLE IF NOT EXISTS geolocation (
	geolocation_zip_code_prefix SMALLINT NOT NULL,
    geolocation_lat DECIMAL(10,2) NOT NULL,
    geolocation_lng DECIMAL(10,2) NOT NULL,
    geolocation_city VARCHAR(255) NOT NULL,
    geolocation_state VARCHAR(255) NOT NULL
);  

CREATE TABLE IF NOT EXISTS category (
	product_category_name VARCHAR (255),
	product_category_name_english VARCHAR (255),
    CONSTRAINT category_pk PRIMARY KEY (product_category_name)
);

CREATE TABLE IF NOT EXISTS sellers (
	seller_id	VARCHAR(255) NOT NULL,
    seller_zip_code_prefix	SMALLINT NOT NULL,
    seller_city	VARCHAR(255) NOT NULL,
    seller_state VARCHAR(255) NOT NULL,
    CONSTRAINT sellers_pk PRIMARY key (seller_id)
);

CREATE TABLE IF NOT EXISTS products (
	product_id VARCHAR (255) NOT NULL,
    product_category_name VARCHAR (255),
    product_name_lenght INT,
    product_description_lenght INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT,
    CONSTRAINT products_pk PRIMARY KEY (product_id) /*,
	CONSTRAINT products_fk FOREIGN KEY (product_category_name)
		REFERENCES category(product_category_name) */
);

CREATE TABLE IF NOT EXISTS customers (
	customer_id	VARCHAR (255) NOT NULL,
    customer_unique_id	INT NOT NULL,
    customer_zip_code_prefix SMALLINT NOT NULL,
    customer_city VARCHAR (255) NOT NULL,
    customer_state VARCHAR (255) NOT NULL,
    CONSTRAINT customers_pk PRIMARY KEY (customer_id)
);

CREATE TABLE IF NOT EXISTS orders (
	order_id VARCHAR (255) NOT NULL,
    customer_id	VARCHAR (255) NOT NULL,
    order_status VARCHAR (255) NOT NULL,
    order_purchase_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    order_approved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    order_delivered_customer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT orders_pk PRIMARY KEY (order_id),
    CONSTRAINT orders_fk FOREIGN KEY (customer_id)
		REFERENCES customers(customer_id)
);

CREATE TABLE IF NOT EXISTS items (
	order_id VARCHAR (255) NOT NULL,
    order_item_id SMALLINT NOT NULL,
    product_id VARCHAR (255) NOT NULL,
    seller_id VARCHAR (255) NOT NULL,
    shipping_limit_date	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    price DECIMAL(10,2) NOT NULL,
    freight_value DECIMAL(10,2) NOT NULL,
    CONSTRAINT items_pk PRIMARY KEY (order_id), 
    CONSTRAINT items_product_fk FOREIGN KEY (product_id)
		REFERENCES products(product_id),
	CONSTRAINT items_seller_fk FOREIGN KEY (seller_id)
		REFERENCES sellers(seller_id)
);

CREATE TABLE IF NOT EXISTS payments (
	order_id VARCHAR (255) NOT NULL,
    payment_sequential SMALLINT NOT NULL,
    payment_type VARCHAR (255) NOT NULL,
    payment_installments SMALLINT NOT NULL,
    payment_value DECIMAL(10,2) NOT NULL,
    CONSTRAINT payments_pk PRIMARY KEY (order_id)
);

CREATE TABLE IF NOT EXISTS reviews (
	review_id VARCHAR (255) NOT NULL,
    order_id VARCHAR (255) NOT NULL,
    review_score TINYINT NOT NULL,
    review_comment_title VARCHAR (255),
    review_comment_message	VARCHAR (255),
    review_creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    review_answer_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT reviews_pk PRIMARY KEY (review_id),
    CONSTRAINT reviews_fk FOREIGN KEY (order_id)
		REFERENCES orders(order_id)
);
