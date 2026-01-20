from pathlib import Path
import pandas as pd
import pandera.pandas as pa
from pandera.pandas import DataFrameSchema, Column, Check

YES_NO = {"Yes", "No"}
GENDER = {"Male", "Female"}
MULTIPLE_LINES = {"Yes", "No", "No phone service"}
INTERNET_SERVICE = {"DSL", "Fiber optic", "No"}
CONTRACT = {"Month-to-month", "One year", "Two year"}
PAYMENT_METHOD = {"Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"}


CUSTOMER_SCHEMA = DataFrameSchema(
    {
        "customerID": Column(pa.String, nullable=False),
        "gender": Column(pa.String, Check.isin(GENDER)),
        "SeniorCitizen": Column(pa.Int, Check.in_range(0, 1)),
        "Partner": Column(pa.String, Check.isin(YES_NO)),
        "Dependents": Column(pa.String, Check.isin(YES_NO)),
        "tenure": Column(pa.Int, Check.greater_than_equal_to(0)),
        "PhoneService": Column(pa.String, Check.isin(YES_NO)),
        "MultipleLines": Column(pa.String, Check.isin(MULTIPLE_LINES)),
        "InternetService": Column(pa.String, Check.isin(INTERNET_SERVICE)),
        "OnlineSecurity": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}),
        "OnlineBackup": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}),
        "DeviceProtection": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}),
        "TechSupport": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}),
        "StreamingTV": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}),
        "StreamingMovies": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}),
        "Contract": Column(pa.String, Check.isin(CONTRACT)),
        "PaperlessBilling": Column(pa.String, Check.isin(YES_NO)),
        "PaymentMethod": Column(pa.String, Check.isin(PAYMENT_METHOD))
    },
    coerce=True,
    strict=True,
    name="CustomerIDSchema"
)