# Customer Segmentation and Churn Pattern Analytics in European Banking

**Author:** Shridhar Kalasgonda  
**Project Type:** Banking Analytics and Business Intelligence  
**Tools Used:** Python, Pandas, Streamlit, Plotly  

## Abstract

Customer churn is a critical challenge in retail banking because customer acquisition is generally more expensive than customer retention, and churn can reduce both deposit stability and long-term relationship value. This study presents an end-to-end analytical framework for understanding customer churn patterns in a European banking dataset containing 10,000 customer records. The work focuses on descriptive analytics, customer segmentation, KPI development, and business intelligence dashboarding rather than black-box prediction. The dataset was cleaned, validated, and transformed into analytical customer segments based on age, credit score, tenure, balance, salary, engagement status, and customer value tier. The analysis found an overall churn rate of 20.37%. Germany showed the highest country-level churn rate at 32.44%, with a geographic risk index of 159.25 relative to the overall churn rate. Customers aged 46-60 showed the highest age-segment churn rate at 51.12%, while inactive customers churned at 26.85% compared with 14.27% for active customers. Premium value-tier customers showed a churn rate of 25.76%, representing USD 83.10 million in balance exposure. These findings demonstrate the practical value of interpretable segmentation and KPI dashboards for banking retention strategy. The final output is a deployed Streamlit dashboard that allows interactive exploration of churn risk and provides strategic recommendations for customer retention.

**Keywords:** Customer churn, banking analytics, customer segmentation, Streamlit dashboard, business intelligence, retention strategy, KPI analysis.

## 1. Introduction

Retail banks operate in a competitive environment where customers can move deposits, salary accounts, cards, and product relationships between institutions with increasing ease. In this context, customer churn is not only a marketing concern but also a risk to relationship value, balance stability, and future product revenue. A customer who exits may take away current account balances, future lending opportunities, card usage, and referral value. For this reason, churn analytics has become an important area of banking business intelligence.

Traditional churn studies often focus on predictive modeling, where machine learning algorithms estimate the probability that a customer will leave. Predictive models are useful, but banks also require interpretable dashboards that explain which customer groups are at risk and why they deserve attention. A manager may not only ask, "Who is likely to churn?" but also "Which customer segment is driving churn?", "Which country requires intervention?", and "What type of retention action should be prioritized?" This project addresses those business questions using structured descriptive analytics.

The main objective of this project is to build a customer segmentation and churn pattern analytics system for European banking data. The system includes data cleaning, feature engineering, KPI calculations, visual analytics, and business recommendations. The solution is implemented as an interactive Streamlit dashboard with multiple pages covering executive KPIs, geography analysis, customer segmentation, behavior analysis, high-value customers, and retention recommendations.

## 2. Problem Statement

The problem addressed in this project is the need to identify churn patterns in a European banking customer base and translate them into business insights. The dataset contains demographic, financial, product, and behavior variables, including geography, gender, age, tenure, account balance, number of products, credit card ownership, active membership status, estimated salary, and churn status.

The project aims to answer the following research and business questions:

1. What is the overall churn rate in the customer base?
2. Which geographic market has the highest churn risk?
3. Which customer segments show the strongest churn tendency?
4. How does engagement status influence churn?
5. Are high-value customers exposed to meaningful churn risk?
6. What retention actions should the bank prioritize?

## 3. Objectives

The objectives of the study are:

- To clean and validate the European banking customer dataset.
- To engineer interpretable customer segments for churn analysis.
- To calculate churn-related KPIs for the full customer base and selected segments.
- To identify high-risk segments across geography, age, credit score, balance, salary, tenure, engagement, and value tier.
- To estimate balance exposure among churned customers.
- To develop a Streamlit dashboard for interactive business intelligence.
- To provide practical recommendations for customer retention strategy.

## 4. Literature Review

Customer churn management has been widely studied in service industries because retention is closely related to profitability and long-term customer value. Reichheld and Sasser emphasized the business importance of reducing defections in service organizations and connected service quality measurement with customer retention outcomes. Their work established a managerial foundation for churn-focused performance monitoring.

Hadden, Tiwari, Roy, and Ruta reviewed computer-assisted churn management techniques and highlighted the need for systematic churn management platforms. Their study positioned churn management as an integrated process involving data, customer identification, and retention action. This is relevant to the present project because the dashboard is designed not only to report churn but also to support business action.

Verbeke, Martens, Mues, and Baesens argued that churn models should be comprehensible and useful for business decision-making. While advanced models can improve accuracy, interpretable patterns are important for managers who must design and justify retention strategies. This project follows that principle by focusing on transparent segmentation and KPIs rather than relying only on predictive scores.

