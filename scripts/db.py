from sqlalchemy import create_engine
import os

def get_engine():
    user = os.getenv("POSTGRES_USER", "airflow")
    password = os.getenv("POSTGRES_PASSWORD", "airflow")
    host = os.getenv("POSTGRES_HOST", "postgres")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "airflow")

    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    )
    return engine
