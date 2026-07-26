-- corp_fin.clean_balance_view source

CREATE OR REPLACE VIEW corp_fin.clean_balance_view
AS WITH ranked_balance AS (
         SELECT fact_balance.balance_id,
            fact_balance.company_id,
            fact_balance.period_start,
            fact_balance.period_end,
            fact_balance.assets,
            fact_balance.liabilities,
            fact_balance.equity,
            fact_balance.cash,
            fact_balance.inventory,
            fact_balance.current_assets,
            fact_balance.current_liabilities,
            fact_balance.long_term_debt,
            fact_balance.fiscal_year,
            fact_balance.fiscal_period,
            fact_balance.filing_form,
            fact_balance.filed_date,
            row_number() OVER (PARTITION BY fact_balance.company_id, fact_balance.period_end ORDER BY fact_balance.filed_date DESC) AS rn
           FROM corp_fin.fact_balance
        )
 SELECT company_id,
    period_end,
    assets,
    liabilities,
    equity,
    cash,
    inventory,
    current_assets,
    current_liabilities,
    long_term_debt,
    fiscal_year,
    fiscal_period,
    filing_form,
    filed_date
   FROM ranked_balance
  WHERE rn = 1;
  
 
  
  -- corp_fin.clean_cashflow_view source

CREATE OR REPLACE VIEW corp_fin.clean_cashflow_view
AS WITH ranked AS (
         SELECT fact_cashflow.cashflow_id,
            fact_cashflow.company_id,
            fact_cashflow.period_start,
            fact_cashflow.period_end,
            fact_cashflow.operating_cash_flow,
            fact_cashflow.investing_cash_flow,
            fact_cashflow.financing_cash_flow,
            fact_cashflow.capital_expenditure,
            fact_cashflow.dividends_paid,
            fact_cashflow.fiscal_year,
            fact_cashflow.fiscal_period,
            fact_cashflow.filing_form,
            fact_cashflow.filed_date,
            row_number() OVER (PARTITION BY fact_cashflow.company_id, fact_cashflow.period_end ORDER BY fact_cashflow.filed_date DESC) AS rn
           FROM corp_fin.fact_cashflow
          WHERE fact_cashflow.filing_form::text = '10-K'::text AND fact_cashflow.fiscal_period::text = 'FY'::text
        )
 SELECT company_id,
    fiscal_year,
    period_start,
    period_end,
    operating_cash_flow,
    investing_cash_flow,
    financing_cash_flow,
    capital_expenditure,
    dividends_paid,
    filed_date
   FROM ranked
  WHERE rn = 1;
  
  
-- corp_fin.clean_income_view source

CREATE OR REPLACE VIEW corp_fin.clean_income_view
AS WITH ranked_income AS (
         SELECT fact_income.income_id,
            fact_income.company_id,
            fact_income.period_start,
            fact_income.period_end,
            fact_income.revenue,
            fact_income.operating_income,
            fact_income.net_income,
            fact_income.rd_expense,
            fact_income.income_tax,
            fact_income.fiscal_year,
            fact_income.fiscal_period,
            fact_income.filing_form,
            fact_income.filed_date,
            row_number() OVER (PARTITION BY fact_income.company_id, fact_income.period_end ORDER BY fact_income.filed_date DESC) AS rn
           FROM corp_fin.fact_income
        )
 SELECT company_id,
    period_start,
    period_end,
    revenue,
    operating_income,
    net_income,
    rd_expense,
    income_tax,
    fiscal_year,
    fiscal_period,
    filing_form,
    filed_date
   FROM ranked_income
  WHERE rn = 1;
  
  
  
  
  
  
  
  -- corp_fin.company_financials_view source

CREATE OR REPLACE VIEW corp_fin.company_financials_view
AS SELECT i.company_id,
    i.period_start,
    i.period_end,
    i.fiscal_year,
    i.fiscal_period,
    i.filing_form,
    i.filed_date,
    i.revenue,
    i.operating_income,
    i.net_income,
    i.rd_expense,
    i.income_tax,
    b.assets,
    b.liabilities,
    b.equity,
    b.cash,
    b.inventory,
    b.current_assets,
    b.current_liabilities,
    b.long_term_debt,
    c.operating_cash_flow,
    c.investing_cash_flow,
    c.financing_cash_flow,
    c.capital_expenditure,
    c.dividends_paid
   FROM corp_fin.clean_income_view i
     LEFT JOIN corp_fin.clean_balance_view b ON i.company_id = b.company_id AND i.period_end = b.period_end
     LEFT JOIN corp_fin.clean_cashflow_view c ON i.company_id = c.company_id AND i.period_end = c.period_end;
  
  
  
  
  
  
  -- corp_fin.financials_analysis_view source

CREATE OR REPLACE VIEW corp_fin.financials_analysis_view
AS SELECT f.company_id,
    f.period_start,
    f.period_end,
    f.fiscal_year,
    f.fiscal_period,
    f.filing_form,
    f.filed_date,
    f.revenue,
    f.operating_income,
    f.net_income,
    f.rd_expense,
    f.income_tax,
    f.assets,
    f.liabilities,
    f.equity,
    f.cash,
    f.inventory,
    f.current_assets,
    f.current_liabilities,
    f.long_term_debt,
    f.operating_cash_flow,
    f.investing_cash_flow,
    f.financing_cash_flow,
    f.capital_expenditure,
    f.dividends_paid,
    c.ticker,
    c.company_name,
    c.sector,
    c.country,
    c.industry,
    c.exchange
   FROM corp_fin.company_financials_view f
     LEFT JOIN corp_fin.dim_company c ON f.company_id = c.company_id;