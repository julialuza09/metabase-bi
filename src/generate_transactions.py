import os
import random
from datetime import datetime, timedelta

import pandas as pd


DATA_DIR = "data"
OUTPUT_FILE = os.path.join(DATA_DIR, "transactions.csv")

categories = ["books", "electronics", "food"]
statuses = ["paid", "pending", "cancelled"]

os.makedirs(DATA_DIR, exist_ok=True)

rows = []

start_date = datetime(2026, 5, 1)

for i in range(1000):
    event_time = start_date + timedelta(
        days=random.randint(0, 30),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    )

    row = {
        "event_time": event_time.strftime("%Y-%m-%d %H:%M:%S"),
        "user_id": f"u{random.randint(1, 100):03}",
        "category": random.choice(categories),
        "amount": round(random.uniform(10, 500), 2),
        "status": random.choice(statuses)
    }

    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv(OUTPUT_FILE, index=False)

print("Wygenerowano plik:", OUTPUT_FILE)
print("Liczba rekordów:", len(df))
print(df.head())