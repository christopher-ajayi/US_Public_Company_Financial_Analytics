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


    income_df = df[
        df["metric"].isin(income_metrics)
    ].copy()


    # Annual filings only
    income_df = income_df[
        income_df["form"] == "10-K"
    ]


    # Calculate duration
    income_df["duration"] = (
        pd.to_datetime(income_df["end"])
        -
        pd.to_datetime(income_df["start"])
    ).dt.days


    # Keep annual periods only
    income_df = income_df[
        income_df["duration"] > 250
    ]


    # Keep the longest/latest annual record
    income_df = (
        income_df
        .sort_values(
            [
                "company_id",
                "metric",
                "end",
                "duration"
            ],
            ascending=[
                True,
                True,
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


    # Pivot using actual reporting period
    income_df = (
    income_df
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


    return income_df