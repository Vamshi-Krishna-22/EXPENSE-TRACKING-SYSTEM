import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import uuid  # Import uuid to generate unique keys

API_URL = "http://localhost:8000"

def analytics_month_category():
    response = requests.get(f"{API_URL}/monthly_category_summary/")
    monthly_summary = response.json()

    # Convert API response into DataFrame
    df = pd.DataFrame(monthly_summary)

    # Fix column names
    df.rename(columns={
        "expense_year": "Year",
        "expense_month": "Month Name",
        "category": "Category",
        "total": "Total"
    }, inplace=True)

    st.title("📊 Yearly & Monthly Expense Breakdown by Category")

    # Group data by year and month
    for (year, month_name), group in df.groupby(["Year", "Month Name"]):
        st.subheader(f"📅 {month_name} {year}")

        # Create category-wise breakdown
        category_df = group[["Category", "Total"]].sort_values(by="Total", ascending=False)

        # Create a Plotly bar chart
        fig = px.bar(
            category_df,
            x="Category",
            y="Total",
            text="Total",
            labels={"Total": "Expense Amount", "Category": "Expense Category"},
            title=f"Expenses for {month_name} {year}"
        )
        fig.update_traces(textposition="outside")

        # ✅ Add a truly unique key using uuid
        st.plotly_chart(fig, use_container_width=True, key=f"{year}_{month_name}_{uuid.uuid4()}")
