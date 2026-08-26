import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

import pandas as pd
from sqlalchemy import text

from database_db_core.connection import get_db_engine


engine = get_db_engine()


income = pd.read_sql(
    text("""
    SELECT
        company_id,
        fiscal_year,
        period_start,
        period_end,
        revenue,
        operating_income,
        net_income,
        rd_expense,
        income_tax
    FROM corp_fin.fact_income
    """),
    engine
)


balance = pd.read_sql(
    text("""
    SELECT
        company_id,
        fiscal_year,
        assets,
        liabilities,
        equity,
        cash,
        inventory,
        current_assets,
        current_liabilities,
        long_term_debt
    FROM corp_fin.fact_balance
    """),
    engine
)


cashflow = pd.read_sql(
    text("""
    SELECT
        company_id,
        fiscal_year,
        operating_cash_flow,
        investing_cash_flow,
        financing_cash_flow,
        capital_expenditure,
        dividends_paid
    FROM corp_fin.fact_cashflow
    """),
    engine
)

financials = (
    income
    .merge(
        balance,
        on=[
            "company_id",
            "fiscal_year"
        ],
        how="outer"
    )
    .merge(
        cashflow,
        on=[
            "company_id",
            "fiscal_year"
        ],
        how="outer"
    )
)

print(financials.head())
print(financials.shape)