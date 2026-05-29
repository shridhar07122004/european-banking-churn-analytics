from __future__ import annotations

import pandas as pd


def pct(numerator: float, denominator: float) -> float:
    return 0.0 if denominator == 0 else round((numerator / denominator) * 100, 2)


def overall_kpis(df: pd.DataFrame) -> dict:
    total = len(df)
    churned = int(df["Exited"].sum())
    premium = df[df["Value Tier"].astype(str) == "Premium"]
    inactive = df[df["IsActiveMember"] == 0]
    return {
        "total_customers": total,
        "churned_customers": churned,
        "overall_churn_rate": pct(churned, total),
        "retained_customers": total - churned,
        "revenue_at_risk": float(df.loc[df["Exited"] == 1, "Balance"].sum()),
        "avg_customer_value": float(df["Customer Value Score"].mean()),
        "high_value_churn_ratio": pct(premium["Exited"].sum(), len(premium)),
        "engagement_drop_indicator": pct(inactive["Exited"].sum(), len(inactive)),
    }


def churn_by_segment(df: pd.DataFrame, segment: str) -> pd.DataFrame:
    grouped = (
        df.groupby(segment, observed=False)
        .agg(
            Customers=("Exited", "size"),
            Churned=("Exited", "sum"),
            Balance_Exposure=("Balance", lambda s: s[df.loc[s.index, "Exited"] == 1].sum()),
        )
        .reset_index()
    )
    grouped["Churn Rate"] = grouped.apply(
        lambda row: pct(row["Churned"], row["Customers"]), axis=1
    )
    return grouped.sort_values("Churn Rate", ascending=False)


def geographic_risk(df: pd.DataFrame) -> pd.DataFrame:
    overall_rate = overall_kpis(df)["overall_churn_rate"]
    geo = churn_by_segment(df, "Geography")
    geo["Geographic Risk Index"] = geo["Churn Rate"].apply(
        lambda value: pct(value, overall_rate)
    )
    return geo


def top_risk_segments(df: pd.DataFrame) -> pd.DataFrame:
    frames = []
    for column in [
        "Geography",
        "Gender",
        "Age Segment",
        "Credit Score Band",
        "Balance Segment",
        "Value Tier",
    ]:
        segment = churn_by_segment(df, column)
        segment.insert(0, "Segment Type", column)
        segment = segment.rename(columns={column: "Segment"})
        frames.append(segment)
    combined = pd.concat(frames, ignore_index=True)
    minimum_segment_size = 10 if len(df) >= 100 else 1
    return combined[combined["Customers"] >= minimum_segment_size].sort_values(
        ["Churn Rate", "Customers"], ascending=[False, False]
    )
