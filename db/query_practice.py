import sqlite3
import sys

# Paths
db_path = "db/local_data.db"

try:
    # Connect to DB using context manager to auto .commit()/.close()/.resolve()
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Run a query
        cursor.execute("""
            SELECT zip_code, area_name, population, median_income
            FROM census_data
            WHERE population > 50000
            ORDER BY population DESC
            LIMIT 10;
        """)

        # Fetch and print results
        results = cursor.fetchall()
        print("ZIPs with population > 50,000:")
        # for row in results:
        #     print(row)

        # Extra Formatting
        for zip_code, area_name, population, median_income in results:
            print(f"{zip_code} | {area_name} | Population: {population:,} | Median Income: ${median_income:,.2f}")


        # Run the query to calculate average population
        cursor.execute("""
            SELECT AVG(population) FROM census_data;
        """)

        # Fetch the result
        average_population = cursor.fetchone()[0]

    # Display the result
    print(f"📊 Average population across ZIP codes: {int(average_population):,}")

except sqlite3.DatabaseError as e:
    print(f"❌ SQLite Error: {e}")
    sys.exit(1)

except Exception as e:
    print(f"❌ Unexpected Error: {e}")
    sys.exit(1)
