import pandas as pd
from database import get_connection


def load_data(file_path):

    data = pd.read_csv(file_path)

    print("Data loaded successfully!")

    return data


def store_data(data):

    engine = get_connection()

    data.to_sql(
        "sales_data",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data stored in PostgreSQL successfully!")


data = load_data("../data/sales_data.csv")

store_data(data)