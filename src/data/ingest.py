from pathlib import Path
import pandas as pd

from config import RAW_PATH, PROCESSED_PATH
from src.schema import CUSTOMER_SCHEMA

def load_raw_data(path: str) -> pd.DataFrame:
    """Load and validate customer data from a CSV file.

    Args:
        path (str): The file path to the CSV data."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"The file at {path} does not exist.")
    df = pd.read_csv(path)

    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and validate the customer data.

    Args:
        df (pd.DataFrame): The raw customer data."""

    df = df.copy()

    # Strip whitespace from string columns
    str_cols = df.select_dtypes(include=["object"]).columns
    for col in str_cols:
        df[col] = df[col].str.strip()
    
    # Convert 'TotalCharges' to numeric, coercing errors to NaN
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Ensure other numeric columns are numeric type
    df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"], errors="raise")
    df["tenure"] = pd.to_numeric(df["tenure"], errors="raise").astype(int)
    df["SeniorCitizen"] = pd.to_numeric(df["SeniorCitizen"], errors="raise").astype(int)

    return df

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Validate the customer data against the schema.

    Args:
        df (pd.DataFrame): The cleaned customer data."""
    
    validated_df = CUSTOMER_SCHEMA.validate(df, lazy=True)

    return validated_df

def write_processed_data(df: pd.DataFrame, path: str) -> None:
    """Write the processed customer data to a CSV file.

    Args:
        df (pd.DataFrame): The processed customer data.
        path (str): The file path to save the CSV data."""

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Processed data written to {path}")

    return

def main():
    raw_df = load_raw_data(RAW_PATH)
    clean_df = clean_data(raw_df)
    validated_df = validate_data(clean_df)
    write_processed_data(validate_df, PROCESSED_PATH)


if __name__ == "__main__":
    main()