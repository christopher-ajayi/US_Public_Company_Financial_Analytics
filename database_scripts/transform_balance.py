import pandas as pd


def transform_balance(df):

    balance_metrics = [
        "assets",
        "liabilities",
        "equity",
        "cash",
        "inventory",
        "current_assets",
        "current_liabilities",
        "long_term_debt"
    ]


    balance_df = df[
        df["metric"].isin(balance_metrics)
    ].copy()


    # Annual filings only
    balance_df = balance_df[
        balance_df["form"] == "10-K"
    ]


    # Remove rows without balance sheet date
    balance_df = balance_df[
        balance_df["end"].notna()
    ]


    # Convert dates
    balance_df["end"] = pd.to_datetime(
        balance_df["end"]
    )


    # Keep latest filing for each company/date/metric
    # Keep latest annual filing for each balance sheet date and metric
    balance_df = (
        balance_df
        .sort_values(
            [
                "company_id",
                "end",
                "metric",
                "fy",
                "filed"
            ],
            ascending=[
                True,
                True,
                True,
                False,
                False
            ]
        )
        .drop_duplicates(
            [
                "company_id",
                "end",
                "metric"
            ],
            keep="first"
        )
    )


    # Pivot metrics into columns while preserving metadata
    balance_df = (
        balance_df
        .pivot_table(
            index=[
                "company_id",
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


    return balance_df