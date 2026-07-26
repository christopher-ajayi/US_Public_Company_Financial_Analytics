-- DROP SCHEMA corp_fin;

CREATE SCHEMA corp_fin AUTHORIZATION postgres;



-- corp_fin.company_financials definition

-- Drop table

-- DROP TABLE corp_fin.company_financials;

CREATE TABLE corp_fin.company_financials (
    company_id int4 NOT NULL,
    fiscal_year int4 NOT NULL,
    period_start date NULL,
    period_end date NULL,
    revenue numeric NULL,
    operating_income numeric NULL,
    net_income numeric NULL,
    rd_expense numeric NULL,
    income_tax numeric NULL,
    assets numeric NULL,
    liabilities numeric NULL,
    equity numeric NULL,
    cash numeric NULL,
    inventory numeric NULL,
    current_assets numeric NULL,
    current_liabilities numeric NULL,
    long_term_debt numeric NULL,
    operating_cash_flow numeric NULL,
    investing_cash_flow numeric NULL,
    financing_cash_flow numeric NULL,
    capital_expenditure numeric NULL,
    dividends_paid numeric NULL,
    CONSTRAINT company_financials_company_id_not_null NOT NULL company_id,
    CONSTRAINT company_financials_fiscal_year_not_null NOT NULL fiscal_year,
    CONSTRAINT company_financials_pkey PRIMARY KEY (company_id, fiscal_year)
);


-- corp_fin.company_financials foreign keys

ALTER TABLE corp_fin.company_financials ADD CONSTRAINT fk_company_financials_company FOREIGN KEY (company_id) REFERENCES corp_fin.dim_company(company_id);



-- corp_fin.dim_company definition

-- Drop table

-- DROP TABLE corp_fin.dim_company;

CREATE TABLE corp_fin.dim_company (
    company_id serial4 NOT NULL,
    ticker varchar(10) NOT NULL,
    company_name varchar(100) NOT NULL,
    sector varchar(100) NULL,
    country varchar(50) NULL,
    cik varchar(20) NULL,
    industry varchar(100) NULL,
    exchange varchar(50) NULL,
    CONSTRAINT dim_company_company_id_not_null NOT NULL company_id,
    CONSTRAINT dim_company_company_name_not_null NOT NULL company_name,
    CONSTRAINT dim_company_pkey PRIMARY KEY (company_id),
    CONSTRAINT dim_company_ticker_not_null NOT NULL ticker,
    CONSTRAINT uq_dim_company_ticker UNIQUE (ticker)
);



-- corp_fin.fact_balance definition

-- Drop table

-- DROP TABLE corp_fin.fact_balance;

CREATE TABLE corp_fin.fact_balance (
    balance_id serial4 NOT NULL,
    company_id int4 NOT NULL,
    period_start date NULL,
    period_end date NULL,
    assets numeric NULL,
    liabilities numeric NULL,
    equity numeric NULL,
    cash numeric NULL,
    inventory numeric NULL,
    current_assets numeric NULL,
    current_liabilities numeric NULL,
    long_term_debt numeric NULL,
    fiscal_year int4 NULL,
    fiscal_period varchar(10) NULL,
    filing_form varchar(10) NULL,
    filed_date date NULL,
    CONSTRAINT fact_balance_balance_id_not_null NOT NULL balance_id,
    CONSTRAINT fact_balance_company_id_not_null NOT NULL company_id,
    CONSTRAINT fact_balance_pkey PRIMARY KEY (balance_id),
    CONSTRAINT fact_balance_unique UNIQUE (company_id, period_end, filed_date)
);


-- corp_fin.fact_balance foreign keys

ALTER TABLE corp_fin.fact_balance ADD CONSTRAINT fk_balance_company FOREIGN KEY (company_id) REFERENCES corp_fin.dim_company(company_id);



-- corp_fin.fact_cashflow definition

-- Drop table

-- DROP TABLE corp_fin.fact_cashflow;

CREATE TABLE corp_fin.fact_cashflow (
    cashflow_id serial4 NOT NULL,
    company_id int4 NOT NULL,
    period_start date NULL,
    period_end date NULL,
    operating_cash_flow numeric NULL,
    investing_cash_flow numeric NULL,
    financing_cash_flow numeric NULL,
    capital_expenditure numeric NULL,
    dividends_paid numeric NULL,
    fiscal_year int4 NULL,
    fiscal_period varchar(10) NULL,
    filing_form varchar(10) NULL,
    filed_date date NULL,
    CONSTRAINT fact_cashflow_cashflow_id_not_null NOT NULL cashflow_id,
    CONSTRAINT fact_cashflow_company_id_not_null NOT NULL company_id,
    CONSTRAINT fact_cashflow_pkey PRIMARY KEY (cashflow_id),
    CONSTRAINT fact_cashflow_unique UNIQUE (company_id, period_start, period_end, filed_date)
);


