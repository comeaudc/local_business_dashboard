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
    try:
        response = requests.get(BASE_URL, params=PARAMS, timeout=10)


        if response.status_code != 200:
            raise Exception(f"❌ HTTP {response.status_code}: {response.text}")
        
       
        data = response.json()

        if not data or len(data) < 2:
            raise ValueError("❌ Unexpected data format from Census API")

        headers = data[0]
        rows = data[1:]

        # Make sure directory exists and if not make one
        os.makedirs("data/raw", exist_ok=True)
        with open("data/raw/census_by_zip.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)

        print("✅ Census data saved to data/raw/census_by_zip.csv")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error during request: {e}")

    except ValueError as e:
        print(f"❌ Data format error: {e}")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    fetch_median_data()