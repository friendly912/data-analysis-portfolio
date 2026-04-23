import pandas as pd

# Load data
data = pd.read_csv("messy_data.csv")

print("\nOriginal Data:")
print(data)

# Remove extra spaces
data["Age"] = data["Age"].astype(str).str.strip()

# Replace blank values with NaN
data = data.replace(" ", pd.NA)

# Fill missing Age with average
data["Age"] = pd.to_numeric(data["Age"], errors="coerce")
data["Age"].fillna(data["Age"].mean(), inplace=True)

# Fill missing City with "Unknown"
data["City"].fillna("Unknown", inplace=True)

# Fill missing Salary with 0
data["Salary"].fillna(0, inplace=True)

# Remove duplicate rows
data = data.drop_duplicates()

print("\nDuplicates removed (if any).")

print("\nCleaned Data:")
print(data)

# Save cleaned file
data.to_csv("cleaned_data.csv", index=False)

print("\nCleaned file saved as cleaned_data.csv")