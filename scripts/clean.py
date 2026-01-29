import pandas as pd
from db import get_engine

RAW_TABLE = "raw_supermarket_sales"
CLEAN_TABLE = "clean_supermarket_sales"

def clean_data():
    engine = get_engine()

    # Read raw data
    df = pd.read_sql(f"SELECT * FROM {RAW_TABLE}", engine)
    before_rows = len(df)

    # Drop duplicate invoices
    df = df.drop_duplicates(subset=["Invoice ID"])

    # Basic validation
    df = df[
        (df["Quantity"] > 0) &
        (df["Unit price"] > 0)
    ]

    # Recalculate total for consistency
    df["Total"] = df["Quantity"] * df["Unit price"]

    # Parse date
    df["Date"] = pd.to_datetime(df["Date"])

    after_rows = len(df)

    # Write clean data
    df.to_sql(
        CLEAN_TABLE,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"[CLEAN] Rows before: {before_rows}, "
        f"after cleaning: {after_rows}"
    )

if __name__ == "__main__":
    clean_data()
