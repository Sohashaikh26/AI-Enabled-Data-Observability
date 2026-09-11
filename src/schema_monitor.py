import pandas as pd


# Check added and removed columns
def check_schema_changes(old_data, new_data):

    # Get column names
    old_columns = set(old_data.columns)
    new_columns = set(new_data.columns)

    # Find new columns
    added_columns = new_columns - old_columns

    # Find removed columns
    removed_columns = old_columns - new_columns

    print("\n--- SCHEMA MONITORING ---")

    # Check for changes
    if not added_columns and not removed_columns:
        print("Status: NO SCHEMA CHANGE")
    else:
        print("Status: SCHEMA CHANGE DETECTED")

        if added_columns:
            print("Added columns:", list(added_columns))

        if removed_columns:
            print("Removed columns:", list(removed_columns))

    return {
        "added_columns": list(added_columns),
        "removed_columns": list(removed_columns)
    }


# Check data type changes
def check_data_type_changes(old_data, new_data):

    common_columns = set(old_data.columns).intersection(
        set(new_data.columns)
    )

    changed_types = {}

    for column in common_columns:

        old_type = str(old_data[column].dtype)
        new_type = str(new_data[column].dtype)

        if old_type != new_type:
            changed_types[column] = {
                "old_type": old_type,
                "new_type": new_type
            }

    return changed_types


# Load original dataset
old_data = pd.read_csv("../data/sales_data.csv")

# Load new dataset
new_data = pd.read_csv(
    "../data/changed_schema_sales_data.csv"
)


# Run schema monitoring
check_schema_changes(old_data, new_data)


# Run data type monitoring
type_changes = check_data_type_changes(old_data, new_data)

print("\n--- DATA TYPE MONITORING ---")

if type_changes:

    print("Data type changes detected:")

    for column, types in type_changes.items():

        print(
            f"{column}: "
            f"{types['old_type']} → {types['new_type']}"
        )

else:
    print("Status: NO DATA TYPE CHANGES")