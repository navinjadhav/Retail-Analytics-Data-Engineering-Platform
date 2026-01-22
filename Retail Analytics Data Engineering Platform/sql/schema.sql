
CREATE TABLE IF NOT EXISTS sales_clean (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id VARCHAR(10),
    product VARCHAR(50),
    category VARCHAR(30),
    quantity INT,
    price FLOAT,
    total_amount FLOAT
);

CREATE TABLE IF NOT EXISTS daily_sales_summary (
    order_date DATE,
    total_orders INT,
    total_revenue FLOAT
);
