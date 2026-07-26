# Corporate Financial Intelligence Platform

## Overview

The Corporate Financial Intelligence Platform is an end-to-end data analytics project that transforms corporate financial statement data into actionable financial insights.

The project builds a complete data pipeline that extracts, transforms, stores, cleans, and analyzes company financial information using Python, SQL, and PostgreSQL.

The final objective is to evaluate corporate financial performance, financial health, and business trends across multiple companies using standardized financial metrics.

---

# Business Problem

Companies generate large amounts of financial statement data through annual filings, but raw financial information is often difficult to analyze because it is:

- Distributed across different financial statements
- Reported using different accounting contexts
- Containing duplicate filings and restated information
- Difficult to compare across companies and time periods

This project addresses the following question:

> How can raw corporate financial statement data be transformed into a reliable analytical dataset that enables meaningful comparison of company performance and financial health?

---

# Project Objectives

The project aims to:

1. Build a structured financial database from SEC XBRL financial data.

2. Clean and standardize corporate financial statements.

3. Integrate income statements, balance sheets, and cash flow statements into a unified analytical dataset.

4. Develop financial metrics to evaluate:

   - Profitability
   - Liquidity
   - Solvency
   - Operational efficiency
   - Cash generation

5. Identify trends and differences in corporate financial performance over time.

---

# Data Scope

The project analyzes financial statement data from:

- 50 publicly listed companies

Current integrated dataset:

- 880 company-period observations

Financial statements included:

## Income Statement

Examples: Revenue, Operating income and Net income.


## Balance Sheet

Examples: Assets, Liabilities, Equity, Cash and Debt.


## Cash Flow Statement

Examples: Operating cash flow, Investing cash flow, Financing cash flow, and Capital expenditure.

---

# Technical Architecture
```
            SEC XBRL Financial Data
                     ↓
       Python Extraction & Transformation
                     ↓
            PostgreSQL Database
                     ↓
             SQL Cleaning Views
                     ↓
          Integrated Financial Dataset
                     ↓
            Python Financial Analysis
                     ↓
            Visualization & Insights
```

---

# Technology Stack

## Data Engineering

- PostgreSQL
- SQL
- SQL Views
- Window Functions

## Programming

- Python
- pandas
- SQLAlchemy

## Development

- VS Code
- Git/GitHub

## Visualization
- Power BI
---

# Database Design

The project uses the `corp_fin` PostgreSQL schema.

Please see  [DATABASE_DESIGN.md](/docs/DATABASE_DESIGN.md/)


---

# Analytical Questions

The analysis phase will answer questions such as:

## Profitability

- Which companies show consistent revenue growth?
- Which companies maintain strong profit margins?
- Which companies generate higher returns on assets and equity?


## Financial Health

- Which companies maintain strong liquidity?
- Which companies carry higher debt levels?
- How does financial structure differ across companies?


## Cash Generation

- Which companies generate strong operating cash flows?
- Are companies converting earnings into cash?
- How are companies allocating capital?


## Trends

- How has company performance changed over time?
- Which companies improved or deteriorated financially?

---

# Project Status

## Completed

✅ Database design  
✅ Data extraction  
✅ Data transformation  
✅ PostgreSQL loading  
✅ SQL cleaning layer  
✅ Financial data integration  
✅ Exploratory data analysis  
✅ Financial ratio calculation  
✅ Company comparison  
✅ Trend analysis  
✅ Visualization  
✅ Business insights    

## Current Phase

Financial Analytics

Upcoming work:



---

# Project Deliverables

Final outputs will include:

- PostgreSQL database design
- SQL scripts
- Python analysis notebook
- Financial performance metrics
- Visualizations
- Analytical conclusions

---
## Key Findings
- Visa emerged as the strongest performer in terms of profitability, recording the highest average operating margin (64.2%) and net profit margin (51.8%), demonstrating exceptional operational efficiency and earnings generation.
- Microsoft, Apple, Amazon, Alphabet, and Meta consistently ranked among the top-performing companies in revenue generation and operating cash flow, reflecting sustained financial growth and strong cash-generating capabilities over the reporting period.
- NVIDIA demonstrated the strongest liquidity position, achieving the highest average current ratio (4.44) while also maintaining one of the highest profitability levels, indicating both financial resilience and efficient operations.
- Liquidity and capital structure varied considerably across companies, with current ratios ranging from 0.66 to 4.44 and debt-to-equity ratios highlighting different financing strategies among firms.
-Trend analysis revealed sustained long-term revenue growth among leading technology companies, particularly Microsoft, Apple, Amazon, Alphabet, and Meta, reinforcing the sector's dominant financial performance throughout the analysis period.

---

**Data Limitations:**
 - The dataset contains significant missing values across several financial metrics
 - Revenue data is incomplete, with approximately 28% of observations missing, limiting some revenue trend and profitability analysis.
 - Key profitability variables such as net income and operating income contain substantial missing observations, which may affect margin calculations.
 - Cash flow variables (operating, investing, and financing cash flows) have high levels of missing data, limiting comprehensive cash flow analysis.
 - Missing values are not manually imputed because the objective is to analyze reported financial information rather than estimate unavailable disclosures.
 - Financial metrics will therefore be calculated only where sufficient data exists and interpreted with consideration of data availability.

Therfore, results should be interpreted with caution due to incomplete availability of certain financial metrics across reporting periods.

---

# Repository Structure


```
US_Public_Company_Financial_Analytics/
├── csv_files
├── documentation/
├── graphs/
├── notebooks/
├── power_bi_dashboard/
├── sql/
├── README.md
├── requirements.txt
└── .gitignore
```


---

# Future Improvements

Potential improvements for this project include:

- Expand analysis to include additional companies

---

# Author

Christopher Ajayi