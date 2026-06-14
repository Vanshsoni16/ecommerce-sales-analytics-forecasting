import pandas as pd
import streamlit as st
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

st.title("📈 Sales Forecasting Dashboard")

# Load Dataset
import os
import pandas as pd

file_path = os.path.join("data", "processed", "cleaned_sales.csv")
sales_data = pd.read_csv(file_path)

sales_data["Order Date"] = pd.to_datetime(
    sales_data["Order Date"]
)

# Monthly Sales Aggregation
monthly_sales_data = (
    sales_data
    .resample("MS", on="Order Date")["Sales"]
    .sum()
    .reset_index()
)

monthly_sales_data.columns = [
    "Date",
    "Sales"
]

st.subheader("📅 Monthly Sales Data")

st.dataframe(
    monthly_sales_data.tail()
)

# Feature Engineering

monthly_sales_data["Month_Number"] = np.arange(
    len(monthly_sales_data)
)

training_features = monthly_sales_data[
    ["Month_Number"]
]

actual_sales = monthly_sales_data[
    "Sales"
]

# Train Model

sales_forecasting_model = LinearRegression()

sales_forecasting_model.fit(
    training_features,
    actual_sales
)

# Forecast Future Months

number_of_future_months = 6

future_month_numbers = np.arange(
    len(monthly_sales_data),
    len(monthly_sales_data)
    + number_of_future_months
).reshape(-1, 1)

future_sales_predictions = (
    sales_forecasting_model.predict(
        future_month_numbers
    )
)

future_dates = pd.date_range(
    start=monthly_sales_data["Date"].max(),
    periods=number_of_future_months + 1,
    freq="MS"
)[1:]

forecast_results = pd.DataFrame({
    "Forecast_Date": future_dates,
    "Predicted_Sales": future_sales_predictions
})

# Forecast Table

st.subheader("🔮 Next 6 Months Forecast")

st.dataframe(
    forecast_results
)

# Forecast KPI

st.metric(
    "Next Month Forecast",
    f"₹{forecast_results['Predicted_Sales'].iloc[0]:,.0f}"
)

# Historical vs Forecast Chart

st.subheader("📊 Historical & Forecast Sales")

historical_sales_chart = (
    monthly_sales_data
    .set_index("Date")["Sales"]
)

forecast_sales_chart = (
    forecast_results
    .set_index("Forecast_Date")
    ["Predicted_Sales"]
)

st.line_chart(
    pd.concat([
        historical_sales_chart,
        forecast_sales_chart
    ])
)

# Model Evaluation

predicted_training_sales = (
    sales_forecasting_model.predict(
        training_features
    )
)

average_prediction_error = (
    mean_absolute_error(
        actual_sales,
        predicted_training_sales
    )
)

model_accuracy_score = (
    r2_score(
        actual_sales,
        predicted_training_sales
    )
)

st.subheader("📈 Model Performance")

column_1, column_2 = st.columns(2)

with column_1:
    st.metric(
        "Average Prediction Error",
        f"₹{average_prediction_error:,.2f}"
    )

with column_2:
    st.metric(
        "Model Accuracy Score",
        f"{model_accuracy_score:.2f}"
    )

# Business Insights

st.subheader("🧠 Business Insights")

predicted_growth_percentage = (
    (
        forecast_results[
            "Predicted_Sales"
        ].iloc[-1]
        -
        forecast_results[
            "Predicted_Sales"
        ].iloc[0]
    )
    /
    forecast_results[
        "Predicted_Sales"
    ].iloc[0]
) * 100

if predicted_growth_percentage > 0:
    st.success(
        f"📈 Sales expected to grow by "
        f"{predicted_growth_percentage:.2f}% "
        f"over the next 6 months."
    )
else:
    st.warning(
        f"📉 Sales expected to decline by "
        f"{abs(predicted_growth_percentage):.2f}% "
        f"over the next 6 months."
    )

# Save Forecast

forecast_results.to_csv(
    r"C:\Users\vansh soni\PROJECT_2\data\processed\sales_forecast.csv",
    index=False
)

# Download Forecast Report

forecast_report_csv = (
    forecast_results.to_csv(
        index=False
    )
)

st.download_button(
    label="📥 Download Forecast Report",
    data=forecast_report_csv,
    file_name="sales_forecast.csv",
    mime="text/csv"
)