Overall, the literature supports three ideas that guide this project: customer retention has strong business value, churn management should be systematic and data-driven, and analytical outputs should remain understandable for decision-makers.

## 5. Dataset Description

The dataset used in this project contains 10,000 customer records from a European banking context. Each record represents a customer and includes profile, account, and churn-related fields.

### 5.1 Dataset Fields

| Field | Description |
|---|---|
| Year | Reporting or observation year |
| CustomerId | Unique customer identifier |
| Surname | Customer surname |
| CreditScore | Customer credit score |
| Geography | Customer country |
| Gender | Customer gender |
| Age | Customer age |
| Tenure | Years associated with the bank |
| Balance | Customer account balance |
| NumOfProducts | Number of bank products used |
| HasCrCard | Credit card ownership indicator |
| IsActiveMember | Active membership indicator |
| EstimatedSalary | Estimated annual salary |
| Exited | Churn indicator |

The target variable is `Exited`, where `1` indicates a churned customer and `0` indicates a retained customer.

### 5.2 Data Validation

The dataset contained 10,000 rows and 14 columns. No missing required columns were found. No missing values or duplicate records were detected during validation. Binary fields such as `HasCrCard`, `IsActiveMember`, and `Exited` were checked to ensure that they contained valid 0/1 values.

## 6. Methodology

The methodology follows a structured analytics pipeline consisting of data ingestion, cleaning, feature engineering, KPI calculation, visualization, and interpretation.

### 6.1 Data Cleaning

Non-analytical identifier fields such as `CustomerId` and `Surname` were removed from the analytical workflow because they do not directly contribute to segment-level churn interpretation. Duplicate records were removed if present. Numeric fields were converted to appropriate numeric types, and binary variables were normalized to 0/1 values.

### 6.2 Feature Engineering

To make the analysis interpretable for business users, continuous variables were transformed into meaningful segments:

| Feature | Segment Logic |
|---|---|
| Age Segment | `<30`, `30-45`, `46-60`, `>60` |
| Credit Score Band | Low `<580`, Medium `580-700`, High `>700` |
| Tenure Group | New `0-2`, Mid-Term `3-6`, Long-Term `7-10` |
| Balance Segment | Zero `0`, Low `<50,000`, High `>=50,000` |
| Salary Segment | Low `<50,000`, Medium `50,000-100,000`, High `>100,000` |
| Value Tier | Bronze, Silver, Gold, Premium |

The customer value score was created as a composite indicator using balance, estimated salary, and number of products. Customers were then divided into quartile-based value tiers. This allowed the project to identify whether higher-value customers were also exposed to churn risk.

### 6.3 KPI Calculation

The dashboard uses the following KPI formulas:

| KPI | Formula |
|---|---|
| Overall Churn Rate | Churned Customers / Total Customers * 100 |
| Segment Churn Rate | Churned Customers in Segment / Total Customers in Segment * 100 |
| Geographic Risk Index | Country Churn Rate / Overall Churn Rate * 100 |
| High-Value Churn Ratio | Churned Premium Customers / Total Premium Customers * 100 |
| Engagement Drop Indicator | Inactive Churned Customers / Total Inactive Customers * 100 |
| Balance Exposure | Sum of Balance for Churned Customers |

Balance exposure is treated as a risk proxy. It should not be interpreted as actual revenue unless profitability, interest margin, or product income data is available.

### 6.4 Dashboard Development

The analytical solution was implemented in Streamlit. The dashboard is divided into six pages:

1. Executive Dashboard
2. Geography Analysis
3. Customer Segmentation
4. Customer Behavior
5. High Value Customers
6. Recommendations

Plotly was used to create interactive bar charts, donut charts, heatmaps, gauges, and scatter plots. Sidebar filters allow users to filter by geography, gender, and age range.

## 7. Results and Analysis

### 7.1 Overall Churn Performance

The dataset contains 10,000 customers, of which 2,037 customers churned. The overall churn rate is therefore 20.37%. This means that approximately one in five customers in the dataset exited the bank.

| Metric | Value |
|---|---:|
| Total Customers | 10,000 |
| Churned Customers | 2,037 |
| Retained Customers | 7,963 |
| Overall Churn Rate | 20.37% |
| Balance Exposure | USD 185,588,094.63 |
| Average Customer Value Score | 34.77 |

### 7.2 Geographic Churn Analysis

Germany shows the highest churn rate among the three countries. Germany has a churn rate of 32.44%, compared with 16.67% in Spain and 16.15% in France. Germany's geographic risk index is 159.25, meaning its churn rate is about 59% higher than the overall churn rate.

