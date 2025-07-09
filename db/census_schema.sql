CREATE TABLE IF NOT EXISTS census_median_data (
    zip_code TEXT PRIMARY KEY,
    area_name TEXT,
    population INTEGER,
    median_income REAL
);