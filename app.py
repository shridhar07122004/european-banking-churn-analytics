from __future__ import annotations

import streamlit as st

from src.app_state import prepare_page
from src.chart_factory import bar, donut
from src.kpi_engine import overall_kpis, top_risk_segments


df = prepare_page(
    "Customer Segmentation & Churn Pattern Analytics",
    "European banking churn intelligence dashboard",
)

if df is not None and not df.empty:
    kpis = overall_kpis(df)
    cols = st.columns(5)
    cols[0].metric("Customers", f"{kpis['total_customers']:,}")
    cols[1].metric("Churn Rate", f"{kpis['overall_churn_rate']:.2f}%")
    cols[2].metric("Churned", f"{kpis['churned_customers']:,}")
    cols[3].metric("Balance Exposure", f"${kpis['revenue_at_risk']:,.0f}")
    cols[4].metric("Avg Value Score", f"{kpis['avg_customer_value']:.1f}")

    churn_counts = df["Churn Label"].value_counts().rename_axis("Status").reset_index(name="Customers")
    left, right = st.columns([1, 1])
    with left:
        st.plotly_chart(donut(churn_counts, "Status", "Customers", "Overall Churn Mix"), use_container_width=True)
    with right:
        tenure = (
            df.groupby("Tenure Group", observed=False)["Exited"]
            .mean()
            .mul(100)
            .reset_index(name="Churn Rate")
        )
        st.plotly_chart(bar(tenure, "Tenure Group", "Churn Rate", "Churn Rate by Tenure Group"), use_container_width=True)

    st.subheader("Top Risk Segments")
    st.dataframe(
        top_risk_segments(df).head(12),
        use_container_width=True,
        hide_index=True,
        column_config={
            "Churn Rate": st.column_config.NumberColumn(format="%.2f%%"),
            "Balance_Exposure": st.column_config.NumberColumn("Balance Exposure", format="$%.0f"),
        },
    )

