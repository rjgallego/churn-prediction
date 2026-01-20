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
        "gender": Column(pa.String, Check.isin(GENDER), nullable=False),
        "SeniorCitizen": Column(pa.Int, Check.in_range(0, 1), nullable=False),
        "Partner": Column(pa.String, Check.isin(YES_NO), nullable=False),
        "Dependents": Column(pa.String, Check.isin(YES_NO), nullable=False),
        "tenure": Column(pa.Int, Check.greater_than_equal_to(0), nullable=False),
        "PhoneService": Column(pa.String, Check.isin(YES_NO), nullable=False),
        "MultipleLines": Column(pa.String, Check.isin(MULTIPLE_LINES), nullable=False),
        "InternetService": Column(pa.String, Check.isin(INTERNET_SERVICE), nullable=False),
        "OnlineSecurity": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}, nullable=False),
        "OnlineBackup": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}, nullable=False),
        "DeviceProtection": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}, nullable=False),
        "TechSupport": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}, nullable=False),
        "StreamingTV": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}, nullable=False),
        "StreamingMovies": Column(pa.String, Check.isin(YES_NO) | {"No internet service"}, nullable=False),
        "Contract": Column(pa.String, Check.isin(CONTRACT), nullable=False),
        "PaperlessBilling": Column(pa.String, Check.isin(YES_NO), nullable=False),
        "PaymentMethod": Column(pa.String, Check.isin(PAYMENT_METHOD), nullable=False),
        "MonthlyCharges": Column(pa.Float, Check.greater_than_equal_to(0.0), nullable=False),
        "TotalCharges": Column(pa.Float, Check.greater_than_equal_to(0.0), nullable=True),
        "Churn": Column(pa.String, Check.isin(YES_NO), nullable=False),
    },
    coerce=True,
    strict=True,
    name="CustomerIDSchema"
)