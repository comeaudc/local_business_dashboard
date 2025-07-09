```
local-business-dashboard/
│
├── ingest/                # Scripts to pull raw data from APIs
│   └── fetch_census.py
│
├── transform/             # Data cleaning and formatting
│   └── clean_census.py
│
├── db/                    # DB schema and loading scripts
│   ├── schema.sql
│   └── load_data.py
│
├── app/                   # Streamlit dashboard
│   └── dashboard.py
│
├── data/                  # Raw and cleaned CSVs
│   ├── raw/
│   └── cleaned/
│
├── .env                   # API keys and secrets (use dotenv)
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
└── run_all.py             # Optional main script to run all steps

```

[United Census Bureau](https://www.census.gov/en.html) - API For all census data (i.e. median income by zip, ect)

[Bureau of Statistics](https://www.bls.gov/) - API For unemployment data