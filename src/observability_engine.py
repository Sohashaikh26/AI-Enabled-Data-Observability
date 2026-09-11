import pandas as pd
from datetime import datetime
from sklearn.ensemble import IsolationForest


def run_observability_pipeline():

    print("\n===================================")
    print(" AI-ENABLED DATA OBSERVABILITY")
    print("===================================\n")


    # -------------------------------
    # LOAD DATA
    # -------------------------------

    data = pd.read_csv("../data/anomaly_sales_data.csv")

    print("Dataset loaded successfully!")
    print("Total Records:", len(data))


    # -------------------------------
    # DATA QUALITY
    # -------------------------------

    print("\n--- DATA QUALITY ---")

    missing_values = data.isnull().sum().sum()
    duplicate_records = data.duplicated().sum()

    print("Missing Values:", missing_values)
    print("Duplicate Records:", duplicate_records)


    # -------------------------------
    # DATA FRESHNESS
    # -------------------------------

    print("\n--- DATA FRESHNESS ---")

    data["date"] = pd.to_datetime(data["date"])

    latest_date = data["date"].max()

    current_date = datetime.now()

    data_age = (current_date - latest_date).days

    print("Latest Data:", latest_date.date())
    print("Data Age:", data_age, "days")


    if data_age <= 2:
        freshness_status = "FRESH"
    else:
        freshness_status = "STALE"

    print("Status:", freshness_status)


    # -------------------------------
    # SCHEMA INFORMATION
    # -------------------------------

    print("\n--- SCHEMA INFORMATION ---")

    print("Columns:")

    for column in data.columns:
        print("-", column)


    # -------------------------------
    # AI ANOMALY DETECTION
    # -------------------------------

    print("\n--- AI ANOMALY DETECTION ---")

    features = data[
        [
            "quantity",
            "price",
            "sales_amount"
        ]
    ]

    model = IsolationForest(
        contamination=0.03,
        random_state=42
    )

    data["anomaly"] = model.fit_predict(features)

    data["anomaly_status"] = data["anomaly"].map(
        {
            1: "NORMAL",
            -1: "ANOMALY"
        }
    )

    anomaly_count = (
        data["anomaly_status"] == "ANOMALY"
    ).sum()

    print("Anomalies Detected:", anomaly_count)


    # -------------------------------
    # DATA HEALTH SCORE
    # -------------------------------

    health_score = 100

    health_score -= missing_values * 2
    health_score -= duplicate_records * 5
    health_score -= anomaly_count * 3

    if freshness_status == "STALE":
        health_score -= 10


    # Prevent negative score
    health_score = max(0, health_score)

    print("\n--- DATA HEALTH SCORE ---")
    print("Health Score:", health_score, "%")


    # -------------------------------
    # SAVE RESULTS
    # -------------------------------

    results = {
        "total_records": len(data),
        "missing_values": int(missing_values),
        "duplicate_records": int(duplicate_records),
        "latest_date": str(latest_date.date()),
        "data_age_days": int(data_age),
        "freshness_status": freshness_status,
        "anomaly_count": int(anomaly_count),
        "health_score": int(health_score)
    }


    results_df = pd.DataFrame([results])

    results_df.to_csv(
        "../data/observability_results.csv",
        index=False
    )

    print("\nObservability results saved!")

    return results


# Run pipeline
if __name__ == "__main__":

    run_observability_pipeline()