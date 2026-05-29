from __future__ import annotations

import pandas as pd
import streamlit as st

from src.app_state import prepare_page
from src.kpi_engine import geographic_risk, overall_kpis, top_risk_segments


df = prepare_page("Recommendations", "Strategic retention actions by risk signal")

if df is not None and not df.empty:
    kpis = overall_kpis(df)
    top_segments = top_risk_segments(df).head(5)
    geo = geographic_risk(df).head(1)

    st.subheader("Key Findings")
    findings = [
        f"Overall churn rate is {kpis['overall_churn_rate']:.2f}% across {kpis['total_customers']:,} customers.",
        f"Estimated balance exposure from churned customers is ${kpis['revenue_at_risk']:,.0f}.",
        f"Inactive customers show a churn rate of {kpis['engagement_drop_indicator']:.2f}%.",
    ]
    if not geo.empty:
        findings.append(
            f"{geo.iloc[0]['Geography']} has the highest geographic risk index at {geo.iloc[0]['Geographic Risk Index']:.2f}."
        )
    for finding in findings:
        st.write(f"- {finding}")

    st.subheader("Retention Strategy Framework")
    strategy = pd.DataFrame(
        [
            ["Inactive customers", "Reactivation offers, advisor outreach, digital engagement nudges", "High"],
            ["Premium value tier", "Relationship manager review, fee benefits, retention call list", "High"],
            ["High-risk geography", "Localized service diagnostics and targeted loyalty campaigns", "Medium"],
            ["Low credit score band", "Financial health education and product-fit review", "Medium"],
            ["New tenure customers", "Onboarding check-ins and early product usage prompts", "Medium"],
        ],
        columns=["Segment", "Recommended Action", "Priority"],
    )
    st.dataframe(strategy, use_container_width=True, hide_index=True)

    st.subheader("Action Priority Matrix")
    st.dataframe(
        top_segments[["Segment Type", "Segment", "Customers", "Churned", "Churn Rate", "Balance_Exposure"]],
        use_container_width=True,
        hide_index=True,
    )

