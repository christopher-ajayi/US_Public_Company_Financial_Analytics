# Corporate Financial Intelligence Platform

## Project Roadmap

## 1. Project Overview

The Corporate Financial Intelligence Platform is an end-to-end financial data engineering and analytics project designed to collect, transform, store, clean, and analyze corporate financial statement data.

The project uses SEC XBRL financial data to build a structured PostgreSQL database containing company financial statements and prepares the data for financial performance analysis using Python.

---

# Phase 1 — Project Environment Setup

## Completed Tasks

- Created project structure
- Configured Python virtual environment
- Installed required packages
- Connected Python to PostgreSQL
- Configured database connection management

## Technologies Used

- Python
- PostgreSQL
- SQLAlchemy
- pandas
- psycopg2
- VS Code

---

# Phase 2 — Database Design

## Objective

Create a relational database structure capable of storing corporate financial statement data.

## Database Schema

Schema created: corp_fin

## Fact Tables Created

### fact_income

Stores income statement information.

Examples:

- Revenue
- Operating income
- Net income
- Research and development expense
- Income tax


### fact_balance

Stores balance sheet information.

Examples:

- Assets
- Liabilities
- Equity
- Cash
- Inventory
- Debt


### fact_cashflow

Stores cash flow statement information.

Examples:

- Operating cash flow
- Investing cash flow
- Financing cash flow
- Capital expenditure
- Dividends

---

# Phase 3 — Data Extraction

## Objective

Extract corporate financial statement data from SEC XBRL filings.

Collected:

- Income statements
- Balance sheets
- Cash flow statements

Final dataset coverage:

- 50 companies
- Multiple years of annual financial statements

---

# Phase 4 — Data Transformation

## Objective

Convert raw financial data into analytical structures.

Completed transformations:

- Converted XBRL metric data from long format to wide format
- Standardized financial statement variables
- Prepared datasets for database loading

Transformation scripts:

transform_income.py

transform_balance.py

transform_cashflow.py


---

# Phase 5 — Data Loading

## Objective

Load transformed financial statements into PostgreSQL.

Created loading scripts: Loaded tables:

corp_fin.fact_income

corp_fin.fact_balance

corp_fin.fact_cashflow


---

# Phase 6 — Data Cleaning and Validation

## Objective

Create clean analytical datasets.

Problems identified:

- Duplicate company-period records
- Multiple SEC filing contexts
- Restated financial information
- Duplicate joins

Solutions implemented:

- SQL cleaning views
- Window functions
- ROW_NUMBER ranking
- Latest filing selection

---

# Phase 7 — SQL Cleaning Views

Created:

clean_income_view

clean_balance_view

clean_cashflow_view


Purpose:

- Remove duplicate financial records
- Maintain one financial record per company reporting period
- Prepare data for integration

Validation:

All three cleaning views returned: No duplicate company_id + period_end records


---

# Phase 8 — Integrated Financial Dataset

Created: company_financials_view


Purpose: 

Combine: Income Statement + Balance Sheet + Cash Flow Statement


Join keys: compay_id, period_end

Final Validation: 

880 total financial records

50 companies

0 duplicate company-period records

