# Local Information Dashboard

```
project/
├── data/
│   ├── raw/
│   ├── cleaned/
├── db/
│   ├── schemas/
│   ├── sql_queries/
│   └── local_data.db
├── ingest/
│   └── fetch_census.py
│   └── fetch_unemployment.py
├── transform/
│   └── transform_census.py
│   └── transform_unemployment.py
├── load/
│   └── load_census.py
│   └── load_unemployment.py
│   └── load_zip_to_fip.py
├── query/
│   └── join_unemployment_zip.py
├── run_all.py
└── README.md

```

[United Census Bureau](https://www.census.gov/en.html) - API For all census data (i.e. median income by zip, ect)

[Bureau of Statistics](https://www.bls.gov/) - API For unemployment data

[HUD Website](https://www.huduser.gov/portal/) - ZIP to FIPS tables excel sheet