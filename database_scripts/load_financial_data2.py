from sqlalchemy import text
from database_db_core.connection import get_db_engine


engine = get_db_engine()


def load_financial_data(financial_df, company_id):

    financial_df = financial_df.rename(
        columns={
            "start": "period_start",
            "end": "period_end",
            "val": "value",
            "fy": "fiscal_year",
            "fp": "fiscal_period",
            "form": "filing_form",
            "filed": "filed_date"
        }
    )

    financial_df["company_id"] = company_id


    insert_sql = """
    INSERT INTO corp_fin.fact_financials
    (
        period_start,
        period_end,
        value,
        fiscal_year,
        fiscal_period,
        filing_form,
        filed_date,
        metric,
        company_id
    )

    VALUES
    (
        :period_start,
        :period_end,
        :value,
        :fiscal_year,
        :fiscal_period,
        :filing_form,
        :filed_date,
        :metric,
        :company_id
    )

    ON CONFLICT
    (
        company_id,
        metric,
        COALESCE(period_start, DATE '1900-01-01'),
        COALESCE(period_end, DATE '1900-01-01'),
        filing_form,
        filed_date
    )

    DO NOTHING;
    """


    records = financial_df.to_dict(
        orient="records"
    )


    with engine.begin() as conn:

        conn.execute(
            text(insert_sql),
            records
        )


    print(
        f"{len(records)} financial records processed"
    )