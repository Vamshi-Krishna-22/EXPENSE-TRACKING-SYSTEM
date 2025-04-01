import streamlit as st # for web applications
from datetime import datetime # for default date value for the date date input field
import requests # for sending http request(get, post) postman


API_URL = "http://localhost:8000"
# this is the base url for the fastapi backend
# In this tab we done only get request part that is adding or updating the data
# in simple wordes in the db_helper we have three fuctions
# fetch, delete, update data for the particular date

def add_update_tab():
# this is the function named add_update_tab which will be used in our app.py
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    # this is for slecting a date to fetch or update expenses for that day.
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    #  this request fetches the expenses for the selected date
    if response.status_code == 200:
        existing_expenses = response.json()
        # st.write(existing_expenses)
    else:
        st.error("failed to retrieve expenses")
        existing_expenses = []
    # error handling for expense retrieval

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
    # expenses categories list
    with st.form(key="expense_form"):
        # in this we created form container
        # inside this block, all ui elements are grouped together as part of this form
        # key=expense form : form's unique identifier
        col1, col2, col3 = st.columns(3)
        # st.columns divides the layout into 3 equal-width columns
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")
        # with blocks specifies what goes inside each column

        expenses = [] # created empty list of expenses
        for i in range(5): # creates 5 rows for expense entry
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']
            # this field brighs existing values in the exsiting expenses
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""
            # this fills the non existing values as default values
            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}",
                                               label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category),
                                              key=f"category_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")
            # efficiently collects data with proper input value types
            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })
        #     this line collects the user's input data from the fields and append it to the expense list.
        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]

            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses updated successfully!")
            else:
                st.error("Failed to update expenses.")
        # created submit button and ensures only valid data is submited and handles errors gracefully