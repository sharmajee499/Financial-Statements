# ******************************************************************************
# IMPORT LIBRARIES
# ******************************************************************************
import helper_functions as hf
import streamlit as st
import streamlit_tags as st_tags


# ******************************************************************************
# Get the Ticker Values
# ******************************************************************************
# Link for Ticker Info
st.header(
    "Please find the Ticker name from the EDGAR [website](https://www.sec.gov/edgar/searchedgar/companysearch)")


# options to input the ticker value
options = st_tags.st_tags(
    label="Enter the Tickers (All Caps)",
    text="Press Enter to Add More",
    value=["TGT", "WMT"],
    maxtags=5,
    key="1",
)


st.text("""The max number of companies to compare are 5.""")


# Get the Data
df = hf.combine_ticker(options)

# Tabs for Different Viz
GPM, OM, NPM, DER, CR, TAT, ROA, ROE = st.tabs(
    ['GPM', 'OM', 'NPM', 'DER', 'CR', 'TAT', 'ROA', 'ROE'])


# ******************************************************************************
# Plots for each tabs
# ******************************************************************************

# Gross Profit Margin
with GPM:
    st.subheader(
        f"Comparision of Gross Profit Margin(GPM) for {[i for i in options]}")

    # Get the plot
    fig_gpm = hf.make_plot('gross_profit_margin', df, "Gross Profit Margin")
    st.plotly_chart(fig_gpm)

    # Explaination
    with st.expander("Explanation"):
        st.write("""Gross profit margin is an analytical metric expressed as a 
                company's net sales minus the cost of goods sold (COGS).""")

        st.write("""If a company's gross profit margin wildly fluctuates, this 
        may signal poor management practices and/or inferior products. On the 
        other hand, such fluctuations may be justified in cases where a company 
        makes sweeping operational changes to its business model, in which case 
        temporary volatility should be no cause for alarm""")

        st.latex(
            r'''\text{Gross Profit Margin} = \frac{Net Sales - COGS}{Net Sales}''')

        st.markdown("""*Referenced from Investopedia*""")


# Operational Margin
with OM:
    st.subheader(
        f"Comparision of Operational Margin(OM) for {[i for i in options]}")

    # Get the plot
    fig_om = hf.make_plot('operating_margin', df, "Operating Margin")
    st.plotly_chart(fig_om)

    with st.expander('Explanation'):
        st.write("""The operating margin represents how efficiently a company is
        able to generate profit through its core operations.""")

        st.write("""A company’s operating margin, sometimes referred to as return 
        on sales (ROS), is a good indicator of how well it is being managed and 
        how efficient it is at generating profits from sales. It shows the 
        proportion of revenues that are available to cover non-operating costs, 
        such as paying interest, which is why investors and lenders pay close 
        attention to it.""")

        st.latex(
            r'''\text{Operating Margin} = \frac{\text{Operating Revenue}}{\text{Revenue}}''')

        st.markdown("""*Referenced from Investopedia*""")


# Net Profit Margin
with NPM:
    st.subheader(
        f"Comparision of Net Profit Margin(NPM) for {[i for i in options]}")

    # Get the plot
    fig_npm = hf.make_plot('net_profit_margin', df, "Net Profit Margin")
    st.plotly_chart(fig_npm)

    with st.expander('Explanation'):
        st.write("""Net profit margin measures how much net income is generated 
        as a percentage of revenues received.""")

        st.write("""The net profit margin is perhaps the most important measure 
        of a company's overall profitability. It is the ratio of net profits to 
        revenues for a company or business segment. Expressed as a percentage, 
        the net profit margin shows how much profit is generated from every $1 
        in sales, after accounting for all business expenses involved in earning
         those revenues.""")

        st.latex(
            r'''\text{Net Profit Margin Margin} = \frac{\text{Net Income}}{\text{Revenue}}*100''')

        st.markdown("""*Referenced from Investopedia*""")


# Debt-Equity Ratio
with DER:
    st.subheader(
        f"Comparision of Debt-Equity Ratio(DER) for {[i for i in options]}")

    # Get the plot
    fig_der = hf.make_plot('debt_equity_ratio', df, "Debt-Equity Ratio")
    st.plotly_chart(fig_der)

    with st.expander('Explanation'):
        st.write("""The debt-to-equity (DER) ratio shows the proportions of 
        equity and debt a company is using to finance its assets and it signals 
        the extent to which shareholder's equity can fulfill obligations to 
        creditors, in the event a business declines.""")

        st.write("""A low debt-to-equity ratio indicates a lower amount of 
        financing by debt via lenders, versus funding through equity via 
        shareholders. A higher ratio indicates that the company is getting more 
        of its financing by borrowing money, which subjects the company to 
        potential risk if debt levels are too high.""")

        st.latex(
            r'''\text{Debt To Equity Ratio} = \frac{\text{Total Liabilities}}{\text{Total Shareholder Equity}}''')

        st.markdown("""*Referenced from Investopedia*""")


