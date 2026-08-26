import pandas as pd


def transform_income(df):

    income_metrics = [
        "revenue",
        "cost_of_revenue",
        "operating_income",
        "net_income",
        "rd_expense",
        "income_tax"
    ]

    # Keep required metrics only
    income_df = df[
        df["metric"].isin(income_metrics)
    ].copy()

    print("After metric filter:")
    print(income_df["metric"].value_counts())


    # Annual filings only
    income_df = income_df[
        income_df["form"] == "10-K"
    ].copy()

    print("\nAfter 10-K filter:")
    print(income_df["metric"].value_counts())


    # Calculate duration
    income_df["duration"] = (
        pd.to_datetime(income_df["end"])
        -
        pd.to_datetime(income_df["start"])
    ).dt.days


    # Keep annual periods only
    income_df = income_df[
        income_df["duration"] > 250
    ].copy()

    print("\nRevenue after annual duration filter:")
    print(
    income_df[
        income_df["metric"] == "revenue"
    ][
        ["company_id", "start", "end", "val"]
    ].head(20)
)


    print("\nAfter annual duration filter:")
    print(income_df["metric"].value_counts())


    # Remove duplicate filings
    income_df = (
        income_df
        .sort_values(
            [
                "company_id",
                "metric",
                "end",
                "duration",
                "filed"
            ],
            ascending=[
                True,
                True,
                False,
                False,
                False
            ]
        )
        .drop_duplicates(
            [
                "company_id",
                "metric",
                "start",
                "end"
            ],
            keep="first"
        )
    )


    print("\nAfter duplicate removal:")
    print(income_df["metric"].value_counts())


    # Pivot financial metrics into columns
    income_df = (
        income_df
        .pivot_table(
            index=[
                "company_id",
                "start",
                "end",
                "fy",
                "fp",
                "form"
            ],
            columns="metric",
            values="val",
            aggfunc="first"
        )
        .reset_index()
    )


    # Remove pivot column name
    income_df.columns.name = None


    print("\nFinal transformed income:")
    print(income_df.head())

    print("\nRevenue availability:")
    print(income_df["revenue"].notna().sum(),
          "available out of",
          len(income_df))


    return income_df