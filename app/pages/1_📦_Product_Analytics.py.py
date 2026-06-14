import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📦 Product Analytics")

df = pd.read_csv(
    r"C:\Users\vansh soni\PROJECT_2\data\processed\cleaned_sales.csv"
)

top_products = (
    df.groupby("Product Name")["Sales"]
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
    title="Top 10 Products by Sales"
)

st.plotly_chart(fig, use_container_width=True)