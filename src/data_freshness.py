import pandas as pd
from datetime import datetime


def check_data_freshness(data, date_column="date", max_days=2):

    data[date_column] = pd.to_datetime(data[date_column])

    latest_date = data[date_column].max()
    current_date = datetime.now()

    difference = (current_date - latest_date).days

    if difference <= max_days:
        status = "FRESH"
    else:
        status = "STALE"

    print("\n--- DATA FRESHNESS MONITORING ---")
    print(f"Latest Data Date: {latest_date.date()}")
    print(f"Current Date: {current_date.date()}")
    print(f"Data Age: {difference} days")
    print(f"Status: {status}")

    return {
        "latest_date": latest_date,
        "data_age": difference,
        "status": status
    }


data = pd.read_csv("../data/sales_data.csv")

result = check_data_freshness(data)