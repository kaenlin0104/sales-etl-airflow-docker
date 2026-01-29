from db import get_engine
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def run_quality_check():
    engine = get_engine()

    raw_count = pd.read_sql(
        "SELECT COUNT(*) FROM raw_supermarket_sales",
        engine
    ).iloc[0, 0]

    clean_count = pd.read_sql(
        "SELECT COUNT(*) FROM clean_supermarket_sales",
        engine
    ).iloc[0, 0]

    logging.info(f"Raw layer row count: {raw_count}")
    logging.info(f"Clean layer row count: {clean_count}")

    # Threshold check (80%)
    if clean_count < raw_count * 0.8:
        raise ValueError(
            "Data quality check failed: too many rows removed during cleaning"
        )

    logging.info("Data quality check passed successfully")

if __name__ == "__main__":
    run_quality_check()
