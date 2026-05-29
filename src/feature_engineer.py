from __future__ import annotations

import pandas as pd


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    featured = df.copy()

    featured["Age Segment"] = pd.cut(
        featured["Age"],
        bins=[0, 29, 45, 60, float("inf")],
        labels=["<30", "30-45", "46-60", ">60"],
        include_lowest=True,
    )
    featured["Credit Score Band"] = pd.cut(
        featured["CreditScore"],
        bins=[0, 579, 700, float("inf")],
        labels=["Low", "Medium", "High"],
        include_lowest=True,
    )
    featured["Tenure Group"] = pd.cut(
        featured["Tenure"],
        bins=[-1, 2, 6, 10],
        labels=["New", "Mid-Term", "Long-Term"],
    )
    featured["Balance Segment"] = pd.cut(
        featured["Balance"],
        bins=[-1, 0, 50_000, float("inf")],
        labels=["Zero", "Low", "High"],
    )
    featured["Salary Segment"] = pd.cut(
        featured["EstimatedSalary"],
        bins=[0, 50_000, 100_000, float("inf")],
        labels=["Low", "Medium", "High"],
        include_lowest=True,
    )

    balance_score = _minmax(featured["Balance"])
    salary_score = _minmax(featured["EstimatedSalary"])
    product_score = _minmax(featured["NumOfProducts"])
    featured["Customer Value Score"] = (
        balance_score * 0.45 + salary_score * 0.35 + product_score * 0.20
    ) * 100
    featured["Value Tier"] = pd.qcut(
        featured["Customer Value Score"].rank(method="first"),
        q=4,
        labels=["Bronze", "Silver", "Gold", "Premium"],
    )
    featured["Churn Label"] = featured["Exited"].map({0: "Retained", 1: "Churned"})
    featured["Engagement Status"] = featured["IsActiveMember"].map(
        {0: "Inactive", 1: "Active"}
    )
    featured["Credit Card Status"] = featured["HasCrCard"].map(
        {0: "No Card", 1: "Has Card"}
    )
    return featured


def _minmax(series: pd.Series) -> pd.Series:
    minimum = series.min()
    spread = series.max() - minimum
    if spread == 0:
        return pd.Series(0.0, index=series.index)
    return (series - minimum) / spread
