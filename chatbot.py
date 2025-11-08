import pandas as pd
import streamlit as st

#pands
##import csv
companies_financials = pd.read_csv('/Users/samibsata/Desktop/gen_ai/finacials.csv')

##data cleaning and set up
companies_financials_sorted = companies_financials.groupby(['company']).apply(lambda x: x.sort_values('fiscal year'))
companies_financials_sorted = companies_financials_sorted.reset_index(drop=True)

companies_financials_sorted['company and year'] = companies_financials_sorted['company'].astype(str) + '_' + companies_financials_sorted['fiscal year'].astype(str)
companies_financials_sorted = companies_financials_sorted.drop(['company', 'fiscal year'], axis=1)

new_column_order = ['company and year', 'ticker', 'total revenue', 'net income', 'total assets', 'total liabilities', 'cash flow from ops']
companies_financials_sorted = companies_financials_sorted[new_column_order]

companies_financials_sorted = companies_financials_sorted.set_index('company and year')

##YoY change
companies_financials_sorted['revenue change (%)'] = companies_financials_sorted.groupby(['ticker'])['total revenue'].pct_change() * 100
companies_financials_sorted['income change (%)'] = companies_financials_sorted.groupby(['ticker'])['net income'].pct_change() * 100
companies_financials_sorted['asset change (%)'] = companies_financials_sorted.groupby(['ticker'])['total assets'].pct_change() * 100
companies_financials_sorted['liabilities change (%)'] = companies_financials_sorted.groupby(['ticker'])['total liabilities'].pct_change() * 100
companies_financials_sorted['cashflow change (%)'] = companies_financials_sorted.groupby(['ticker'])['cash flow from ops'].pct_change() * 100

##agregates
total_revenue_cv = companies_financials_sorted.groupby('ticker')['total revenue'].agg(
    mean='mean',
    std='std'
)
total_revenue_cv['coefficient of variation'] = (total_revenue_cv['std'] / total_revenue_cv['mean']) * 100
total_revenue_cv.head()

#streamlit

user_input = st.text_input("What company would you like to look at:")


if 'microsoft' in user_input.lower():
    year = st.text_input("what year would you like to look at?:")
    if '2023' in year.lower() or '2024' in year.lower() or '2025' in year.lower():
        figure = st.text_input("What would you like to look at?:")
        if 'revenue' in figure.lower():
            company_and_year = user_input + "_" + year
            specific_value = companies_financials_sorted.loc[company_and_year, 'total revenue']
            st.write('the total revenue is ' + str(specific_value))
    else:
        st.write('I dont have data for that year, please choose another year')


