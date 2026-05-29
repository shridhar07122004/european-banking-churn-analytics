from __future__ import annotations

import streamlit as st

from src.app_state import prepare_page
from src.chart_factory import bar, scatter
from src.kpi_engine import churn_by_segment, overall_kpis


df = prepare_page("High Value Customers", "Premium customer risk and balance exposure")

if df is not None and not df.empty:
    kpis = overall_kpis(df)
    premium = df[df["Value Tier"].astype(str) == "Premium"]
    premium_rate = premium["Exited"].mean() * 100 if len(premium) else 0

    cols = st.columns(4)
    cols[0].metric("Premium Customers", f"{len(premium):,}")
    cols[1].metric("Premium Churn", f"{premium_rate:.2f}%")
    cols[2].metric("Overall Churn", f"{kpis['overall_churn_rate']:.2f}%")
    cols[3].metric("Premium Exposure", f"${premium.loc[premium['Exited'] == 1, 'Balance'].sum():,.0f}")

    left, right = st.columns(2)
    with left:
        value = churn_by_segment(df, "Value Tier")
        st.plotly_chart(bar(value, "Value Tier", "Churn Rate", "Churn Rate by Value Tier"), use_container_width=True)
    with right:
        exposure = (
            df[df["Exited"] == 1]
            .groupby("Value Tier", observed=False)["Balance"]
            .sum()
            .reset_index(name="Balance Exposure")
        )
        st.plotly_chart(bar(exposure, "Value Tier", "Balance Exposure", "Balance Exposure by Tier"), use_container_width=True)

    st.plotly_chart(
        scatter(df, "EstimatedSalary", "Balance", "Salary x Balance by Churn Status", "Churn Label"),
        use_container_width=True,
    )

