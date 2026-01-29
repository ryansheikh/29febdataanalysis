import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Company Sales Dashboard")

# ---------------- CSV Files ----------------
csv_files = {
    "monthly_sales": "monthly_sales.csv",
    "top_products": "top_products.csv",
    "distributor_perf": "distributor_perf.csv",
    "client_type": "client_type.csv",
    "bonus_discount": "bonus_discount.csv"
}

# Load CSVs safely
dataframes = {}
for key, file in csv_files.items():
    if os.path.exists(file):
        df = pd.read_csv(file)
        dataframes[key] = df
        st.success(f"✅ Loaded: {file}")
    else:
        st.error(f"❌ Missing file: {file}")
        st.stop()  # Stop app if a file is missing

# Assign dataframes to variables
monthly_sales = dataframes['monthly_sales']
top_products = dataframes['top_products']
distributor_perf = dataframes['distributor_perf']
client_type = dataframes['client_type']
bonus_discount = dataframes['bonus_discount']

# ---------------- Preprocessing ----------------
monthly_sales['MonthYear'] = pd.to_datetime(monthly_sales[['Year','Month']].assign(DAY=1))
bonus_discount['MonthYear'] = pd.to_datetime(bonus_discount[['Year','Month']].assign(DAY=1))

# ---------------- VISUALIZATIONS ----------------

# 1️⃣ Monthly Sales Line Chart
st.subheader("Monthly Sales Trend")
fig1 = px.line(monthly_sales, x='MonthYear', y='TotalSales', markers=True, title='Monthly Sales')
st.plotly_chart(fig1, use_container_width=True)

# 2️⃣ Monthly Units Sold
st.subheader("Monthly Units Sold")
fig2 = px.line(monthly_sales, x='MonthYear', y='TotalUnits', markers=True, title='Units Sold per Month')
st.plotly_chart(fig2, use_container_width=True)

# 3️⃣ Monthly Bonus vs Discount
st.subheader("Monthly Bonus vs Discount")
fig3 = px.line(bonus_discount, x='MonthYear', y=['TotalBonus','TotalDiscount'], title='Bonus & Discount Trend')
st.plotly_chart(fig3, use_container_width=True)

# 4️⃣ Top 10 Products by Revenue
st.subheader("Top 10 Products by Revenue")
top10_products = top_products.sort_values('Revenue', ascending=False).head(10)
fig4 = px.bar(top10_products, x='ProductName', y='Revenue', text='Revenue', title='Top Products by Revenue')
st.plotly_chart(fig4, use_container_width=True)

# 5️⃣ Top 10 Products by Units Sold
st.subheader("Top 10 Products by Units Sold")
top10_units = top_products.sort_values('UnitsSold', ascending=False).head(10)
fig5 = px.bar(top10_units, x='ProductName', y='UnitsSold', text='UnitsSold', title='Top Products by Units Sold')
st.plotly_chart(fig5, use_container_width=True)

# 6️⃣ Distributor Revenue (Top 10)
st.subheader("Top 10 Distributors by Revenue")
top10_distributors = distributor_perf.sort_values('Revenue', ascending=False).head(10)
fig6 = px.bar(top10_distributors, x='DistributorName', y='Revenue', text='Revenue', title='Top Distributors')
st.plotly_chart(fig6, use_container_width=True)

# 7️⃣ Distributor Revenue Pie Chart
st.subheader("Distributor Revenue Distribution")
fig7 = px.pie(distributor_perf, names='DistributorName', values='Revenue', title='Distributor Revenue')
st.plotly_chart(fig7, use_container_width=True)

# 8️⃣ Client Type Revenue Pie Chart
st.subheader("Revenue by Client Type")
fig8 = px.pie(client_type, names='ClientType', values='Revenue', title='Revenue by Client Type')
st.plotly_chart(fig8, use_container_width=True)

# 9️⃣ Client Count by Type
st.subheader("Client Count by Type")
fig9 = px.bar(client_type, x='ClientType', y='Clients', text='Clients', title='Number of Clients per Client Type')
st.plotly_chart(fig9, use_container_width=True)

# 🔟 Bonus vs Discount Scatter Plot
st.subheader("Bonus vs Discount Scatter")
fig10 = px.scatter(bonus_discount, x='TotalBonus', y='TotalDiscount', size='TotalBonus', color='TotalDiscount',
                    hover_data=['Year','Month'], title='Bonus vs Discount Scatter')
st.plotly_chart(fig10, use_container_width=True)

