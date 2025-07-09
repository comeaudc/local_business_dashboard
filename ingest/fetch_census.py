import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://api.census.gov/data/2021/acs/acs5'

PARAMS = {
    "get": "NAME,B01003_001E,B19013_001E",
    "for": "zip code tabulation area:*"
}

def fetch_median_data():
    response = requests.get(BASE_URL, params=PARAMS)
    if response.status_code == 200:
        data = response.json()
        headers = data[0]
        rows = data[1:]

        os.makedirs("data/raw", exist_ok=True)
        with open("data/raw/census_by_zip.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
        print("✅ Census data saved to data/raw/census_by_zip.csv")
    else:
        print(f"❌ Failed to fetch data. Status code: {response.status_code}")



if __name__ == "__main__":
    fetch_median_data()