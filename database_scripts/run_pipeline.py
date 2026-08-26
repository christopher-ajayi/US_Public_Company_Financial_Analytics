import sys
from pathlib import Path
import time

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from config.companies import COMPANIES
from extract_company_financials import extract_company_financials


def run_pipeline():

    total = len(COMPANIES)
    successful = 0
    failed = 0

    start_time = time.time()

    print("\n")
    print("=" * 70)
    print("Corporate Financial Intelligence Pipeline")
    print("=" * 70)

    for i, company in enumerate(COMPANIES, start=1):

        ticker = company["ticker"]

        print(f"\n[{i}/{total}] Processing {ticker}...")

        try:

            extract_company_financials(
                ticker=ticker,
                cik=company["cik"]
            )

            successful += 1

            print(f"✓ {ticker} completed successfully")

        except Exception as e:

            failed += 1

            print(f"✗ {ticker} failed")
            print(e)

    elapsed = round((time.time() - start_time) / 60, 2)

    print("\n")
    print("=" * 70)
    print("Pipeline Summary")
    print("=" * 70)
    print(f"Companies Processed : {total}")
    print(f"Successful          : {successful}")
    print(f"Failed              : {failed}")
    print(f"Elapsed Time        : {elapsed} minutes")
    print("=" * 70)


if __name__ == "__main__":
    run_pipeline()