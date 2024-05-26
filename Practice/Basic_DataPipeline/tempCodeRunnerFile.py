import pyodbc as pyodbc

# Connect to MS SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-JMHKIQOF;'
                      'Database=AdventureWorks2022;'
                      'Trusted_Connection=yes;'
                      )

# Create a cursor
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT TOP 1 * FROM HumanResources.Employee")

# Fetch the results
data = cursor.fetchall()

import pandas as pd
df = pd.DataFrame(data)
df