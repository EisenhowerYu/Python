# Python Extract Load Transform data from online sources
'''
Gets data from a public open api by the Treasury
The data is trasnformed from a json format into a dataframe
Then it is loaded into a sqlite database
'''

# import libs
import requests
import pandas as pd
from sqlalchemy import create_engine

# Extract
def extract()-> dict:
    print("Extracting data from online...")
    BASE_URL = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
    ENDPOINT = "/v1/accounting/od/rates_of_exchange"
    PARAMS = "?fields=country_currency_desc,exchange_rate,record_date"
    "&filter=country_currency_desc:in:(Canada-Dollar),record_date:gte:2019-01-01"

    API_URL = BASE_URL + ENDPOINT + PARAMS
    data = requests.get(API_URL).json()
    return data

# Transform
def transform(data:dict) -> pd.DataFrame:
    print("Transforming data into a dataframe...")
    df = pd.DataFrame(data['data'])
    return df

# Load
def load(df:pd.DataFrame) -> None:
    print("Loading into sqlite db")
    disk_engine = create_engine('sqlite:///lite.db')
    df.to_sql('tmp', disk_engine, if_exists="replace")

data = extract()
df = transform(data)
print(df)
load(df)


