DROP TABLE IF EXISTS unemployment_zip_joined;

CREATE TABLE unemployment_zip_joined AS
SELECT
    u.series_id,
    u.year,
    u.period,
    u.month,
    u.unemployment_rate,
    u.geo_fips,
    z.zip_code,
    z.city,
    z.state,
    c.population,
    c.median_income
FROM unemployment_data u
JOIN zip_to_fip z ON u.geo_fips = z.county_fips
JOIN census_data c ON c.zip_code = z.zip_code;
