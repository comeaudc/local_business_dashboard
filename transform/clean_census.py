import pandas as pd
import os

# Data paths
raw_path = "data/raw/census_by_zip.csv"
cleaned_path = "data/cleaned/cleaned_census_by_zip.csv"

def clean_census():

    try:
        if not os.path.exists(raw_path):
            raise FileNotFoundError(f"Missing CSV File: {raw_path}")
        
        # Load Dataframe aka table of data
        df = pd.read_csv(raw_path)

        # Preview Data (test as we go!!!) - can view columns as so, or whole dataset (whole data set will be very slow)
        # print('📊', df.columns.tolist())

        # Rename columns for clarity
        df.columns = ['AreaName', 'Population', 'MedianIncome', 'ZipCode']

        # Testing again!
        # print('📊', df.columns.tolist())

        df['ZipCode'] = df['ZipCode'].astype(str).str.zfill(5) # Keeps leading zeros
        df['Population'] = pd.to_numeric(df['Population'], errors='coerce') # try to set as number, if not "coerce" to nan"
        df["MedianIncome"] = pd.to_numeric(df["MedianIncome"], errors='coerce')# try to set as number, if not "coerce" to nan"

        # Remove Rows that now contain NaN
        df = df.dropna()

        # Remove duplicates if you want
        df = df.drop_duplicates(subset="ZipCode")

        os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
        df.to_csv(cleaned_path, index=False)
        print(f"✅ Cleaned Data saved to {cleaned_path}")

    except FileNotFoundError as e:
        print(f"❌ File Error: {e}")

    except pd.errors.ParserError as e:
        print(f"❌ Parsing Error: {e}")

    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    clean_census()