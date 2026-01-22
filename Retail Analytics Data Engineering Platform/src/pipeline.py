
import logging
from extract import extract
from transform import transform
from load import load_sales
from analytics import build_daily_summary

logging.basicConfig(level=logging.INFO)

def run():
    logging.info("Pipeline started")
    df = extract()
    df = transform(df)
    load_sales(df)
    build_daily_summary()
    logging.info("Pipeline finished successfully")

if __name__ == "__main__":
    run()
