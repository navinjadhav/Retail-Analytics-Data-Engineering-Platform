
# Retail Analytics Data Engineering Platform

## Overview
This project simulates a real-world **Retail Company Data Platform**.
It ingests data from APIs and CSVs, performs ETL, applies data quality checks,
and builds analytics-ready tables for business reporting.

## Business Use Case
Retail companies need daily reliable data for:
- Sales performance
- Customer behavior
- Product demand

This pipeline ensures **clean, consistent, and analytics-ready data**.

## Tech Stack
- Python
- Pandas
- PostgreSQL
- SQL
- Logging & Validation

## Architecture
Raw Data → Cleaned Data → Analytics Tables

## How to Run
1. Create PostgreSQL DB `retail_dw`
2. Run SQL from `sql/schema.sql`
3. Install requirements
4. Run `python src/pipeline.py`

## Output
- Clean sales data
- Aggregated analytics tables
- Logs for monitoring

## Author
Navin Jadhav | Aspiring Data Engineer
