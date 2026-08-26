import os
import requests
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env", override=True)


SEC_USER_AGENT = os.getenv("SEC_USER_AGENT")

headers = {
    "User-Agent": SEC_USER_AGENT
}


cik = "0000789019"

url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"


response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

response.raise_for_status()


data = response.json()


import os
import requests
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env", override=True)


SEC_USER_AGENT = os.getenv("SEC_USER_AGENT")

headers = {
    "User-Agent": SEC_USER_AGENT
}


cik = "0000789019"

url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"


response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

response.raise_for_status()


data = response.json()


facts = data["facts"]["us-gaap"]

revenue = facts["RevenueFromContractWithCustomerExcludingAssessedTax"]

print(revenue.keys())
print(revenue["units"].keys())

print(revenue["units"]["USD"][:5])