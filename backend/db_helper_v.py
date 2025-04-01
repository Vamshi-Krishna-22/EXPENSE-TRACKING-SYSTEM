import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

# creating a custom logger
logger = setup_logger("db_helper_v")

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()



def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with date {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with date {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called from {start_date} to {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total
            FROM expenses WHERE expense_date
            BETWEEN %s and %s
            GROUP BY category;''',
            (start_date,end_date)
        )
        data = cursor.fetchall()
        return data

def fetch_monthly_expense_summary():
    logger.info(f"fetch_monthly_expense_summary")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT month(expense_date) as expense_month, 
               monthname(expense_date) as month_name,
               sum(amount) as total FROM expenses
               GROUP BY expense_month, month_name;
            '''
        )
        data = cursor.fetchall()
        return data

def fetch_monthly_category_summary():
    logger.info(f"fetch_monthly_category_summary")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT 
                   YEAR(expense_date) AS expense_year,
                   MONTH(expense_date) AS expense_month_number,
                   MONTHNAME(expense_date) AS expense_month,
                   category,
                   SUM(amount) AS total 
               FROM expenses
               GROUP BY expense_year, expense_month_number, expense_month, category
               ORDER BY expense_year, 
                        FIELD(expense_month, 'January', 'February', 'March', 'April', 
                              'May', 'June', 'July', 'August', 'September', 'October', 
                              'November', 'December'),
                        category;
            '''
        )
        data = cursor.fetchall()
        return data


    # Transform data into structured format
    summary = {}
    for row in data:
        month_number = row["expense_month"]
        month_name = row["month_name"]
        category = row["category"]
        total = row["total"]

        if month_number not in summary:
            summary[month_number] = {
                "expense_month": month_number,
                "month_name": month_name,
                "total": 0,
                "categories": {}
            }

        summary[month_number]["categories"][category] = total
        summary[month_number]["total"] += total  # Update total expense for the month

    return list(summary.values())  # Convert dictionary to list




if __name__ == "__main__":
    # expenses = fetch_expenses_for_date("2024-08-01")
    # print(expenses)
    # insert_expense("2024-11-20", 300, "Food", "Panipuri")
    #  delete_expenses_for_date("2024-11-20")
    summary = fetch_monthly_category_summary()
    for row in summary:
        print(row)

