import requests
import csv
import os

BASE_URL = 'https://api.census.gov/data/2021/acs/acs5'
raw_path = "data/raw/census_by_zip.csv"

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
        os.makedirs(os.path.dirname(raw_path), exist_ok=True)
        with open(raw_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)

        print(f"✅ Census data saved to {raw_path}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error during request: {e}")

    except ValueError as e:
        print(f"❌ Data format error: {e}")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    fetch_median_data()