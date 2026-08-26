import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))


from sqlalchemy import text
from database_db_core.connection import get_db_engine


def load_balance(balance_df):

    engine = get_db_engine()

    with engine.begin() as conn:

        for _, row in balance_df.iterrows():

            conn.execute(
                text("""
                INSERT INTO corp_fin.fact_balance
                (
                    company_id,
                    period_end,
                    assets,
                    liabilities,
                    equity,
                    cash,
                    inventory,
                    current_assets,
                    current_liabilities,
                    long_term_debt,
                    fiscal_year,
                    fiscal_period,
                    filing_form,
                    filed_date
                )

                VALUES
                (
                    :company_id,
                    :period_end,
                    :assets,
                    :liabilities,
                    :equity,
                    :cash,
                    :inventory,
                    :current_assets,
                    :current_liabilities,
                    :long_term_debt,
                    :fiscal_year,
                    :fiscal_period,
                    :filing_form,
                    :filed_date
                )

                ON CONFLICT
                (
                    company_id,
                    period_end,
                    filed_date
                )
                DO NOTHING;
                """),

                {
                    "company_id": row["company_id"],

                    "period_end": row.get("end"),

                    "assets": row.get("assets"),
                    "liabilities": row.get("liabilities"),
                    "equity": row.get("equity"),
                    "cash": row.get("cash"),
                    "inventory": row.get("inventory"),
                    "current_assets": row.get("current_assets"),
                    "current_liabilities": row.get("current_liabilities"),
                    "long_term_debt": row.get("long_term_debt"),

                    "fiscal_year": row.get("fy"),
                    "fiscal_period": row.get("fp"),
                    "filing_form": row.get("form"),
                    "filed_date": row.get("filed")
                }
            )