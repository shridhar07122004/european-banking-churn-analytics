# Customer Segmentation & Churn Pattern Analytics

Streamlit dashboard for European banking churn analytics. The project includes data validation, cleaning, feature engineering, KPI calculations, customer segmentation, interactive visualizations, and documentation artifacts for portfolio or academic submission.

## Project Structure

```text
banking-churn-analytics/
|-- app.py
|-- pages/
|-- src/
|-- data/
|-- assets/
|-- docs/
|-- requirements.txt
`-- README.md
```

## Dataset

The app loads this default dataset automatically:

```text
data/European_Bank.csv
```

It also supports `data/Churn_Modelling.csv` as a fallback, or uploading a CSV from the sidebar. The expected standard columns are:

```text
Year, CustomerId, Surname, CreditScore, Geography, Gender, Age,
Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember,
EstimatedSalary, Exited
```

## Run Locally

```powershell
pip install -r requirements.txt
streamlit run app.py
```

## Key KPIs

- Overall churn rate
- Segment churn rate
- High-value churn ratio
- Geographic risk index
- Engagement drop indicator
- Balance exposure from churned customers

## Pages

- Executive Dashboard
- Geography Analysis
- Customer Segmentation
- Customer Behavior
- High Value Customers
- Recommendations
