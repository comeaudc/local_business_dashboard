SELECT
    u.series_id,
    u.year,
    u.period,
    u.month,
    u.unemployment_rate,
    u.geo_fips,
    z.zip_code,
    z.city,
    z.state
FROM unemployment_data u
JOIN zip_to_fip z
    ON u.geo_fips = z.county_fips