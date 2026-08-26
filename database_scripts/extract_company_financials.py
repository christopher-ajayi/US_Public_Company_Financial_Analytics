import os
import requests
from pathlib import Path
from dotenv import load_dotenv

from scripts.transform_financial_data import transform_financial_data
from scripts.load_financial_data import load_financial_data
from scripts.company_lookup import get_company_id


BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env", override=True)

SEC_USER_AGENT = os.getenv("SEC_USER_AGENT")

headers = {
    "User-Agent": SEC_USER_AGENT
}


def extract_company_financials(ticker, cik):

    company_id = get_company_id(ticker)

    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

    response = requests.get(url, headers=headers)

    print(f"\nProcessing {ticker}...")
    print("Status Code:", response.status_code)

    response.raise_for_status()

    data = response.json()

    print("Company:", data["entityName"])

    facts = data["facts"]["us-gaap"]

    financial_df = transform_financial_data(facts)

    print(financial_df.head(20))

    load_financial_data(
        financial_df,
        company_id
    )

    print(f"{ticker} financial data loaded successfully")


if __name__ == "__main__":

    extract_company_financials(
        ticker="MSFT",
        cik="0000789019"
    )