def get_kpis(df):

    return {
        "total_sales": df["Sales"].sum(),
        "total_profit": df["Profit"].sum(),
        "total_orders": len(df),
        "avg_order_value": df["Sales"].mean()
    }