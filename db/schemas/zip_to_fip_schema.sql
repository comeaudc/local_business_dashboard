OPEN TABLE IF NOT EXISTS zip_to_fip_data(
    zip_code TEXT,
    county_fips TEXT,
    city TEXT,
    state TEXT,
    PRIMARY KEY (zip_code, county_fips)
);