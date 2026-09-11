import pandas as pd
import random
from datetime import datetime, timedelta


data = []

start_date = datetime(2026, 8, 1)

# Generate normal data
for i in range(1, 101):

    quantity = random.randint(1, 5)
    price = random.choice([800, 1500, 2000, 30000, 50000])

    sales_amount = quantity * price

    date = start_date + timedelta(days=i % 30)

    data.append([
        i,
        date.strftime("%Y-%m-%d"),
        quantity,
        price,
        sales_amount
    ])


# Add unusual/anomalous records
data.append([101, "2026-09-01", 1, 950000, 950000])
data.append([102, "2026-09-02", 50, 50000, 2500000])
data.append([103, "2026-09-03", 100, 30000, 3000000])


# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "transaction_id",
        "date",
        "quantity",
        "price",
        "sales_amount"
    ]
)


# Save CSV
df.to_csv(
    "../data/anomaly_sales_data.csv",
    index=False
)

print("Dataset generated successfully!")
print("Total records:", len(df))