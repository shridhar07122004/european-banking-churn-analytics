---
title: European Banking Churn Analytics
emoji: 📊
colorFrom: teal
colorTo: blue
sdk: streamlit
sdk_version: 1.57.0
app_file: app.py
pinned: false
---

# Customer Segmentation & Churn Pattern Analytics in European Banking

An end-to-end data analytics project that studies customer churn patterns in a European banking dataset. The project combines data cleaning, feature engineering, KPI design, customer segmentation, and an interactive Streamlit dashboard to help identify high-risk customer groups and support retention strategy decisions.

This project was prepared as a portfolio and internship-style analytics submission, with emphasis on clear business interpretation, reproducible code, and deployable dashboard output.

## Project Objective

Banks lose revenue and long-term relationship value when customers leave. The objective of this project is to analyze customer churn behavior across demographic, geographic, financial, and behavioral dimensions, then convert the findings into actionable retention recommendations.

The dashboard helps answer questions such as:

- What is the overall churn rate?
- Which countries show the highest churn risk?
- Which age, credit score, tenure, salary, and balance segments are most vulnerable?
- Are inactive customers more likely to churn?
- How much customer balance is exposed among churned customers?
- Which high-value customers need retention priority?

## Problem Statement

Customer churn is a major challenge in retail banking. A bank needs to understand which customer segments are leaving, what patterns are associated with churn, and where retention efforts should be focused. This project builds an analytics dashboard for European banking customers to reveal churn patterns and support data-driven business decisions.

## Dataset

The project uses a European banking customer churn dataset with 10,000 customer records.

Default dataset path:

```text
data/European_Bank.csv
```

Main columns used:

```text
Year, CustomerId, Surname, CreditScore, Geography, Gender, Age,
Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember,
EstimatedSalary, Exited
```

Target column:

```text
Exited
```

`Exited = 1` means the customer churned.  
`Exited = 0` means the customer was retained.

## Key Features

- Automated CSV loading and validation
- Data cleaning and duplicate handling
- Feature engineering for customer segmentation
- KPI calculation engine
- Reusable Plotly chart factory
- Multi-page Streamlit dashboard
- Sidebar filters for geography, gender, and age
- High-value customer analysis
- Strategic recommendations page
- Ready for Streamlit Community Cloud deployment

## Customer Segments Created

- Age Segment: `<30`, `30-45`, `46-60`, `>60`
- Credit Score Band: `Low`, `Medium`, `High`
- Tenure Group: `New`, `Mid-Term`, `Long-Term`
- Balance Segment: `Zero`, `Low`, `High`
- Salary Segment: `Low`, `Medium`, `High`
- Value Tier: `Bronze`, `Silver`, `Gold`, `Premium`

## KPI Framework

| KPI | Formula / Meaning |
| --- | --- |
| Overall Churn Rate | Churned customers / Total customers * 100 |
| Segment Churn Rate | Churned customers in segment / Total customers in segment * 100 |
| High-Value Churn Ratio | Churned premium customers / Total premium customers * 100 |
| Geographic Risk Index | Country churn rate / Overall churn rate * 100 |
| Engagement Drop Indicator | Inactive churned customers / Total inactive customers * 100 |
| Balance Exposure | Sum of balances for churned customers |

Note: Balance exposure is used as a business risk proxy. It is not the same as actual revenue unless revenue or profitability data is available.

## Dashboard Pages

### 1. Executive Dashboard

Displays overall churn KPIs, churn composition, country churn comparison, and top risk segments.

### 2. Geography Analysis

Analyzes churn by country, geographic risk index, and country-age interaction patterns.

### 3. Customer Segmentation

Compares churn across age groups, credit score bands, balance segments, tenure groups, and value tiers.

### 4. Customer Behavior

Studies churn patterns based on active membership, product ownership, and credit card ownership.

### 5. High Value Customers

Identifies premium customers and analyzes high-value churn risk, balance exposure, and salary-balance patterns.

### 6. Recommendations

Summarizes key findings and provides strategic retention actions for high-risk customer groups.

## Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- Git and GitHub

## Project Structure

```text
european-banking-churn-analytics/
|-- app.py
|-- requirements.txt
|-- README.md
|-- .streamlit/
|   `-- config.toml
|-- assets/
|   `-- style.css
|-- data/
|   `-- European_Bank.csv
|-- docs/
|   |-- executive_summary.md
|   |-- research_paper.md
|   |-- resume_description.md
|   `-- viva_questions.md
|-- pages/
|   |-- 1_Executive_Dashboard.py
|   |-- 2_Geography_Analysis.py
|   |-- 3_Customer_Segmentation.py
|   |-- 4_Customer_Behavior.py
|   |-- 5_High_Value_Customers.py
|   `-- 6_Recommendations.py
`-- src/
    |-- app_state.py
    |-- chart_factory.py
    |-- data_cleaner.py
    |-- data_loader.py
    |-- feature_engineer.py
    `-- kpi_engine.py
```

## Installation and Local Run

Clone the repository:

```powershell
git clone https://github.com/shridhar07122004/european-banking-churn-analytics.git
cd european-banking-churn-analytics
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the Streamlit app:

```powershell
python -m streamlit run app.py
```

The app will open at:

```text
http://localhost:8501
```

## Live Demo

View the deployed Streamlit dashboard here:

[https://european-bankingchurnanalytics.streamlit.app/](https://european-bankingchurnanalytics.streamlit.app/)

## Business Insights Supported

The dashboard is designed to help banking teams:

- Identify high-risk customer groups
- Prioritize retention campaigns
- Compare churn risk across geographies
- Detect engagement-related churn patterns
- Monitor high-value customer risk
- Translate analytics into business recommendations

## Future Enhancements

- Add machine learning churn prediction
- Add model explainability using feature importance
- Add downloadable filtered reports
- Add campaign simulation for retention strategies
- Add customer-level churn risk scoring
- Add authentication for business users

## Author

Shridhar Kalasgonda

GitHub: [shridhar07122004](https://github.com/shridhar07122004)
