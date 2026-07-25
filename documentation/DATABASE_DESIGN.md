# Database Design

## Overview

The Corporate Financial Intelligence Platform uses PostgreSQL as the primary data storage system.

The database was designed to store, clean, and integrate corporate financial statement data extracted from SEC XBRL filings.

The database follows a structured approach:
```
            Raw Financial Data
                    ↓
                Fact Tables
                    ↓
              Cleaning Views
                    ↓
         Integrated Analytical View
                    ↓
          Python Financial Analysis
```

---

# Database Schema

## Schema Name
corp_fin
The `corp_fin` schema contains all financial data objects used in the project.

---

# Fact Tables

The project uses three main fact tables.

---

# 1. fact_income

## Purpose

Stores corporate income statement data.

## Key Information Stored

- Revenue
- Operating income
- Net income
- Research and development expenses
- Income taxes

## Example Structure

| Column | Description |
|---|---|
| company_id | Company identifier |
| period_start | Reporting period start date |
| period_end | Reporting period end date |
| revenue | Total revenue |
| operating_income | Operating profit |
| net_income | Earnings after expenses |
| rd_expense | Research and development expense |
| income_tax | Income tax expense |
| fiscal_year | Fiscal reporting year |
| fiscal_period | Annual/quarter period |
| filing_form | SEC filing type |
| filed_date | Filing submission date |

---

# 2. fact_balance

## Purpose

Stores corporate balance sheet information.

## Key Information Stored

- Assets
- Liabilities
- Equity
- Cash
- Inventory
- Debt

## Example Structure

| Column | Description |
|---|---|
| company_id | Company identifier |
| period_end | Balance sheet reporting date |
| assets | Total assets |
| liabilities | Total liabilities |
| equity | Shareholders' equity |
| cash | Cash and equivalents |
| inventory | Inventory value |
| current_assets | Current assets |
| current_liabilities | Current liabilities |
| long_term_debt | Long-term debt |

---

# 3. fact_cashflow

## Purpose

Stores corporate cash flow statement information.

## Key Information Stored

- Operating cash flow
- Investing cash flow
- Financing cash flow
- Capital expenditure
- Dividends

## Example Structure

| Column | Description |
|---|---|
| company_id | Company identifier |
| period_start | Reporting period start |
| period_end | Reporting period end |
| operating_cash_flow | Cash generated from operations |
| investing_cash_flow | Investment-related cash movements |
| financing_cash_flow | Financing activities |
| capital_expenditure | Capital investments |
| dividends_paid | Dividend payments |

---

# Cleaning Views

The database uses SQL views to prepare clean analytical datasets.

---

# 1. clean_income_view

## Purpose

Creates a standardized income statement dataset.

Operations performed:

- Removes duplicate filings
- Keeps one record per company reporting period
- Selects the most recent filing

Technique used:

```sql
ROW_NUMBER()
PARTITION BY company_id, period_end
ORDER BY filed_date DESC
```

---
# 2. clean_balance_view

## Purpose

Creates a clean balance sheet dataset.

Operations performed:

- Removes duplicate balance sheet contexts
- Keeps the latest available filing
- Ensures one balance record per company-period

---

# 3. clean_cashflow_view

## Purpose

Creates a clean cash flow dataset.

Operations performed:

- Removes duplicate cash flow records
- Standardizes annual cash flow information
- Prepares data for integration

---

# Integrated View

## 1. company_financials_view

This is the primary analytical dataset.

It combines: Income Statement + Balance Sheet + Cashflow Statement

## using : company_id, period_end

---

# Final Dataset

## After Cleaning and Integration

```
Companies: 50

Financial observations: 880

Duplicate company-period records: 0
```

---
# Database Design Principles Applied

## The project demonstrates:
```
- Relational database design
- Data normalization
- SQL joins
- View creation
- Data validation
- Duplicate detection
- Window functions
- Analytical data preparation
````