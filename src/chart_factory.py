from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


COLORWAY = ["#2dd4bf", "#f97316", "#60a5fa", "#f43f5e", "#a3e635", "#c084fc"]
CHURN_COLORS = {"Retained": "#2dd4bf", "Churned": "#f43f5e"}


def apply_theme(fig: go.Figure) -> go.Figure:
    fig.update_layout(
        template="plotly_dark",
        colorway=COLORWAY,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=24, r=24, t=48, b=24),
        font=dict(family="Inter, Segoe UI, Arial", color="#e5eefb"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig


def bar(df: pd.DataFrame, x: str, y: str, title: str, color: str | None = None) -> go.Figure:
    fig = px.bar(df, x=x, y=y, color=color, title=title, text_auto=".1f")
    return apply_theme(fig)


def donut(df: pd.DataFrame, names: str, values: str, title: str) -> go.Figure:
    fig = px.pie(
        df,
        names=names,
        values=values,
        hole=0.58,
        title=title,
        color=names,
        color_discrete_map=CHURN_COLORS,
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    return apply_theme(fig)


def heatmap(df: pd.DataFrame, x: str, y: str, z: str, title: str) -> go.Figure:
    pivot = df.pivot_table(index=y, columns=x, values=z, aggfunc="mean", observed=False)
    fig = px.imshow(
        pivot,
        text_auto=".1f",
        aspect="auto",
        color_continuous_scale=["#0f172a", "#2dd4bf", "#f97316", "#f43f5e"],
        title=title,
    )
    return apply_theme(fig)


def gauge(value: float, title: str, suffix: str = "%") -> go.Figure:
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            number={"suffix": suffix},
            title={"text": title},
            gauge={
                "axis": {"range": [0, max(100, value * 1.15)]},
                "bar": {"color": "#f97316"},
                "bgcolor": "rgba(255,255,255,0.05)",
                "steps": [
                    {"range": [0, 80], "color": "#11343d"},
                    {"range": [80, 120], "color": "#3b2f1d"},
                    {"range": [120, max(160, value * 1.15)], "color": "#431c2a"},
                ],
            },
        )
    )
    return apply_theme(fig)


def scatter(df: pd.DataFrame, x: str, y: str, title: str, color: str) -> go.Figure:
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        title=title,
        opacity=0.72,
        color_discrete_map=CHURN_COLORS,
        hover_data=["Geography", "Age", "NumOfProducts", "Customer Value Score"],
    )
    return apply_theme(fig)

