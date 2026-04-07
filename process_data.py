import pandas as pd

# Read files
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine
df = pd.concat([df0, df1, df2], ignore_index=True)

# Filter Pink Morsels
df = df[df["product"] == "pink morsel"].copy()

# Clean price (remove $)
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Convert quantity
df["quantity"] = pd.to_numeric(df["quantity"])

# Create Sales
df["Sales"] = df["price"] * df["quantity"]

# Keep needed columns
df = df[["Sales", "date", "region"]]

# Rename columns
df = df.rename(columns={"date": "Date", "region": "Region"})

# Save output
df.to_csv("formatted_sales_data.csv", index=False)

print("Done! File created.")
print(df.head())