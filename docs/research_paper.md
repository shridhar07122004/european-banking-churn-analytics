# Customer Segmentation and Churn Pattern Analytics in European Banking

## Abstract

Customer churn is a major challenge in retail banking because acquiring new customers is often more expensive than retaining existing ones. This project develops an interactive analytics dashboard to study churn patterns across demographic, geographic, financial, and behavioral dimensions.

## Introduction

Banks require timely insight into churn drivers so they can prioritize retention resources. This project uses a structured dashboard and KPI framework to convert raw customer records into actionable business intelligence.

## Literature Review

Customer churn analysis commonly uses demographic profiling, product usage analysis, customer value segmentation, and behavioral indicators. Prior studies show that engagement, geography, tenure, and financial value can all influence retention risk.

## Methodology

The dataset is cleaned by removing non-analytical identifiers, handling missing values, normalizing binary fields, and removing duplicates. Feature engineering creates age segments, credit score bands, tenure groups, balance segments, salary segments, and a composite customer value score. Churn KPIs are calculated globally and by segment.

## Results

The dashboard presents churn distribution, country-level risk, segment churn rates, customer behavior patterns, high-value customer exposure, and strategic recommendations. Actual values depend on the uploaded dataset and active dashboard filters.

## Discussion

The approach emphasizes interpretability and business usability. Balance exposure is used as a practical proxy for revenue risk, but it should not be interpreted as actual revenue without income, margin, or product profitability data.

## Conclusion

The project provides a complete analytics workflow for banking churn exploration. It can be extended with predictive modeling, customer lifetime value, campaign tracking, and deployment to Streamlit Community Cloud.

