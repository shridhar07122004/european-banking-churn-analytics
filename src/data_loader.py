from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

import pandas as pd
import streamlit as st


REQUIRED_COLUMNS = {
    "CreditScore",
    "Geography",
    "Gender",
    "Age",
    "Tenure",
    "Balance",
    "NumOfProducts",
    "HasCrCard",
    "IsActiveMember",
    "EstimatedSalary",
    "Exited",
}


@st.cache_data(show_spinner=False)
def load_csv(source: str | BinaryIO) -> pd.DataFrame:
    return pd.read_csv(source)


def default_data_path() -> Path:
    data_dir = Path(__file__).resolve().parents[1] / "data"
    for filename in ["European_Bank.csv", "Churn_Modelling.csv"]:
        path = data_dir / filename
        if path.exists():
            return path
    return data_dir / "European_Bank.csv"


def validate_dataframe(df: pd.DataFrame) -> dict:
    missing_columns = sorted(REQUIRED_COLUMNS - set(df.columns))
    binary_issues = {}
    for column in ["HasCrCard", "IsActiveMember", "Exited"]:
        if column in df.columns:
            values = set(pd.Series(df[column]).dropna().unique())
            invalid = sorted(values - {0, 1, 0.0, 1.0})
            if invalid:
                binary_issues[column] = invalid

    return {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "missing_columns": missing_columns,
        "missing_values": df.isna().sum().loc[lambda s: s > 0].to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "binary_issues": binary_issues,
        "is_valid": not missing_columns,
    }


def load_default_dataset() -> tuple[pd.DataFrame | None, dict | None]:
    path = default_data_path()
    if not path.exists():
        return None, None
    df = load_csv(str(path))
    return df, validate_dataframe(df)
