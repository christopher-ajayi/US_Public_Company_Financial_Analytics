print("TEST SCRIPT STARTED")

from extract_financial_data2 import extract_company_financials


if __name__ == "__main__":

    extract_company_financials(
        ticker="MSFT",
        cik="0000789019"
    )

    print("TEST SCRIPT FINISHED")