# ******************************************************************************
# IMPORT LIBRARIES
# ******************************************************************************
import finpie as fp
import pandas as pd
import yfinance as yf
import pandas as pd
import plotly.express as px

# ******************************************************************************
# FUNCTIONS
# ******************************************************************************

# Get Data Function


def get_date(ticker: str):
    """
    This functions get the data based on the input ticker. It only take a single
    ticker as string. For instance, the ticker for Google is 'GOOG'.

    Outputs all the calculations and ratios.
    """

    # get the income statement
    inc_st = fp.Fundamentals(ticker, source="yahoo")
    df_inc_st = inc_st.income_statement()

    # Change the values to original
    # --------------------------------------------------------------------------
    exclude_column = ["basic_eps", "diluted_eps"]

    # make the data-frame
    df_inc_st_org = df_inc_st.loc[:, ~df_inc_st.columns.isin(exclude_column)]

    # change to the same name for easyness
    df_inc_st = df_inc_st_org.copy()

    # Multiply the df with 1000 to make original
    df_inc_st = df_inc_st.mul(1000)

    # --------------------------------------------------------------------------
    """
    We will use 'yfinance' package to get the balance sheet data as the 
    previous libaray 'finpie' doesn't gave the broken down results.
    """

    # Balance Statement
    tgt = yf.Ticker(ticker)
    df_bal_st = tgt.get_balance_sheet()

    # Combine the Balance Sheet and Income Statement
    # --------------------------------------------------------------------------

    # Pivot the 'df_inc_st'
    df_inc_st_t = df_inc_st.transpose()

    # ----------------------------------
    # Change the column name (inc st)
    new_col = df_inc_st_t.columns.year

    # Assign the new column (inc st)
    df_inc_st_t.columns = new_col

    # Change the column name (bal st)
    new_col = df_bal_st.columns.year

    # Assign the new column (bal st)
    df_bal_st.columns = new_col

    # ----------------------------------

    # # Change the column name
    # df_inc_st_t.columns = ['2022', '2021', '2020', '2019']

    # # Change the column name for 'df_bal_st'
    # df_bal_st.columns = ['2022', '2021', '2020', '2019']

    # Combine the 'df_inc_st_t' and 'df_bal_st'
    df_comb = pd.concat([df_inc_st_t, df_bal_st], axis=0)

    # Transposing the df to get correct format
    df = df_comb.transpose()

    # --------------------------------------------------------------------------
    # Financial Ratios Calculations

    # Gross Profit Margin
    df["gross_profit_margin"] = (
        df["gross_profit"] / df["total_revenue"]) * 100

    # Operating Margin
    df["operating_margin"] = (
        df["operating_income"] / df["total_revenue"]) * 100

    # Net Profit Margin
    df["net_profit_margin"] = (
        df["normalized_income"] / df["total_revenue"]) * 100

    # Debt-to-equity Ratio
    df["debt_equity_ratio"] = df["Total Liab"] / df["Total Stockholder Equity"]

    # Current Ratio
    df["current_ratio"] = df["Total Current Assets"] / \
        df["Total Current Liabilities"]

    # Fixed Asset Turnover
    df["fixed_asset_turn"] = df["total_revenue"] / \
        df["Property Plant Equipment"]

    # Total Asset Turnover
    df["total_asset_turn"] = df["total_revenue"] / df["Total Assets"]

    # Return on Asset
    df["ROA"] = df["net_profit_margin"] * df["total_asset_turn"]

    # Return on Equity
    df["ROE"] = df["normalized_income"] / df["Total Stockholder Equity"]

    # --------------------------------------------------------------------------

    return df


# Combine multiple ticker

def combine_ticker(ticker_list: list):
    """This functions get the data for the list of tickers. You can input the
    tickers as string in list.

    The out put is the dataframe
    """

    df = pd.DataFrame()

    for items in ticker_list:

        df1 = get_date(items)
        df1.sort_index(ascending=True, inplace=True)
        df1.reset_index(inplace=True)
        df1["company"] = items
        df1 = pd.melt(df1, id_vars=["index", "company"])

        df = pd.concat([df, df1], axis=0, ignore_index=True)

    return df


# Plot Functions

def make_plot(ratio_name, df, ratio_full_name):
    """
    ratio_name: Name of the ratio plot as string. This has to be same as the names
                in the dataframe or imported data.
    df: the combined data-frame that has main data
    ratio_full_name: full name of the ratio. This will be the title of plot

    """
    # Subsetting the data-frame
    df_sub = df[df["variable"] == ratio_name]

    # Dropping the NAs
    df_sub.dropna(inplace=True)

    # Changing the values to integer from string
    df_sub["value"] = pd.to_numeric(df_sub["value"])

    # Rounding the values
    df_sub = df_sub.round(2)

    # Plot

    fig = px.line(
        df_sub,
        x="index",
        y="value",
        color="company",
        markers=True,
        labels={"value": ratio_name, "index": "Year"},
        title=ratio_full_name,
        template="plotly_white",
    )

    return fig
