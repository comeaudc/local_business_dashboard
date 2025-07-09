import pandas as pd
import os

raw_path = "data/raw/unemployment.csv"
cleaned_path = "data/cleaned/cleaned_unemployment.csv"

try:
    # If file path does not exist throw error
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Missing CSV file: {raw_path}")
    
    # read csv dataframe with panda for use
    df = pd.read_csv(raw_path)

    required_columns = ["series_id", "year", "period", "value"]
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise KeyError(f"Missing required columns: {missing}")

    # Testing
    # print("📊", df.columns.tolist())

    # headers for reference = ["series_id", "year", "period", "periodName", "value", "footnotes"]
    # Clean dataframe with panda
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    # Drop Nan Valued rows
    df = df.dropna(subset=["year", "value"])

    # Drop duplicates
    df = df.drop_duplicates(subset=["series_id", "year", "period"])

    # Rename column for clarity
    df.rename(columns={"value": "unemployment_rate"}, inplace=True)

    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
    df.to_csv(cleaned_path, index=False)
    print(f"✅ Cleaned Data saved to {cleaned_path}")

except FileNotFoundError as e:
    print(f"❌ File Error: {e}")

except pd.errors.ParserError as e:
    print(f"❌ CSV Parsing Error: {e}")

except KeyError as e:
    print(f"❌ Missing column: {e}")

except Exception as e:
    print(f"❌ Unexpected Error: {e}")