# <span style="color:  maroon">Expense Management System</span>

This project is an **expense management system** that consists of a **Streamlit frontend** application and a **FastAPI backend** server. It helps users track expenses efficiently, categorize spending, and analyze trends over time

## <span style = "color: maroon">Key features</span>
- **Add and Update expenses**
  ![](https://github.com/Vamshi-Krishna-22/EXPENSE-TRACKING-SYSTEM/blob/main/ADD%20AND%20UPDATE%20TAB.png)
- **Analytics by Category from selected date to selected date**
  ![](https://github.com/Vamshi-Krishna-22/EXPENSE-TRACKING-SYSTEM/blob/main/categroy%20wise%20analytics.png)
- **Analytics by Months**
  ![](https://github.com/Vamshi-Krishna-22/EXPENSE-TRACKING-SYSTEM/blob/main/monthly%20analytics.png)
- **Monthly and category wise analytics**
- ![](https://github.com/Vamshi-Krishna-22/EXPENSE-TRACKING-SYSTEM/blob/main/monthly%20category%20wise%20analytics.png)


## <span style = "color: maroon"> Project Structure </span>

- **frontend/**: Contains the  <span style="color:blue">Streamlit application</span> code.
- **backend/**: Contains the <span style="color:blue">FastAPI backend server</span> code.
- **tests/**: Contains the test cases for both <span style="color:blue">frontend and backend</span>.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## <span style = "color: maroon"> Setup Instructions </span>

1. **<span style="color:blue">Clone the repository: </span>**
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
2. **<span style="color:blue"> Install dependencies: </span>**   
   ```commandline
    pip install -r requirements.txt
   ```
3. **<span style="color:blue"> Run the FastAPI server: </span>** 
   ```commandline
    uvicorn server.server:app --reload
   ```
4. **<span style="color:blue"> Run the Streamlit app:</span>**   
   ```commandline
    streamlit run frontend/app.py
   ```
   

