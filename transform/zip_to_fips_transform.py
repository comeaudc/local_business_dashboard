import pandas as pd
import os

# Paths
raw_path = "data/raw/ZIP_COUNTY_032025.xlsx"
cleaned_path = "data/cleaned/zip_to_fips.csv"

def zip_to_fips_transform():

     try:
          if not os.path.exists(raw_path):
               raise FileNotFoundError(f"Missing Crosswalk File: {raw_path}")
          
          df = pd.read_excel(raw_path, dtype=str)

     # Selecting Columns from excel file
          df = df[["ZIP", "COUNTY","USPS_ZIP_PREF_CITY", "USPS_ZIP_PREF_STATE"]].drop_duplicates()

          df.columns = ["zip_code", "county_fips", "city", "state"]

          df["zip_code"] = df["zip_code"].str.zfill(5)
          df["county_fips"] = df["county_fips"].str.zfill(5)
          df["city"] = df["city"].str.strip().str.title()
          df["state"] = df["state"].str.strip().str.upper()

          os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
          df.to_csv(cleaned_path, index=False)
          print(f"✅ Cleaned Crosswalk saved to {cleaned_path}")

     except FileNotFoundError as e:
          print(f"❌ File Error: {e}")

     except Exception as e:
          print(f"❌ Unexpected Error: {e}")


if __name__ == "__main__":
     zip_to_fips_transform()