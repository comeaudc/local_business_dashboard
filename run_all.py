from ingest.fetch_census import fetch_median_data
from ingest.fetch_unemployment import fetch_unemployment
from transform.clean_census import clean_census
from transform.clean_unemployment import clean_unemployment
from transform.zip_to_fips_transform import zip_to_fips_transform
from load.census_load_sqlite import census_load
from load.unemployment_load_sqlite import unemployment_load
from load.zip_to_fips_load import zip_to_fips_load
from query.join_unemployment_to_zip import join_zip_to_unemployment

def run_all():
    print("🏁 Starting ETL Pipeline...")
    fetch_median_data()
    fetch_unemployment()
    clean_census()
    clean_unemployment()
    zip_to_fips_transform()
    census_load()
    unemployment_load()
    zip_to_fips_load()
    join_zip_to_unemployment()
    print("🎉 ETL Pipeline Completed!")

if __name__ == "__main__":
    try:
        run_all()
    except Exception as e:
        print(f"❌ Pipeline Failed: {e}")