from sqlalchemy import text
from database_db_core.connection import get_db_engine


def load_cashflow(df):

    engine = get_db_engine()

    with engine.begin() as conn:

        for _, row in df.iterrows():

            conn.execute(
                text("""
                INSERT INTO corp_fin.fact_cashflow
                (
                    company_id,
                    period_start,
                    period_end,
                    operating_cash_flow,
                    investing_cash_flow,
                    financing_cash_flow,
                    capital_expenditure,
                    dividends_paid,
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
                    :operating_cash_flow,
                    :investing_cash_flow,
                    :financing_cash_flow,
                    :capital_expenditure,
                    :dividends_paid,
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

                    "operating_cash_flow": row.get("operating_cash_flow"),
                    "investing_cash_flow": row.get("investing_cash_flow"),
                    "financing_cash_flow": row.get("financing_cash_flow"),
                    "capital_expenditure": row.get("capital_expenditure"),
                    "dividends_paid": row.get("dividends_paid"),

                    "fiscal_year": row.get("fy"),
                    "fiscal_period": row.get("fp"),
                    "filing_form": row.get("form"),
                    "filed_date": row.get("filed")
                }
            )