# Current Ratio
with CR:
    st.subheader(
        f"Comparision of Current Ratio(CR) for {[i for i in options]}")

    # Get the plot
    fig_cr = hf.make_plot('current_ratio', df, "Current Ratio")
    st.plotly_chart(fig_cr)

    with st.expander('Explanation'):
        st.write("""The current ratio is a liquidity ratio that measures a 
        company’s ability to pay short-term obligations or those due within one
         year. It tells investors and analysts how a company can maximize the 
         current assets on its balance sheet to satisfy its current debt and 
         other payables.""")

        st.write("""A current ratio that is in line with the industry average or
         slightly higher is generally considered acceptable. A current ratio 
         that is lower than the industry average may indicate a higher risk of 
         distress or default. """)

        st.latex(
            r'''\text{Current Ratio} = \frac{\text{Current Ratio}}{\text{Total Liabilities}}''')

        st.markdown("""*Referenced from Investopedia*""")


# Fixed Asset Turnover
with TAT:
    st.subheader(
        f"Comparision of Total Asset Turnover(TAT) for {[i for i in options]}")

    # Get the plot
    fig_tat = hf.make_plot('total_asset_turn', df,
                           "Total Asset Turnover Ratio")
    st.plotly_chart(fig_tat)

    with st.expander('Explanation'):
        st.write("""The asset turnover ratio measures how effectively a company 
        uses its assets to generate revenue or sales. The ratio compares the 
        dollar amount of sales or revenues to the company's total assets to 
        measure the efficiency of the company's operations.""")

        st.write("""A higher ratio is generally favored as there is the 
        implication that the company is more efficient in generating sales or 
        revenues. A lower ratio illustrates that a company may not be using its 
        assets as efficiently. Asset turnover ratios vary throughout different 
        sectors, so only the ratios of companies that are in the same sector 
        should be compared. """)

        st.latex(
            r'''\text{Total Asset Turnover Ratio} = \frac{\text{Net Sales}}{\text{Average Total Assets}}''')

        st.markdown("""*Referenced from Investopedia*""")


# Return on Asset
with ROA:
    st.subheader(
        f"Comparision of Return on Asset(ROA) for {[i for i in options]}")

    # Get the plot
    fig_roa = hf.make_plot('ROA', df, "Return on Asset")
    st.plotly_chart(fig_roa)

    with st.expander('Explanation'):
        st.write("""The term return on assets (ROA) refers to a financial ratio 
        that indicates how profitable a company is in relation to its total 
        assets. Corporate management, analysts, and investors can use ROA to 
        determine how efficiently a company uses its assets to generate a profit
        .""")

        st.write("""The metric is commonly expressed as a percentage by using a 
        company's net income and its average assets. A higher ROA means a 
        company is more efficient and productive at managing its balance sheet 
        to generate profits while a lower ROA indicates there is room for 
        improvement. """)

        st.latex(
            r'''\text{Return on Asset} = \frac{\text{Net Income}}{\text{Total Assets}}''')

        st.markdown("""*Referenced from Investopedia*""")

# Return on Equity
with ROE:
    st.subheader(
        f"Comparision of Return on Equity(ROE) for {[i for i in options]}")

    # Get the plot
    fig_roe = hf.make_plot('ROE', df, "Return on Equity")
    st.plotly_chart(fig_roe)

    with st.expander('Explanation'):
        st.write("""Return on equity (ROE) is a measure of financial performance
         calculated by dividing net income by shareholders' equity. Because 
         shareholders' equity is equal to a company's assets minus its debt, 
         ROE is considered the return on net assets.""")

        st.write("""ROE is considered a gauge of a corporation's profitability 
        and how efficient it is in generating profits. The higher the ROE, the 
        more efficient a company's management is at generating income and growth
         from its equity financing.""")

        st.latex(
            r'''\text{Return on Equity} = \frac{\text{Net Income}}{\text{Average Shareholder Equity}}''')

        st.markdown("""*Referenced from Investopedia*""")
