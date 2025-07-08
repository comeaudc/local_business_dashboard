import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()

# Variables
apiKey = os.environ.get("blsAPI")
URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

import requests

API_KEY = "YOUR_API_KEY"
url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

body = {
    "seriesid": ["LAUCN040010000000003"],  # Change to your series ID(s)
    "startyear": "2022",
    "endyear": "2023",
    "registrationKey": apiKey
}

def fetch_unemployement_data():
    response = requests.post(URL, json=body)
    if response.status_code == 200:
        data = response.json()
        print(data)


if __name__ == "__main__":
    fetch_unemployement_data()