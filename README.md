# Local Economic Dashboard

This project provides a dynamic, interactive dashboard for exploring U.S. economic data (Census and Unemployment) by ZIP code and state using a local SQLite database and [Streamlit](https://streamlit.io/).

## Project Features

- Fetches real data from:
  - U.S. Census Bureau (population and median income)
  - Bureau of Labor Statistics (unemployment rates)
- Cleans, transforms, and stores the data in a local SQLite database
- Uses a crosswalk file to map ZIP codes to counties (FIPS codes)
- Merges datasets for regional insights
- Interactive dashboard with filtering and visualizations
- Easy-to-run scripts organized by pipeline stage

##  Technologies Used

- Python 3.10+
- SQLite
- pandas
- requests
- dotenv
- Streamlit

##  Project Structure

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

##  How to Run

### 1. Clone the Repo

```
bash
git clone https://github.com/yourusername/local-business-dashboard.git
cd local-business-dashboard
```

### 2.  Create Virtual Enviroment
```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
### 3. Install Dependences
```
pip install -r requirements.txt
```

### 4. Set Enviromental Variables
```
blsAPI=YOUR_BLS_API_KEY
```

### 5. Run the Data Pipline
```
python run_all.py
```

### 6. Launch the Streamlit Dashboard
```
streamlit run app/dashboard.py
```

## Requirements
Python 3.10+

BLS API key (free from https://www.bls.gov/developers/)

ZIP_COUNTY crosswalk file from HUD (link)

## Sources

[United Census Bureau](https://www.census.gov/en.html) - API For all census data (i.e. median income by zip, ect)

[Bureau of Statistics](https://www.bls.gov/) - API For unemployment data

[HUD Website](https://www.huduser.gov/portal/) - ZIP to FIPS tables excel sheet