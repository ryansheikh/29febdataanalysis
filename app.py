import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Company Sales Dashboard")

# Load CSVs
monthly_sales = pd.read_csv('monthly_sales_clean.csv')
top_products = pd.read_csv('top_products_clean.csv')
distributor_perf = pd.read_csv('distributor_perf_clean.csv')
client_type = pd.read_csv('client_type_clean.csv')
bonus_discount = pd.read_csv('bonus_discount_clean.csv')

# 1️⃣ Monthly Sales
st.subheader("Monthly Sales Trend")
monthly_sales['MonthYear'] = pd.to_datetime(monthly_sales[['Year','Month']].assign(DAY=1))
fig1 = px.line(monthly_sales, x='MonthYear', y='TotalSales', title='Monthly Sales')
st.plotly_chart(fig1, use_container_width=True)

# 2️⃣ Top Products
st.subheader("Top 50 Products by Revenue")
fig2 = px.bar(top_products, x='ProductName', y='Revenue', title='Top Products', text='Revenue')
st.plotly_chart(fig2, use_container_width=True)

# 3️⃣ Distributor Performance
st.subheader("Distributor Revenue Performance")
fig3 = px.bar(distributor_perf.head(10), x='DistributorName', y='Revenue', title='Top 10 Distributors')
st.plotly_chart(fig3, use_container_width=True)

# 4️⃣ Client Type Analysis
st.subheader("Client Type Analysis")
fig4 = px.pie(client_type, names='ClientType', values='Revenue', title='Revenue by Client Type')
st.plotly_chart(fig4, use_container_width=True)

# 5️⃣ Bonus & Discount Analysis
st.subheader("Bonus vs Discount")
bonus_discount['MonthYear'] = pd.to_datetime(bonus_discount[['Year','Month']].assign(DAY=1))
fig5 = px.line(bonus_discount, x='MonthYear', y=['TotalBonus','TotalDiscount'], title='Bonus & Discount Trend')
st.plotly_chart(fig5, use_container_width=True)
