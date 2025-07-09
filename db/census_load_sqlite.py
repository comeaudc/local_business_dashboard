import sqlite3
import pandas as pd
import os
import sys

# Paths
cleaned_path = "data/cleaned/cleaned_census_by_zip.csv"
db_path = "db/local_data.db"
schema_path = "db/schemas/census_schema.sql"


try:
    #  if incorrect filepath or missing file throw error
    if not os.path.exists(cleaned_path):
        raise FileNotFoundError(f"Missing CSV file: {cleaned_path}")
    
    #  Read CSV so we can use it
    df = pd.read_csv(cleaned_path)

    #  Prepare DataFrame to match schema
    df.rename(columns = {
        "ZipCode": "zip_code",
        "AreaName": "area_name",
        "Population": "population",
        "MedianIncome": "median_income"
    }, inplace=True)

    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
    # Open DB with context manager
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()  # cursor allow me to write/edit data to db like pen

        if not os.path.exists(schema_path):
            raise FileNotFoundError(f"Missing CSV file: {schema_path}")

        # Load schema from .sql file
        with open(schema_path, "r") as f:
            cursor.executescript(f.read())

   
        # Insert Into Table
        df.to_sql("census_data", conn, if_exists="replace", index=False)

    print(f"✅ Data loaded into {db_path} using schema from {schema_path}")

except FileNotFoundError as e:
    print(f"❌ File Error: {e}")
    sys.exit(1)

except pd.errors.ParserError as e:
    print(f"❌ CSV Parsing Error")
    sys.exit(1)

except sqlite3.DatabaseError as e:
    print(f"❌ SQLite Error: {e}")
    sys.exit(1)

except Exception as e:
    print(f"❌ Unexpected Error: {e}")
    sys.exit(1)