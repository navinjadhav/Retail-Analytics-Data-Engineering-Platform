
import psycopg2

def load_sales(df):
    conn = psycopg2.connect(
        host="localhost",
        database="retail_dw",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO sales_clean VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (order_id) DO NOTHING
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()