| Geography | Customers | Churned | Churn Rate | Geographic Risk Index | Balance Exposure |
|---|---:|---:|---:|---:|---:|
| Germany | 2,509 | 814 | 32.44% | 159.25 | USD 97,973,915.53 |
| Spain | 2,477 | 413 | 16.67% | 81.84 | USD 29,948,014.56 |
| France | 5,014 | 810 | 16.15% | 79.28 | USD 57,666,164.54 |

This result suggests that geography is a major differentiating factor in customer churn. Germany should be considered a priority market for further investigation into customer satisfaction, pricing, product fit, and service quality.

### 7.3 Gender-Based Churn Analysis

Female customers show a higher churn rate than male customers. Female customers have a churn rate of 25.07%, while male customers have a churn rate of 16.46%.

| Gender | Customers | Churned | Churn Rate | Balance Exposure |
|---|---:|---:|---:|---:|
| Female | 4,543 | 1,139 | 25.07% | USD 101,412,732.23 |
| Male | 5,457 | 898 | 16.46% | USD 84,175,362.40 |

This does not prove that gender itself causes churn, but it identifies a segment where further service and product behavior analysis may be valuable.

### 7.4 Age Segment Analysis

Age is one of the strongest churn differentiators. Customers aged 46-60 have a churn rate of 51.12%, which is more than twice the overall churn rate. Customers under 30 have the lowest churn rate at 7.56%.

| Age Segment | Customers | Churned | Churn Rate | Balance Exposure |
|---|---:|---:|---:|---:|
| 46-60 | 1,647 | 842 | 51.12% | USD 75,172,453.58 |
| >60 | 464 | 115 | 24.78% | USD 10,567,926.89 |
| 30-45 | 6,248 | 956 | 15.30% | USD 87,399,241.03 |
| <30 | 1,641 | 124 | 7.56% | USD 12,448,473.13 |

The 46-60 group should be considered a key retention segment. Customers in this age group may have more complex financial needs and may be more sensitive to service quality, advisory relationships, fees, and competing banking offers.

### 7.5 Engagement Analysis

Customer activity is strongly associated with churn. Inactive customers show a churn rate of 26.85%, while active customers show a churn rate of 14.27%.

| Engagement Status | Customers | Churned | Churn Rate | Balance Exposure |
|---|---:|---:|---:|---:|
| Inactive | 4,849 | 1,302 | 26.85% | USD 118,467,426.82 |
| Active | 5,151 | 735 | 14.27% | USD 67,120,667.81 |

This finding supports the business importance of engagement programs. Customers who are not actively interacting with the bank may be less attached to the relationship and more likely to leave.

### 7.6 Product Ownership Analysis

Product count shows a nonlinear relationship with churn. Customers with two products have the lowest churn rate at 7.58%, while customers with three or four products show very high churn rates.

| Number of Products | Customers | Churned | Churn Rate | Balance Exposure |
|---|---:|---:|---:|---:|
| 4 | 60 | 60 | 100.00% | USD 5,623,988.10 |
| 3 | 266 | 220 | 82.71% | USD 18,887,679.16 |
| 1 | 5,084 | 1,409 | 27.71% | USD 129,668,607.08 |
| 2 | 4,590 | 348 | 7.58% | USD 31,407,820.29 |

The extremely high churn rate among customers with three or four products may indicate dissatisfaction, unsuitable product bundling, or other product management issues. However, the four-product group contains only 60 customers, so it should be interpreted carefully.

### 7.7 High-Value Customer Analysis

Premium customers represent the top value tier based on the composite customer value score. This group contains 2,500 customers and has a churn rate of 25.76%. Premium churn creates a balance exposure of USD 83,099,334.07.

| Value Tier | Customers | Churned | Churn Rate | Balance Exposure |
|---|---:|---:|---:|---:|
| Premium | 2,500 | 644 | 25.76% | USD 83,099,334.07 |
| Silver | 2,500 | 493 | 19.72% | USD 37,463,247.14 |
| Gold | 2,500 | 493 | 19.72% | USD 53,843,292.39 |
| Bronze | 2,500 | 407 | 16.28% | USD 11,182,221.03 |

Premium churn is especially important because it combines a high churn rate with high financial exposure. The bank should prioritize high-value retention actions, such as relationship manager review, personalized offers, and proactive service recovery.

## 8. Discussion

The analysis shows that churn is not evenly distributed across the customer base. Instead, churn is concentrated in specific geographies, age groups, engagement categories, and value tiers. Germany, customers aged 46-60, inactive customers, customers with three or four products, and premium-tier customers emerge as key areas of concern.

