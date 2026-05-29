from __future__ import annotations

import streamlit as st

from src.app_state import prepare_page
from src.chart_factory import bar
from src.kpi_engine import churn_by_segment


df = prepare_page("Customer Segmentation", "Churn patterns across customer profile bands")

if df is not None and not df.empty:
    segments = ["Age Segment", "Credit Score Band", "Balance Segment", "Tenure Group"]
    for first, second in [segments[:2], segments[2:]]:
        left, right = st.columns(2)
        for column, container in [(first, left), (second, right)]:
            with container:
                segment_df = churn_by_segment(df, column)
                st.plotly_chart(
                    bar(segment_df, column, "Churn Rate", f"Churn Rate by {column}"),
                    use_container_width=True,
                )

    ranking = []
    for segment in segments + ["Value Tier"]:
        table = churn_by_segment(df, segment).rename(columns={segment: "Segment"})
        table.insert(0, "Segment Type", segment)
        ranking.append(table)
    st.subheader("Segment Ranking")
    st.dataframe(
        __import__("pandas").concat(ranking, ignore_index=True).sort_values("Churn Rate", ascending=False),
        use_container_width=True,
        hide_index=True,
    )

