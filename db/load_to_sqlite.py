import sqlite3
import panda as pd

# Paths
cleaned_path = "data/cleaned/cleaned_census_by_zip"
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
    
})