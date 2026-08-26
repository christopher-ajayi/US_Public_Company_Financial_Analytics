import pandas as pd



def extract_fact(
        facts,
        concept,
        metric_name
):

    if concept not in facts:
        print(f"{concept} not found")
        return None


    if "USD" not in facts[concept]["units"]:
        return None


    df = pd.DataFrame(
        facts[concept]["units"]["USD"]
    )


    required_columns = [
        "start",
        "end",
        "val",
        "fy",
        "fp",
        "form",
        "filed"
    ]


    for col in required_columns:

        if col not in df.columns:
            df[col] = None



    df = df[required_columns]


    df["metric"] = metric_name


    return df





def transform_financial_data(facts):


    metrics = {

        # Income statement
        "revenue":
        "RevenueFromContractWithCustomerExcludingAssessedTax",

        "cost_of_revenue":
        "CostOfRevenue",

        "operating_income":
        "OperatingIncomeLoss",

        "net_income":
        "NetIncomeLoss",

        "rd_expense":
        "ResearchAndDevelopmentExpense",

        "income_tax":
        "IncomeTaxExpenseBenefit",


        # Balance sheet

        "assets":
        "Assets",

        "current_assets":
        "AssetsCurrent",

        "cash":
        "CashAndCashEquivalentsAtCarryingValue",

        "inventory":
        "InventoryNet",

        "accounts_receivable":
        "AccountsReceivableNetCurrent",

        "liabilities":
        "Liabilities",

        "current_liabilities":
        "LiabilitiesCurrent",

        "long_term_debt":
        "LongTermDebtNoncurrent",

        "equity":
        "StockholdersEquity",


        # Cash flow

        "operating_cash_flow":
        "NetCashProvidedByUsedInOperatingActivities",

        "investing_cash_flow":
        "NetCashProvidedByUsedInInvestingActivities",

        "financing_cash_flow":
        "NetCashProvidedByUsedInFinancingActivities",

        "capital_expenditure":
        "PaymentsToAcquirePropertyPlantAndEquipment",

        "dividends_paid":
        "PaymentsOfDividends"

    }



    frames = []


    for metric, tag in metrics.items():

        df = extract_fact(
            facts,
            tag,
            metric
        )


        if df is not None:
            frames.append(df)



    financial_df = pd.concat(
        frames,
        ignore_index=True
    )



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