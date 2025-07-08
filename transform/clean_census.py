import pandas as pd

# Data paths
raw_path = "data/raw/census_by_zip.csv"
cleaned_path = "data/cleaned/cleaned_census_by_zip.csv"

# Load Dataframe aka table of data
df = pd.read_csv(raw_path)

# Preview Data (test as we go!!!) - can view columns as so, or whole dataset (whole data set will be very slow)
# print('📊', df.columns.tolist())

# Rename columns for clarity
df.columns = ['AreaName', 'Population', 'MedianIncome', 'ZipCode']

# Testing again!
# print('📊', df.columns.tolist())

df['ZipCode'] = df['ZipCode'].astype(str).str.zfill(5) # Keeps leading zeros
df['Population'] = pd.to_numeric(df['Population'], errors='coerce') # try to set as number, if not "coerce" to nan"
df["MedianIncome"] = pd.to_numeric(df["MedianIncome"], errors='coerce')# try to set as number, if not "coerce" to nan"

# Remove Rows that now contain NaN
df = df.dropna()

# Remove duplicates if you want
df = df.drop_duplicates(subset="ZipCode")

df.to_csv(cleaned_path, index=False)
print(f"✅ Cleaned Data saved to {cleaned_path}")