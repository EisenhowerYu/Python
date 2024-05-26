# Python Extract Load Transform data from online sources

# import libs
import requests
import pandas as pd
from sqlalchemy import create_engine

# Extract
def extract()-> dict:
    print("Extracting data from online...")
    API_URL = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/rates_of_exchange?fields=country_currency_desc,exchange_rate,record_date&filter=country_currency_desc:in:(Canada-Dollar,Mexico-Peso),record_date:gte:2020-01-01"
    data = requests.get(API_URL).json()
    return data

# Transform
def transform(data:dict) -> pd.DataFrame:
    print("Transforming data into a dataframe...")
    df = pd.DataFrame(data)
    return df

# Load
def load(df:pd.DataFrame) -> None:
    print("Loading into sqlite db")
    disk_engine = create_engine('sqlite://my_db')
    df.to_sql('tmp', disk_engine, if_exists="replace")

data = extract()
df = transform(data)
print(df)