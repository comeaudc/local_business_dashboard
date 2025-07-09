import sqlite3
import pandas as pd
import os
import sys

# Paths
cleaned_path = "data/cleaned/cleaned_unemployment.csv"
db_path = "db/local_data.db"
schema_path = "db/schemas/unemployment_schema.sql"

try:
    if not os.path.exists(cleaned_path):
        raise FileNotFoundError(f"Missing CSV File: {cleaned_path}")
    
    df = pd.read_csv(cleaned_path)

    # Prepare df to match schema
    df.rename(columns={
        "periodName": "month",
    }, inplace=True)

    
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    # Open db with context manager
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        if not os.path.exists(schema_path):
            raise FileNotFoundError(f"Missing Schema File: {schema_path}")
        with open(schema_path, "r") as f:
            cursor.executescript(f.read())

        df.to_sql("unemployment_data", conn, if_exists="replace", index=False)
    
    # for testing/debugging
    # print(f"📈 {len(df):,} rows inserted into unemployment_table")
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
    print(f"Unexpected Error: {e}")
    sys.exit(1)