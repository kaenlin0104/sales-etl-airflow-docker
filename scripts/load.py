import pandas as pd
from db import get_engine

CLEAN_TABLE = "clean_supermarket_sales"
FACT_TABLE = "fact_sales"

def load_fact_sales():
    engine = get_engine()

    df = pd.read_sql(f"SELECT * FROM {CLEAN_TABLE}", engine)

    df.to_sql(
        FACT_TABLE,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"[LOAD] Loaded {len(df)} rows into {FACT_TABLE}")

if __name__ == "__main__":
    load_fact_sales()
