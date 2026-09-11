import pandas as pd
from sklearn.ensemble import IsolationForest


# Load dataset
data = pd.read_csv("../data/anomaly_sales_data.csv")


# Select numerical features
features = data[
    [
        "quantity",
        "price",
        "sales_amount"
    ]
]


# Create AI model
model = IsolationForest(
    contamination=0.03,
    random_state=42
)


# Train and predict
data["anomaly"] = model.fit_predict(features)


# Convert result into readable labels
data["anomaly_status"] = data["anomaly"].map(
    {
        1: "NORMAL",
        -1: "ANOMALY"
    }
)


# Display results
print("\n--- AI ANOMALY DETECTION ---\n")

print(
    data[
        [
            "transaction_id",
            "quantity",
            "price",
            "sales_amount",
            "anomaly_status"
        ]
    ].tail(10)
)


# Count anomalies
anomaly_count = (
    data["anomaly_status"] == "ANOMALY"
).sum()


print("\nTotal Anomalies Detected:", anomaly_count)

# Save results
data.to_csv(
    "../data/anomaly_detection_results.csv",
    index=False
)

print("\nResults saved successfully!")