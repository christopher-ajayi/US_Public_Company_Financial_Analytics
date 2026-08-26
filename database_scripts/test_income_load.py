import pandas as pd

from sqlalchemy import text
from database_db_core.connection import get_db_engine

from transform_income import transform_income
from load_income import load_income


engine = get_db_engine()


# Pull raw financial data
query = """
SELECT
    company_id,
    metric,
    period_start AS start,
    period_end AS end,
    value AS val,
    fiscal_year AS fy,
    fiscal_period AS fp,
    filing_form AS form,
    filed_date AS filed
FROM corp_fin.fact_financials
WHERE metric IN
(
    'revenue',
    'operating_income',
    'net_income',
    'rd_expense',
    'income_tax'
);
"""


df = pd.read_sql(query, engine)


print("Raw data:")
print(df.head())


# Transform
income_df = transform_income(df)


print("\nTransformed income:")
print(income_df.head())


# Load
load_income(income_df)
print(income_df.columns)
print(income_df.head())


print("\nIncome data loaded successfully")