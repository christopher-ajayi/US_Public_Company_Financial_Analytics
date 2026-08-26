import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from sqlalchemy import text
from database_db_core.connection import get_db_engine

from scripts.transform_balance import transform_balance


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

df = __import__("pandas").read_sql(text(query), engine)

print("Raw balance data:")
print(df.head())

balance_df = transform_balance(df)

print("\nTransformed balance:")
print(balance_df.head())

from scripts.load_balance import load_balance

load_balance(balance_df)

print("Balance data loaded successfully")