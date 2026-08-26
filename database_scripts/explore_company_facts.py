import os
import requests
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env", override=True)

SEC_USER_AGENT = os.getenv("SEC_USER_AGENT")

print("BASE_DIR:", BASE_DIR)
print("SEC_USER_AGENT:", SEC_USER_AGENT)

headers = {
    "User-Agent": SEC_USER_AGENT
}

CIK = "0000789019"   # Microsoft

url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json"

response = requests.get(url, headers=headers)
response.raise_for_status()

facts = response.json()["facts"]["us-gaap"]

print(f"Total concepts: {len(facts)}")

keywords = [
    "Revenue",
    "Asset",
    "Liabil",
    "Equity",
    "Cash",
    "Inventory",
    "Debt",
    "Research",
    "OperatingIncome",
    "NetIncome"
]

print("\nMatching concepts:\n")

for concept in sorted(facts.keys()):
    if any(k.lower() in concept.lower() for k in keywords):
        print(concept)