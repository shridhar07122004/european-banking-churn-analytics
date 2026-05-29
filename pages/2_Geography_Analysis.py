from __future__ import annotations

import streamlit as st

from src.app_state import prepare_page
from src.chart_factory import bar, gauge, heatmap
from src.kpi_engine import geographic_risk


df = prepare_page("Geography Analysis", "Country-level risk and demographic interactions")

if df is not None and not df.empty:
    geo = geographic_risk(df)
    st.plotly_chart(bar(geo, "Geography", "Churn Rate", "Country-wise Churn Rate"), use_container_width=True)

    gauge_cols = st.columns(max(1, min(3, len(geo))))
    for index, row in geo.reset_index(drop=True).iterrows():
        with gauge_cols[index % len(gauge_cols)]:
            st.plotly_chart(
                gauge(row["Geographic Risk Index"], f"{row['Geography']} Risk Index"),
                use_container_width=True,
            )

    interaction = (
        df.groupby(["Geography", "Age Segment"], observed=False)["Exited"]
        .mean()
        .mul(100)
        .reset_index(name="Churn Rate")
    )
    st.plotly_chart(
        heatmap(interaction, "Age Segment", "Geography", "Churn Rate", "Geography x Age Churn Heatmap"),
        use_container_width=True,
    )
    st.dataframe(geo, use_container_width=True, hide_index=True)

