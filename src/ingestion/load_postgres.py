import os
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text
from src.transform.build_gold import build
RAW=Path("data/raw")

def engine():
    return create_engine(f"postgresql+psycopg2://{os.getenv('POSTGRES_USER','telecom')}:{os.getenv('POSTGRES_PASSWORD','telecom')}@{os.getenv('POSTGRES_HOST','localhost')}:{os.getenv('POSTGRES_PORT','5432')}/{os.getenv('POSTGRES_DB','telecom')}")

def load():
    build(); e=engine()
    mapping={"customers.csv":"customers","recharge.csv":"recharge","usage.csv":"usage","complaints.csv":"complaints"}
    with e.begin() as conn:
        for file,table in mapping.items(): pd.read_csv(RAW/file).to_sql(table,conn,schema="bronze",if_exists="replace",index=False,method="multi")
        pd.read_csv("data/processed/customer_360.csv").to_sql("customer_360",conn,schema="gold",if_exists="replace",index=False,method="multi")
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_gold_state ON gold.customer_360(state)"))
    print("POSTGRES LOAD: PASS")
if __name__=="__main__": load()
