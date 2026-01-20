from pathlib import Path
import pandas as pd
import pytest

from src.data.ingest import clean_data, validate_data

def test_basic_clean_converts_totalcharges():
    df = pd.DataFrame({
        "customerID": ["A"],
        "gender": ["Female"],
        "SeniorCitizen": [0],
        "Partner": ["Yes"],
        "Dependents": ["No"],
        "tenure": [1],
        "PhoneService": ["Yes"],
        "MultipleLines": ["No"],
        "InternetService": ["DSL"],
        "OnlineSecurity": ["No"],
        "OnlineBackup": ["Yes"],
        "DeviceProtection": ["No"],
        "TechSupport": ["No"],
        "StreamingTV": ["No"],
        "StreamingMovies": ["No"],
        "Contract": ["Month-to-month"],
        "PaperlessBilling": ["Yes"],
        "PaymentMethod": ["Electronic check"],
        "MonthlyCharges": [29.85],
        "TotalCharges": [" "],  # blank -> NaN
        "Churn": ["No"],
    })
    cleaned = clean_data(df)
    assert "TotalCharges" in cleaned.columns
    assert cleaned["TotalCharges"].isna().iloc[0]

def test_schema_validation_passes_on_minimal_row():
    # Reuse the same minimal df but ensure TotalCharges is numeric or NaN
    df = pd.DataFrame({
        "customerID": ["A"],
        "gender": ["Female"],
        "SeniorCitizen": [0],
        "Partner": ["Yes"],
        "Dependents": ["No"],
        "tenure": [1],
        "PhoneService": ["Yes"],
        "MultipleLines": ["No"],
        "InternetService": ["DSL"],
        "OnlineSecurity": ["No"],
        "OnlineBackup": ["Yes"],
        "DeviceProtection": ["No"],
        "TechSupport": ["No"],
        "StreamingTV": ["No"],
        "StreamingMovies": ["No"],
        "Contract": ["Month-to-month"],
        "PaperlessBilling": ["Yes"],
        "PaymentMethod": ["Electronic check"],
        "MonthlyCharges": [29.85],
        "TotalCharges": [29.85],
        "Churn": ["No"],
    })
    cleaned = clean_data(df)
    validated = validate_data(cleaned)
    assert len(validated) == 1

def test_schema_fails_if_missing_column():
    df = pd.DataFrame({"customerID": ["A"]})
    with pytest.raises(Exception):
        validate(df)
