from __future__ import annotations

import streamlit as st

from src.app_state import prepare_page
from src.chart_factory import bar, donut
from src.kpi_engine import churn_by_segment, overall_kpis, top_risk_segments


df = prepare_page("Executive Dashboard", "Portfolio-level churn KPIs and risk hotspots")

if df is not None and not df.empty:
    kpis = overall_kpis(df)
    cols = st.columns(4)
    cols[0].metric("Overall Churn", f"{kpis['overall_churn_rate']:.2f}%")
    cols[1].metric("Customers", f"{kpis['total_customers']:,}")
    cols[2].metric("Balance Exposure", f"${kpis['revenue_at_risk']:,.0f}")
    cols[3].metric("Inactive Churn", f"{kpis['engagement_drop_indicator']:.2f}%")

    left, right = st.columns(2)
    with left:
        churn_counts = df["Churn Label"].value_counts().rename_axis("Status").reset_index(name="Customers")
        st.plotly_chart(donut(churn_counts, "Status", "Customers", "Churn Composition"), use_container_width=True)
    with right:
        geography = churn_by_segment(df, "Geography")
        st.plotly_chart(bar(geography, "Geography", "Churn Rate", "Country Churn Rate"), use_container_width=True)

    st.subheader("Highest Priority Segments")
    st.dataframe(top_risk_segments(df).head(10), use_container_width=True, hide_index=True)