The findings also show why segment-level analytics is useful. The overall churn rate of 20.37% gives a broad view, but it hides high-risk pockets such as the 51.12% churn rate among customers aged 46-60 and the 32.44% churn rate in Germany. Similarly, inactive customers churn at nearly twice the rate of active customers. These differences can guide targeted retention strategies instead of broad, expensive campaigns.

From a business intelligence perspective, the Streamlit dashboard improves usability by allowing decision-makers to filter the data and inspect patterns interactively. This supports both executive-level monitoring and operational analysis.

## 9. Recommendations

Based on the results, the following recommendations are proposed:

### 9.1 Prioritize Germany for Market-Level Diagnosis

Germany has the highest churn rate and the highest geographic risk index. The bank should investigate country-specific drivers such as service issues, fees, product competitiveness, digital experience, and customer support quality.

### 9.2 Build a Retention Program for Customers Aged 46-60

The 46-60 age group shows the highest churn rate. Retention actions may include advisory check-ins, wealth planning offers, relationship manager contact, and service quality review.

### 9.3 Reactivate Inactive Customers

Inactive customers represent a major churn risk. The bank should design reactivation campaigns using digital nudges, personalized offers, product usage reminders, and service outreach.

### 9.4 Protect Premium Customers

Premium customers contribute the largest balance exposure among value tiers. The bank should create a premium retention list and monitor high-balance churn risk through relationship managers or priority service teams.

### 9.5 Review Product Bundling Strategy

Customers with three or four products show unusually high churn. The bank should examine whether these customers are experiencing product complexity, fees, dissatisfaction, or inappropriate cross-selling.

## 10. Limitations

This study has several limitations:

- The project is based on descriptive analytics and does not prove causality.
- The dataset does not include transaction frequency, complaint history, digital login activity, branch visits, or customer satisfaction scores.
- Balance exposure is used as a proxy for financial risk but does not represent actual revenue or profit.
- The dataset does not contain detailed time-series behavior, so tenure analysis should not be interpreted as a true monthly or yearly churn trend.
- The dashboard does not currently include machine learning churn prediction.

## 11. Future Scope

Future improvements could include:

- Building a predictive churn model using logistic regression, random forest, XGBoost, or other classification methods.
- Adding explainability through feature importance or SHAP analysis.
- Including customer lifetime value and profitability metrics.
- Adding campaign tracking to measure retention intervention effectiveness.
- Adding transaction-level and digital engagement data.
- Creating customer-level churn risk scores for operational use.

## 12. Conclusion

This project developed a complete customer segmentation and churn pattern analytics system for European banking data. The analysis found an overall churn rate of 20.37%, with significantly higher risk in Germany, customers aged 46-60, inactive customers, and premium-value customers. The project demonstrates that interpretable segmentation and KPI dashboards can help banks move from raw customer data to practical retention strategy.

The Streamlit dashboard provides a usable business intelligence interface for exploring churn patterns and communicating findings. Although the project does not yet include predictive modeling, it establishes a strong foundation for data-driven churn management and can be extended into advanced machine learning and campaign optimization.

## References

1. Reichheld, F. F., and Sasser, W. E. Jr. (1990). Zero Defections: Quality Comes to Services. Harvard Business Review, 68(5), 105-111.
2. Hadden, J., Tiwari, A., Roy, R., and Ruta, D. (2007). Computer Assisted Customer Churn Management: State-of-the-Art and Future Trends. Computers and Operations Research, 34(10), 2902-2917.
3. Verbeke, W., Martens, D., Mues, C., and Baesens, B. (2011). Building Comprehensible Customer Churn Prediction Models with Advanced Rule Induction Techniques. Expert Systems with Applications, 38(3), 2354-2364.
4. McKinney, W. (2010). Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference.
5. Streamlit documentation. Streamlit: A faster way to build and share data apps. https://docs.streamlit.io/

## Appendix A: Project Implementation Modules

| Module | Purpose |
|---|---|
| `data_loader.py` | Loads CSV data and validates required columns |
| `data_cleaner.py` | Cleans data, removes non-analytical identifiers, and normalizes fields |
| `feature_engineer.py` | Creates customer segments and value tiers |
| `kpi_engine.py` | Calculates churn KPIs and risk indicators |
| `chart_factory.py` | Builds reusable Plotly charts |
| `app_state.py` | Manages shared Streamlit page layout, filters, and data loading |

## Appendix B: Dashboard Pages

| Page | Purpose |
|---|---|
| Executive Dashboard | Overall KPIs and top risk segments |
| Geography Analysis | Country-level churn and geographic risk index |
| Customer Segmentation | Age, credit, balance, tenure, and value-tier churn |
| Customer Behavior | Engagement, credit card, and product ownership patterns |
| High Value Customers | Premium customer churn and balance exposure |
| Recommendations | Strategic retention actions |
