from sqlalchemy import text
from database_db_core.connection import get_db_engine


def get_company_id(ticker):

    engine = get_db_engine()

    with engine.connect() as conn:

        result = conn.execute(
            text("""
            SELECT company_id
            FROM corp_fin.dim_company
            WHERE ticker = :ticker
            """),
            {
                "ticker": ticker
            }
        )

        company = result.fetchone()

        if company is None:
            raise ValueError(
                f"{ticker} not found in dim_company"
            )

        return company[0]