-- corp_fin.fact_cashflow foreign keys

ALTER TABLE corp_fin.fact_cashflow ADD CONSTRAINT fk_cashflow_company FOREIGN KEY (company_id) REFERENCES corp_fin.dim_company(company_id);



-- corp_fin.fact_financials definition

-- Drop table

-- DROP TABLE corp_fin.fact_financials;

CREATE TABLE corp_fin.fact_financials (
    financial_id serial4 NOT NULL,
    company_id int4 NOT NULL,
    metric varchar(100) NOT NULL,
    period_start date NULL,
    period_end date NOT NULL,
    value int8 NULL,
    fiscal_year int8 NULL,
    fiscal_period varchar(10) NULL,
    filing_form varchar(10) NULL,
    filed_date date NULL,
    CONSTRAINT fact_financials_company_id_not_null NOT NULL company_id,
    CONSTRAINT fact_financials_financial_id_not_null NOT NULL financial_id,
    CONSTRAINT fact_financials_metric_not_null NOT NULL metric,
    CONSTRAINT fact_financials_period_end_not_null NOT NULL period_end,
    CONSTRAINT fact_financials_pkey PRIMARY KEY (financial_id)
);
CREATE UNIQUE INDEX unique_financial_record ON corp_fin.fact_financials USING btree (company_id, metric, COALESCE(period_start, '1900-01-01'::date), COALESCE(period_end, '1900-01-01'::date), filing_form, filed_date);



-- corp_fin.fact_income definition

-- Drop table

-- DROP TABLE corp_fin.fact_income;

CREATE TABLE corp_fin.fact_income (
    income_id serial4 NOT NULL,
    company_id int4 NOT NULL,
    period_start date NULL,
    period_end date NULL,
    revenue numeric NULL,
    operating_income numeric NULL,
    net_income numeric NULL,
    rd_expense numeric NULL,
    income_tax numeric NULL,
    fiscal_year int4 NULL,
    fiscal_period varchar(10) NULL,
    filing_form varchar(10) NULL,
    filed_date date NULL,
    CONSTRAINT fact_income_company_id_not_null NOT NULL company_id,
    CONSTRAINT fact_income_income_id_not_null NOT NULL income_id,
    CONSTRAINT fact_income_pkey PRIMARY KEY (income_id),
    CONSTRAINT uq_income_record UNIQUE (company_id, period_start, period_end, filed_date)
);



-- corp_fin.fact_metrics definition

-- Drop table

-- DROP TABLE corp_fin.fact_metrics;

CREATE TABLE corp_fin.fact_metrics (
    metric_id serial4 NOT NULL,
    company_id int4 NOT NULL,
    report_date date NOT NULL,
    gross_margin numeric NULL,
    operating_margin numeric NULL,
    net_margin numeric NULL,
    return_on_assets numeric NULL,
    return_on_equity numeric NULL,
    debt_to_equity numeric NULL,
    free_cash_flow_margin numeric NULL,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP NULL,
    CONSTRAINT fact_metrics_company_id_not_null NOT NULL company_id,
    CONSTRAINT fact_metrics_metric_id_not_null NOT NULL metric_id,
    CONSTRAINT fact_metrics_pkey PRIMARY KEY (metric_id),
    CONSTRAINT fact_metrics_report_date_not_null NOT NULL report_date
);


-- corp_fin.fact_metrics foreign keys

ALTER TABLE corp_fin.fact_metrics ADD CONSTRAINT fk_metrics_company FOREIGN KEY (company_id) REFERENCES corp_fin.dim_company(company_id);


-- corp_fin.fact_prices definition

-- Drop table

-- DROP TABLE corp_fin.fact_prices;

CREATE TABLE corp_fin.fact_prices (
    price_id serial4 NOT NULL,
    company_id int4 NOT NULL,
    price_date date NOT NULL,
    open_price numeric NULL,
    high_price numeric NULL,
    low_price numeric NULL,
    close_price numeric NULL,
    volume int8 NULL,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP NULL,
    CONSTRAINT fact_prices_company_id_not_null NOT NULL company_id,
    CONSTRAINT fact_prices_pkey PRIMARY KEY (price_id),
    CONSTRAINT fact_prices_price_date_not_null NOT NULL price_date,
    CONSTRAINT fact_prices_price_id_not_null NOT NULL price_id
);


-- corp_fin.fact_prices foreign keys

ALTER TABLE corp_fin.fact_prices ADD CONSTRAINT fk_prices_company FOREIGN KEY (company_id) REFERENCES corp_fin.dim_company(company_id);


