# Required library
# import pyodbc
import pandas as pd
import os
import datetime
from plyer import notification
from sqlalchemy import create_engine

# Change working directory
os.chdir(r"/Users/carlosinfante/Desktop/winc-academy/backend-course/backend-projects/5. EXCEL-SQL/uploadexcel-SQL-SQLAlchemy")

# Create SQL conection
'''
conn = pyodbc.connect(DRIVER="{SQL Server}",
                      SERVER="RAM-PC", DATABASE="amet")
'''
engine = create_engine("sqlite:///amet.db", echo=True)
# SQL command to retrieve data
comm1 = "SELECT * FROM paintings"
comm2 = "SELECT * FROM customers"
comm3 = "SELECT * FROM fans"

# Read data from SQL using pandas
df1 = pd.read_sql_query(comm1, con=engine)
df2 = pd.read_sql_query(comm2, con=engine)
df3 = pd.read_sql_query(comm3, con=engine)

# Export data to excel
with pd.ExcelWriter('amecillo.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Paintings')
    df2.to_excel(writer, sheet_name='Customers')
    df3.to_excel(writer, sheet_name='Fans')
