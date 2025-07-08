import sqlite3

# Paths
db_path = "db/local_data.db"

# Connect to DB
conn = sqlite3.connect(db_path)
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
for row in results:
    print(row)

# Run the query to calculate average population
cursor.execute("""
    SELECT AVG(population) FROM census_data;
""")

# Fetch the result
average_population = cursor.fetchone()[0]

# Display the result
print(f"📊 Average population across ZIP codes: {int(average_population):,}")

conn.close()