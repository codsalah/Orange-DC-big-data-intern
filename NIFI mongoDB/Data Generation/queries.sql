-- Database creation

CREATE DATABASE IF NOT EXISTS sales_raw;

-- Activate the database before using it everytime opening the hive shell.

USE sales_raw;

-- Create the raw_sales_data to store the sales data

CREATE EXTERNAL TABLE IF NOT EXISTS raw_sales_data (
    transaction_id INT,
    product_id INT,
    quantity INT,
    price FLOAT,
    transaction_date STRING,
    customer_id INT,
    region STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/sales_raw_data'
TBLPROPERTIES ("skip.header.line.count"="1");

-- Create the products dimension table

CREATE EXTERNAL TABLE IF NOT EXISTS dim_product (
    product_id INT,
    product_name STRING,
    product_category STRING,
    price FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/products_data/'
TBLPROPERTIES ("skip.header.line.count"="1");

-- Create the fact table

CREATE EXTERNAL TABLE IF NOT EXISTS fact_sales (
    transaction_id INT,
    product_id INT,
    customer_id INT,
    sale_amount FLOAT,
    quantity INT,
    transaction_date DATE,
    region STRING
)
PARTITIONED BY (year INT, month INT)
STORED AS ORC;


-- Enables dynamic partitioning, which means partitions are determined dynamically based on the data being inserted
SET hive.exec.dynamic.partition.mode=nonstrict;

-- Load the data into the fact table using the raw_sales_data table and products dimension table

INSERT INTO TABLE fact_sales PARTITION(year, month)
SELECT 
    rs.transaction_id, 
    rs.product_id, 
    rs.customer_id, 
    rs.price * rs.quantity AS sale_amount, 
    rs.quantity, 
    TO_DATE(rs.transaction_date) AS transaction_date, 
    rs.region,
    YEAR(TO_DATE(rs.transaction_date)) AS year, 
    MONTH(TO_DATE(rs.transaction_date)) AS month
FROM raw_sales_data rs
JOIN dim_product dp
ON rs.product_id = dp.product_id;

-- Analytical Queries to test the solution

-- E1:

SELECT 
    year, 
    month, 
    SUM(sale_amount) AS total_sales
FROM fact_sales
GROUP BY year, month
ORDER BY year, month;

-- E2:

SELECT 
    dp.product_name, 
    SUM(fs.sale_amount) AS total_sales
FROM fact_sales fs
JOIN dim_product dp ON fs.product_id = dp.product_id
GROUP BY dp.product_name
ORDER BY total_sales DESC
LIMIT 5;

-- E3:

SELECT 
    region, 
    SUM(sale_amount) AS total_sales
FROM fact_sales
GROUP BY region
ORDER BY total_sales DESC;