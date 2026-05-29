from __future__ import annotations

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned.columns = [str(column).strip() for column in cleaned.columns]

    drop_columns = ["RowNumber", "CustomerId", "Surname"]
    cleaned = cleaned.drop(columns=[c for c in drop_columns if c in cleaned.columns])
    cleaned = cleaned.drop_duplicates()

    numeric_columns = [
        "CreditScore",
        "Age",
        "Tenure",
        "Balance",
        "NumOfProducts",
        "HasCrCard",
        "IsActiveMember",
        "EstimatedSalary",
        "Exited",
    ]
    for column in numeric_columns:
        if column in cleaned.columns:
            cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    for column in cleaned.select_dtypes(include="number").columns:
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())

    for column in cleaned.select_dtypes(exclude="number").columns:
        mode = cleaned[column].mode(dropna=True)
        fallback = mode.iloc[0] if not mode.empty else "Unknown"
        cleaned[column] = cleaned[column].fillna(fallback)

    for column in ["HasCrCard", "IsActiveMember", "Exited"]:
        if column in cleaned.columns:
            cleaned[column] = cleaned[column].round().clip(0, 1).astype(int)

    return cleaned

