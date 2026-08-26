from sqlalchemy import text
from database_db_core.connection import get_db_engine
import pandas as pd


def load_financial_data(df, company_id):

    engine = get_db_engine()

    with engine.begin() as conn:

        for _, row in df.iterrows():

            conn.execute(
                text("""
                INSERT INTO corp_fin.fact_financials
                (
                    company_id,
                    metric,
                    period_start,
                    period_end,
                    value,
                    fiscal_year,
                    fiscal_period,
                    filing_form,
                    filed_date
                )
                VALUES
                (
                    :company_id,
                    :metric,
                    :period_start,
                    :period_end,
                    :value,
                    :fiscal_year,
                    :fiscal_period,
                    :filing_form,
                    :filed_date
                )
                ON CONFLICT DO NOTHING;
                """),
                {
                    "company_id": company_id,
                    "metric": row["metric"],
                    "period_start": row["start"] if pd.notna(row["start"]) else "1900-01-01",
                    "period_end": row["end"] if pd.notna(row["end"]) else "1900-01-01",
                    "value": row["val"],
                    "fiscal_year": None if pd.isna(row["fy"]) else row["fy"],
                    "fiscal_period": None if pd.isna(row["fp"]) else row["fp"],
                    "filing_form": row["form"],
                    "filed_date": row["filed"]
                }
            )