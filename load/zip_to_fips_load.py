import sqlite3
import pandas as pd
import os
import sys

# Paths
cleaned_path = "data/cleaned/zip_to_fips.csv"
db_path = "db/local_data.db"
schema_path = "db/schemas/zip_to_fip_schema.sql"

def zip_to_fips_load():
    try:
        if not os.path.exists(cleaned_path):
            raise FileNotFoundError(f"Missing CSV File: {cleaned_path}")
        
        df = pd.read_csv(cleaned_path)

        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            
            if not os.path.exists(schema_path):
                raise FileNotFoundError(f"Missing Schema File: {schema_path}")
            
            with open(schema_path, "r") as f:
                cursor.executescript(f.read())

            df.to_sql("zip_to_fip", conn, if_exists="replace", index=False)

        print(f"📦 Inserted {len(df):,} rows into 'zip_to_fips'")
        print(f"✅ Data loaded into {db_path} using schema from  {schema_path}")

    except FileNotFoundError as e:
        print(f"❌ File Error: {e}")
        sys.exit(1)


    except sqlite3.DatabaseError as e:
        print(f"❌ SQLite Error: {e}")
        sys.exit(1)

    except pd.errors.ParserError as e:
        print(f"❌ CSV Parsing Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    zip_to_fips_load()