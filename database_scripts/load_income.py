from sqlalchemy import text
from database_db_core.connection import get_db_engine
import pandas as pd


def load_income(df):

    engine = get_db_engine()

    with engine.begin() as conn:

        for _, row in df.iterrows():

            conn.execute(
                text("""
                INSERT INTO corp_fin.fact_income
                (
                    company_id,
                    period_start,
                    period_end,
                    revenue,
                    operating_income,
                    net_income,
                    rd_expense,
                    income_tax,
                    fiscal_year,
                    fiscal_period,
                    filing_form,
                    filed_date
                )

                VALUES
                (
                    :company_id,
                    :period_start,
                    :period_end,
                    :revenue,
                    :operating_income,
                    :net_income,
                    :rd_expense,
                    :income_tax,
                    :fiscal_year,
                    :fiscal_period,
                    :filing_form,
                    :filed_date
                )

                ON CONFLICT
                (
                    company_id,
                    period_start,
                    period_end,
                    filed_date
                )
                DO NOTHING;
                """),

                {
                    "company_id": row["company_id"],

                    "period_start": row.get("start"),
                    "period_end": row.get("end"),

                    "revenue": row.get("revenue"),
                    "operating_income": row.get("operating_income"),
                    "net_income": row.get("net_income"),
                    "rd_expense": row.get("rd_expense"),
                    "income_tax": row.get("income_tax"),

                    "fiscal_year": row.get("fy"),
                    "fiscal_period": row.get("fp"),
                    "filing_form": row.get("form"),
                    "filed_date": row.get("filed")
                }
            )