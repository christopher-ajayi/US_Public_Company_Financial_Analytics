import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from sqlalchemy import text
from database_db_core.connection import get_db_engine
from config.companies import COMPANIES


def load_companies():

    engine = get_db_engine()

    with engine.begin() as conn:

        for company in COMPANIES:

            print(company)

            conn.execute(
                text("""
                INSERT INTO corp_fin.dim_company
                (
                    ticker,
                    company_name,
                    cik,
                    sector,
                    industry,
                    country,
                    exchange
                )
                VALUES
                (
                    :ticker,
                    :company_name,
                    :cik,
                    :sector,
                    :industry,
                    :country,
                    :exchange
                )

                ON CONFLICT (ticker)
                DO UPDATE SET
                    company_name = EXCLUDED.company_name,
                    cik = EXCLUDED.cik,
                    sector = EXCLUDED.sector,
                    industry = EXCLUDED.industry,
                    country = EXCLUDED.country,
                    exchange = EXCLUDED.exchange;
                """),
                {
                    "ticker": company["ticker"],
                    "company_name": company["company_name"],
                    "cik": company["cik"],
                    "sector": company["sector"],
                    "industry": company["industry"],
                    "country": company["country"],
                    "exchange": company["exchange"]
                }
            )

    print("Companies loaded successfully")


if __name__ == "__main__":
    load_companies()