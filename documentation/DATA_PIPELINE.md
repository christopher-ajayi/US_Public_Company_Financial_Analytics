# Data Pipeline Documentation

## Overview

The Corporate Financial Intelligence Platform follows an end-to-end data pipeline that transforms raw SEC XBRL financial statement data into a clean analytical dataset for financial analysis.

The pipeline consists of five major stages:
```
                SEC XBRL Data
                    ↓
    Python Extraction & Transformation
                    ↓
            PostgreSQL Storage
                    ↓
         SQL Cleaning & Integration
                    ↓
          Python Financial Analysis
```


---

# Stage 1 — Data Source

## Source

The project uses corporate financial statement data obtained from SEC XBRL filings.

The extracted financial statements include:

- Income Statement
- Balance Sheet
- Cash Flow Statement

The data contains:

- Company identifiers
- Reporting periods
- Financial metrics
- Filing information
- Fiscal year information

---

# Stage 2 — Data Extraction

## Objective

Extract financial statement information and prepare it for processing.

Extraction tasks include:

- Retrieving company financial facts
- Selecting relevant financial metrics
- Capturing filing metadata

Important metadata collected:

- Filing date
- Fiscal year
- Fiscal period
- Filing form
- Reporting dates

---

# Stage 3 — Python Transformation Layer

## Objective

Convert raw SEC financial data into database-ready structures.

## Transformation Process

Raw XBRL data is initially stored in a long format:

Example: company_id | metric | period | value


The data is transformed into a wide analytical format:

Example: company_id | revenue | net_income | assets | cash_flow


---

## Transformation Scripts
transform_income.py

transform_balance.py

transform_cashflow.py

---

## Transformation Tasks

Performed:

- Metric selection
- Data reshaping
- Column standardization
- Date formatting
- Preparation for database loading

---

# Stage 4 — PostgreSQL Storage Layer

## Objective

Store transformed financial information in relational tables.

The transformed data is loaded into:

---
corp_fin.fact_income

corp_fin.fact_balance

corp_fin.fact_cashflow

---

# Loading Scripts


load_income.py

load_balance.py

load_cashflow.py

---

# Stage 5 — SQL Cleaning Layer

## Objective

Prepare reliable analytical datasets.

Raw fact tables contain multiple SEC filing contexts because companies may:

- Restate information
- File amendments
- Report comparative periods

SQL views were created to remove these issues.

---

# Cleaning Views

## clean_income_view

Purpose:

- Remove duplicate income statement records
- Keep latest filing per company-period


## clean_balance_view

Purpose:

- Remove duplicate balance sheet records
- Maintain one balance snapshot per period


## clean_cashflow_view

Purpose:

- Remove duplicate cash flow records
- Maintain one annual cash flow record per period

---

# Duplicate Resolution Method

The project uses SQL window functions:

```sql
ROW_NUMBER()

Partitioning: company_id, period_end

Ordering: filed_date DESC
```
This keeps the most recent filing version.

# Stage 6 — Data Integration
## Integrated View

Created: company_financials_view

Purpose: Combine all three financial statements.

Structure: 
```

Income Statement
        +
Balance Sheet
        +
Cash Flow Statement
        =
Integrated Financial Dataset
```

Join keys: company_id, period_end

# Stage 7 — Analytical Layer

```
The integrated dataset contains: 50 companies

880 financial observations

0 duplicate company-period records
```