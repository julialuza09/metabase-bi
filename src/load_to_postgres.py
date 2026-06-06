import pandas as pd
from sqlalchemy import create_engine


DATABASE_URL = "postgresql+psycopg2://bi:bi@127.0.0.1:5433/ntpd"
CSV_FILE = "data/transactions.csv"

engine = create_engine(DATABASE_URL)

df = pd.read_csv(CSV_FILE)

df["event_time"] = pd.to_datetime(df["event_time"])
df["amount"] = df["amount"].astype(float)

df.to_sql(
    "transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Załadowano dane do tabeli transactions")
print("Liczba rekordów:", len(df))
print(df.head())