from __future__ import annotations

import streamlit as st

from src.app_state import prepare_page
from src.chart_factory import bar, heatmap
from src.kpi_engine import churn_by_segment


df = prepare_page("Customer Behavior", "Engagement, product ownership, and card behavior")

if df is not None and not df.empty:
    left, right = st.columns(2)
    with left:
        active = churn_by_segment(df, "Engagement Status")
        st.plotly_chart(bar(active, "Engagement Status", "Churn Rate", "Active vs Inactive Churn"), use_container_width=True)
    with right:
        card = churn_by_segment(df, "Credit Card Status")
        st.plotly_chart(bar(card, "Credit Card Status", "Churn Rate", "Credit Card Ownership Churn"), use_container_width=True)

    products = churn_by_segment(df, "NumOfProducts")
    st.plotly_chart(bar(products, "NumOfProducts", "Churn Rate", "Product Ownership vs Churn"), use_container_width=True)

    interaction = (
        df.groupby(["Engagement Status", "NumOfProducts"], observed=False)["Exited"]
        .mean()
        .mul(100)
        .reset_index(name="Churn Rate")
    )
    st.plotly_chart(
        heatmap(interaction, "NumOfProducts", "Engagement Status", "Churn Rate", "Engagement x Products Heatmap"),
        use_container_width=True,
    )

