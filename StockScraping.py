import requests
import pandas as pd

api_key = input("Input your api key so loser bots can't steal it from my repo: ")
url = 'https://www.alphavantage.co/query'
ticker = 'AAPL'
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': ticker, 
    'apikey': api_key, 
    'outputsize': 'full'  # ~25 years
}

response = requests.get(url, params=params) #Alpha vantage api

if response.status_code != 200:
    raise ConnectionError(f"Fetch failiure; error code {response.status_code}")

data = response.json()

time_series = data['Time Series (Daily)']
df = pd.DataFrame.from_dict(time_series, orient='index')
df.index = pd.to_datetime(df.index)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

with open(f'{ticker}_Data.csv', '+w') as f:
    f.write(df.to_csv())

