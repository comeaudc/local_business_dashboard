import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()

# Variables
apiKey = os.environ.get("blsAPI")
URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

body = {
        "seriesid": [
        "LAUCN040010000000003",
        "LAUCN060370000000003",
        "LAUCN000000000000003"
    ],  # Change to your series ID(s)

    "startyear": "2022",
    "endyear": "2023",
    "registrationKey": apiKey
}

def fetch_unemployment_data():
    if not apiKey:
        raise ValueError("❌ Missing BLS api key. Check .env file.")
    
    try:

        response = requests.post(URL, json=body, timeout=10)

        if response.status_code != 200:
            raise Exception(f"HTTP {response.status_code}: {response.text}")
        
        data = response.json()
        # print(len(data["Results"]["series"][0]["data"]))

        if "Results" not in data or "series" not in data["Results"]:
            raise KeyError("❌ Unexpected response format. 'Results.serires' missing.")

        rows = []
        headers = ["series_id", "year", "period", "periodName", "value", "footnotes"]

        # format data for csv file 
        for series in data["Results"]["series"]:
            series_id = series["seriesID"]
            for entry in series["data"]:
                row = [
                    series_id,
                    entry.get("year"),
                    entry.get("period"),
                    entry.get("periodName"),
                    entry.get("value"),
                    entry.get("footnotes")[0].get("text") if entry.get("footnotes") and entry["footnotes"][0] else ""
                ]
                rows.append(row)

        # Make sure directory exists and if not make one
        os.makedirs("data/raw", exist_ok=True)
        with open("data/raw/unemployment.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)

        print(f"✅ Saved Unemplyement data for {len(rows)} series to data/raw/unemlpoyement.csv")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error during request: {e}")

    except ValueError as e:
        print(f"❌ Data format error: {e}")

    except KeyError as e:
        print(f"Missing Expected columns in API Response: {e}")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    fetch_unemployment_data()