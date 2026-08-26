import pandas as pd


def transform_cashflow(df):

    cashflow_metrics = [
        "operating_cash_flow",
        "investing_cash_flow",
        "financing_cash_flow",
        "capital_expenditure",
        "dividends_paid"
    ]


    cashflow_df = df[
        df["metric"].isin(cashflow_metrics)
    ].copy()


    # Cash flow is a flow statement
    # Use annual filings only
    cashflow_df = cashflow_df[
        cashflow_df["form"] == "10-K"
    ]


    # Calculate reporting duration
    cashflow_df["duration"] = (
        pd.to_datetime(cashflow_df["end"])
        -
        pd.to_datetime(cashflow_df["start"])
    ).dt.days


    # Keep annual periods
    cashflow_df = cashflow_df[
        cashflow_df["duration"] > 250
    ]


    # Remove duplicate contexts
    cashflow_df = (
        cashflow_df
        .sort_values(
            [
                "company_id",
                "end",
                "metric",
                "filed"
            ],
            ascending=[
                True,
                False,
                True,
                False
            ]
        )
        .drop_duplicates(
            [
                "company_id",
                "start",
                "end",
                "metric"
            ],
            keep="first"
        )
    )


    # Pivot metrics into columns while preserving metadata
    cashflow_df = (
        cashflow_df
        .pivot_table(
            index=[
                "company_id",
                "start",
                "end",
                "fy",
                "fp",
                "form",
                "filed"
            ],
            columns="metric",
            values="val",
            aggfunc="first"
        )
        .reset_index()
    )


    return cashflow_df