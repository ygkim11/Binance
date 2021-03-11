from binance.client import Client
import pandas as pd
from pprint import pprint

cred = pd.read_csv("credentials.csv", index_col=0).loc["binance", :]
client = Client(cred.api_key, cred.secret_key)
# client.FUTURES_URL = 'https://dapi.binance.com/dapi'
SYMBOL = "XRPUSDT"

# info = client.get_symbol_info(SYMBOL)
# pprint(info)

info = client.get_exchange_info()
pprint(info)