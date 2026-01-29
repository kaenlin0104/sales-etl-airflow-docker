import pandas as pd
from db import get_engine

RAW_TABLE = "raw_supermarkepython scripts/load.pyt_sales"
CSV_PATH = "/opt/airflow/data/Supermarket_sales.csv"

def load_raw_data():
    engine = get_engine()

    df = pd.read_csv(CSV_PATH)

    df.to_sql(
        RAW_TABLE,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"[EXTRACT] Loaded {len(df)} rows into {RAW_TABLE}")

if __name__ == "__main__":
    load_raw_data()
