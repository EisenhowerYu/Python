import db_credentials as creds

conn = creds.conn
cursor = creds.cursor

cursor.execute("SELECT * FROM HumanResources.Department")

data = cursor.fetchall()

import pandas as pd

df = pd.read_sql("SELECT TOP 100 * FROM Person.Person", conn)

filename = 'Python/Basic_DataPipeline/Output.csv'
df.to_csv(filename, index=False)