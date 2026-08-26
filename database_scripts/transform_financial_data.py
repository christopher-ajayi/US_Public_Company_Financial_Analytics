import pandas as pd


def extract_fact(facts, concept, metric_name):

    if concept not in facts:
        print(f"{concept} not found")
        return None

    data = facts[concept]["units"]["USD"]

    df = pd.DataFrame(data)

    if "start" not in df.columns:
        df["start"] = None

    if "end" not in df.columns:
        df["end"] = None

    columns = [
        "start",
        "end",
        "val",
        "fy",
        "fp",
        "form",
        "filed"
    ]

    df = df[[c for c in columns if c in df.columns]]

    df["metric"] = metric_name

    return df



def transform_financial_data(facts):

    metrics = {
    # Income Statement
    "revenue": "RevenueFromContractWithCustomerExcludingAssessedTax",
    "cost_of_revenue": "CostOfRevenue",
    "operating_income": "OperatingIncomeLoss",
    "net_income": "NetIncomeLoss",
    "rd_expense": "ResearchAndDevelopmentExpense",
    "interest_expense": "InterestExpenseNonOperating",
    "income_tax": "IncomeTaxExpenseBenefit",

    # Balance Sheet
    "assets": "Assets",
    "current_assets": "AssetsCurrent",
    "cash": "CashAndCashEquivalentsAtCarryingValue",
    "inventory": "InventoryNet",
    "accounts_receivable": "AccountsReceivableNetCurrent",
    "liabilities": "Liabilities",
    "current_liabilities": "LiabilitiesCurrent",
    "long_term_debt": "LongTermDebtNoncurrent",
    "equity": "StockholdersEquity",

    # Cash Flow
    "operating_cash_flow": "NetCashProvidedByUsedInOperatingActivities",
    "capital_expenditure": "PaymentsToAcquirePropertyPlantAndEquipment",
    "depreciation": "DepreciationDepletionAndAmortization",
    "investing_cash_flow": "NetCashProvidedByUsedInInvestingActivities",
    "financing_cash_flow": "NetCashProvidedByUsedInFinancingActivities",
    "dividends_paid": "PaymentsOfDividends"
}


    frames = []


    for name, tag in metrics.items():

        df = extract_fact(
            facts,
            tag,
            name
        )

        if df is not None:
            frames.append(df)


    financial_df = pd.concat(
        frames,
        ignore_index=True
    )


    # Remove duplicate periods
    financial_df = financial_df.sort_values(
        "filed"
    )


    financial_df = financial_df.drop_duplicates(
        subset=[
            "metric",
            "start",
            "end"
        ],
        keep="last"
    )


    return financial_df