import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from sqlalchemy import text
from database_db_core.connection import get_db_engine

from scripts.transform_cashflow import transform_cashflow


engine = get_db_engine()


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

FROM corp_fin.fact_financials;
"""


df = __import__("pandas").read_sql(
    text(query),
    engine
)


print("Raw cashflow data:")
print(df.head())


cashflow_df = transform_cashflow(df)


print("\nTransformed cashflow:")
print(cashflow_df.head())

from scripts.load_cashflow import load_cashflow

print(cashflow_df.columns)
print(cashflow_df.head())

load_cashflow(cashflow_df)

print("Cashflow data loaded successfully")