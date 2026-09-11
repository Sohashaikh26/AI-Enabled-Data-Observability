import pandas as pd


def check_missing_values(data):
    missing = data.isnull().sum()

    print("\n--- MISSING VALUES ---")
    print(missing)

    return missing


def check_duplicates(data):
    duplicates = data.duplicated().sum()

    print("\n--- DUPLICATE RECORDS ---")
    print("Duplicate rows:", duplicates)

    return duplicates


def check_invalid_values(data):
    invalid_quantity = (data["quantity"] <= 0).sum()
    invalid_price = (data["price"] <= 0).sum()
    invalid_sales = (data["sales_amount"] <= 0).sum()

    print("\n--- INVALID VALUES ---")
    print("Invalid quantity:", invalid_quantity)
    print("Invalid price:", invalid_price)
    print("Invalid sales amount:", invalid_sales)

    return {
        "invalid_quantity": invalid_quantity,
        "invalid_price": invalid_price,
        "invalid_sales": invalid_sales
    }


def check_data_volume(data):
    volume = len(data)

    print("\n--- DATA VOLUME ---")
    print("Total records:", volume)

    return volume


# ADD STEP 3.6 FUNCTION HERE
def calculate_health_score(data):

    total_checks = 4
    passed_checks = 0

    # Check missing values
    if data.isnull().sum().sum() == 0:
        passed_checks += 1

    # Check duplicates
    if data.duplicated().sum() == 0:
        passed_checks += 1

    # Check invalid quantity
    if (data["quantity"] <= 0).sum() == 0:
        passed_checks += 1

    # Check invalid sales
    if (data["sales_amount"] <= 0).sum() == 0:
        passed_checks += 1

    score = (passed_checks / total_checks) * 100

    print("\n--- DATA HEALTH SCORE ---")
    print(f"Data Health: {score}%")

    return score


# LOAD DATA
data = pd.read_csv("../data/faulty_sales_data.csv")

print("DATA QUALITY MONITORING")
print("=======================")

check_missing_values(data)
check_duplicates(data)
check_invalid_values(data)
check_data_volume(data)

# ADD THIS AT THE END
calculate_health_score(data)