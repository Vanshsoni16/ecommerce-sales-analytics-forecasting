import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Regional Analytics")

import os
import pandas as pd

file_path = os.path.join("data", "processed", "cleaned_sales.csv")
df = pd.read_csv(file_path)
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