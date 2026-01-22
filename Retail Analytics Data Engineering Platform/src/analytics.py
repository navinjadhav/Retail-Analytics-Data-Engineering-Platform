
import psycopg2

def build_daily_summary():
    conn = psycopg2.connect(
        host="localhost",
        database="retail_dw",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()

    cur.execute("DELETE FROM daily_sales_summary")

    cur.execute("""
        INSERT INTO daily_sales_summary
        SELECT order_date, COUNT(order_id), SUM(total_amount)
        FROM sales_clean
        GROUP BY order_date
    """)

    conn.commit()
    cur.close()
    conn.close()
