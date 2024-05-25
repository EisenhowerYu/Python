import pyodbc as pyodbc

# Connect to MS SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-JMHKIQOF;'
                      'Database=AdventureWorks2022;'
                      'Trusted_Connection=yes;'
                      )

# Create a cursor
cursor = conn.cursor()