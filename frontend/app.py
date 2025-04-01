import streamlit as st
from add_update_delete_ui import add_update_tab
from analytics_category_ui import analytics_category_tab
from analytics_months_ui import analytics_months_tab
from month_category_ui import analytics_month_category

st.title("Expense Management System")

tab1, tab2, tab3, tab4 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months", "Monthly and Category Wise Analytics"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()

with tab4:
    analytics_month_category()
