import streamlit as st
import pandas as pd

import streamlit as st


st.set_page_config(
    page_title="E-Commerce Analytics Platform",
    page_icon="📊",
    layout="wide"
)


st.title("📊 E-Commerce Analytics Platform")

st.markdown("""
### 🧠 AI-Powered Sales Intelligence Dashboard  
Analyze sales trends, performance, and forecast future revenue using machine learning.
""")

# Load Data
df = pd.read_csv(
    r"C:\Users\vansh soni\PROJECT_2\data\processed\cleaned_sales.csv"

)
st.sidebar.title("🎛️ Control Panel")

selected_region = st.sidebar.selectbox(
    "🌍 Region",
    ["All"] + list(df["Region"].unique())
)

selected_category = st.sidebar.selectbox(
    "📦 Category",
    ["All"] + list(df["Category"].unique())
)

st.sidebar.markdown("---")
st.sidebar.info("Use filters to explore sales performance")

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]



total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = len(filtered_df)
avg_order_value = filtered_df["Sales"].mean()





# Title
st.divider()

# KPIs
st.header("📊 Key Performance Indicators")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
avg_order_value = df["Sales"].mean()

st.divider()

st.header("📈 Sales Analysis")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"₹{total_sales:,.0f}")
col2.metric("Total Profit", f"₹{total_profit:,.0f}")
col3.metric("Total Orders", total_orders)
col4.metric("Average Order Value", f"₹{avg_order_value:,.2f}")

st.divider()

st.dataframe(df.head())


st.header("📦 Data Preview")
st.subheader("Sales Performance")
import plotly.express as px

monthly_sales = (
    filtered_df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

fig = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    title="Monthly Sales Trend"
)

st.plotly_chart(fig, use_container_width=True)


category_sales = (
    filtered_df.groupby("Category")["Sales"]
      .sum()
      .reset_index()
)

fig = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Sales by Category"
)

st.plotly_chart(fig, use_container_width=True)





region_profit = (
    filtered_df.groupby("Region")["Profit"]
      .sum()
      .reset_index()
)

fig = px.bar(
    region_profit,
    x="Region",
    y="Profit",
    title="Profit by Region"
)

st.plotly_chart(fig, use_container_width=True)



top_products = (
    filtered_df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

fig = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("📌 Business Insights")

top_region = df.groupby("Region")["Sales"].sum().idxmax()
top_category = df.groupby("Category")["Sales"].sum().idxmax()

st.success(f"🏆 Top Region: {top_region}")
st.success(f"📦 Best Category: {top_category}")


st.markdown("---")
st.markdown("Built by Data Science Project | E-Commerce Analytics Dashboard")