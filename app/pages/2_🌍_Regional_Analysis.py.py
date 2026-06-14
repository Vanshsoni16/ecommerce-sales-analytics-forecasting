import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Regional Analytics")

df = pd.read_csv(
    r"C:\Users\vansh soni\PROJECT_2\data\processed\cleaned_sales.csv"
)

region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .reset_index()
)

fig = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Sales Distribution by Region"
)

st.plotly_chart(fig, use_container_width=True)