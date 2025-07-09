CREATE TABLE IF NOT EXISTS unemployment_data (
    series_id TEXT,
    year INTEGER,
    period TEXT,
    month TEXT,
    unemployment_rate REAL,
    geo_fips TEXT, -- gov standard for location, similar to ZIP code
    PRIMARY KEY (series_id, year, period)
);