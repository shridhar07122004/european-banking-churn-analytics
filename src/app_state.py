from __future__ import annotations

import pandas as pd
import streamlit as st

from src.data_cleaner import clean_data
from src.data_loader import load_csv, load_default_dataset, validate_dataframe
from src.feature_engineer import add_features


def load_dataset_ui() -> tuple[pd.DataFrame | None, dict | None]:
    df, report = load_default_dataset()
    uploaded = st.sidebar.file_uploader("Upload banking CSV", type=["csv"])
    if uploaded is not None:
        df = load_csv(uploaded)
        report = validate_dataframe(df)

    if df is None:
        st.info(
            "Add `data/European_Bank.csv` or upload the CSV from the sidebar to start the dashboard."
        )
        return None, None

    if report and not report["is_valid"]:
        st.error("Dataset is missing required columns: " + ", ".join(report["missing_columns"]))
        return None, report

    return add_features(clean_data(df)), report


def sidebar_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filters")
    geography = st.sidebar.multiselect(
        "Geography",
        sorted(df["Geography"].dropna().unique()),
        default=sorted(df["Geography"].dropna().unique()),
    )
    gender = st.sidebar.multiselect(
        "Gender",
        sorted(df["Gender"].dropna().unique()),
        default=sorted(df["Gender"].dropna().unique()),
    )
    age_min, age_max = int(df["Age"].min()), int(df["Age"].max())
    age_range = st.sidebar.slider("Age range", age_min, age_max, (age_min, age_max))

    filtered = df[
        df["Geography"].isin(geography)
        & df["Gender"].isin(gender)
        & df["Age"].between(age_range[0], age_range[1])
    ]
    if filtered.empty:
        st.warning("The selected filters returned no customers.")
    return filtered


def prepare_page(title: str, subtitle: str) -> pd.DataFrame | None:
    st.set_page_config(
        page_title="Banking Churn Analytics",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()
    st.sidebar.markdown(
        """
        <div class="sidebar-brand">
          <div class="brand-mark">EB</div>
          <div>
            <div class="brand-title">European Bank</div>
            <div class="brand-subtitle">Churn Intelligence</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <section class="page-hero">
          <div class="hero-kicker">Banking Analytics Suite</div>
          <h1>{title}</h1>
          <p>{subtitle}</p>
          <div class="hero-rule"></div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    df, report = load_dataset_ui()
    if report:
        with st.sidebar.expander("Data validation"):
            st.write(report)
    if df is None:
        return None
    return sidebar_filters(df)


def inject_css() -> None:
    css_path = __import__("pathlib").Path(__file__).resolve().parents[1] / "assets" / "style.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
