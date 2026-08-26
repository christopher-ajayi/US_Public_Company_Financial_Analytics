import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from sqlalchemy import text
from database_db_core.connection import get_db_engine


def get_company_id(ticker):

    engine = get_db_engine()

    query = text("""
        SELECT company_id
        FROM corp_fin.dim_company
        WHERE ticker = :ticker
    """)

    with engine.connect() as conn:
        result = conn.execute(
            query,
            {"ticker": ticker}
        ).fetchone()

    if result:
        return result[0]

    raise ValueError(f"Company {ticker} not found")