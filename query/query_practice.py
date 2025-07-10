import sqlite3
import sys
import os
import pandas as pd

# Paths
db_path = "db/local_data.db"
sql_path = "db/sql_queries/join_unemployment_to_zip.sql"
joined_csv="data/cleaned/unemployment_zip_joined.csv"

try:
    # Make sure output directory exists
    os.makedirs(os.path.dirname(joined_csv), exist_ok=True)

    # Connect to DB using context manager to auto .commit()/.close()/.resolve()
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Separate SQL File being run to be dynamic
        if not os.path.exists(sql_path):
            raise FileNotFoundError(f"Missing SQL Query: {sql_path}")
        
        # Open sql query
        with open(sql_path, "r") as f:
            query = f.read()

        # Execute SQL Query
        df = pd.read_sql_query(query, conn)

        df.to_csv(joined_csv, index=False)
        
        print(f"✅ Exported joined data to {joined_csv}")

        # Run a query with hardcoded sql
        # cursor.execute("""
        #     SELECT zip_code, area_name, population, median_income
        #     FROM census_data
        #     WHERE population > 50000
        #     ORDER BY population DESC
        #     LIMIT 10;
        # """)




        # Fetch and print results
        # results = cursor.fetchall()
        # print("ZIPs with population > 50,000:")
        # for row in results:
        #     print(row)

        # Extra Formatting
        # for zip_code, area_name, population, median_income in results:
        #     print(f"{zip_code} | {area_name} | Population: {population:,} | Median Income: ${median_income:,.2f}")


        # # Run the query to calculate average population
        # cursor.execute("""
        #     SELECT AVG(population) FROM census_data;
        # """)

        # Fetch the result
        # average_population = cursor.fetchone()[0]

    # Display the result
    # print(f"📊 Average population across ZIP codes: {int(average_population):,}")

except sqlite3.DatabaseError as e:
    print(f"❌ SQLite Error: {e}")
    sys.exit(1)

except pd.errors.ParserError as e:
    print(f"❌ Parsing Error: {e}")

except FileNotFoundError as e:
    print(f"❌ File Error: {e}")

except Exception as e:
    print(f"❌ Unexpected Error: {e}")
    sys.exit(1)
