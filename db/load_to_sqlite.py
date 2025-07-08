import sqlite3
import pandas as pd

# Paths
cleaned_path = "data/cleaned/cleaned_census_by_zip.csv"
db_path = "db/local_data.db"
schema_path = "db/schema.sql"

#  Read CSV so we can use it
df = pd.read_csv(cleaned_path)

# Connect to sqllite DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Load schema from .sql file
with open(schema_path, "r") as f:
    cursor.executescript(f.read())

#  Prepare DataFrame to match schema
df.rename(columns = {
    "ZipCode": "zip_code",
    "AreaName": "area_name",
    "Population": "population",
    "MedianIncome": "median_income"
}, inplace=True)

# Insert Into Table
df.to_sql("census_data", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print(f"✅ Data loaded into {db_path} using schema from {schema_path}")