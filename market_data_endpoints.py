from binance.client import Client
import pandas as pd
from pprint import pprint

cred = pd.read_csv("credentials.csv", index_col=0).loc["binance", :]
client = Client(cred.api_key, cred.secret_key)
# client.FUTURES_URL = 'https://dapi.binance.com/dapi'
SYMBOL = "BTCUSD"

print(client.ping())

# 서버타임
time_res = client.get_server_time()
print(time_res)

# 서버 상태
status = client.get_system_status()
print(status)

#서버 정보
info = client.get_exchange_info()
# print(info)
for i in info.keys():
    print(i)

info = client.get_symbol_info("BTCUSDT")
print(info)


tickers = client.get_ticker()
print(tickers[0])
print([t["symbol"] for t in tickers])

depth = client.get_order_book(symbol=SYMBOL,limit= 10)
print(depth["bids"], depth["asks"]) # 100단위 호가를 줌..!

trades = client.get_recent_trades(symbol=SYMBOL)
# pprint(len(trades)) # 최근 500틱

h_trades = client.get_historical_trades(symbol=SYMBOL)
# pprint(len(h_trades)) # 최근 500틱? 위 함수랑 무슨 차이지

# Aggregate Trade Iterator ( Backtesting 할때 써먹으면 딱일듯! Generator!)
agg_trades = client.aggregate_trade_iter(symbol=SYMBOL, start_str='1 years ago UTC')
# for i, trade in enumerate(agg_trades):
#     print(i, trade)

# Kline Generator ( Backtesting ㄱㄱ)
# for kline in client.get_historical_klines_generator("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
#     print(kline)
    # do something with the kline

# Kline Historical
# fetch 30 minute klines for the last month of 2017
klines = client.get_historical_klines(symbol=SYMBOL, interval= Client.KLINE_INTERVAL_30MINUTE)
print(klines[0])

# SYMBOL, Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2020", "1 Jan, 2021"