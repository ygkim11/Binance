from binance.client import Client
import pandas as pd
from pprint import pprint


cred = pd.read_csv("credentials.csv", index_col=0).loc["binance", :]
client = Client(cred.api_key, cred.secret_key)
SYMBOL = "BTCUSDT"


ticker = client.futures_ticker()
print(ticker)

klines = client.futures_klines(symbol=SYMBOL,
                               interval=Client.KLINE_INTERVAL_1DAY,
                               startTime=1546473600000,
                               endTime=1609632000000)
# print(len(klines))
# pprint(klines)

# [[1609459200000, '28948.19', '29668.86', '28627.12', '29337.16', '210716.398', 1609545599999, '6157505024.08511', 1511793, '101247.902', '2960175587.62208', '0'], [1609545600000, '29337.15', '33480.00', '28958.24', '32199.91', '545541.080', 1609631999999, '17122938614.70610', 3514545, '273388.463', '8578964529.70894', '0'], [1609632000000, '32198.41', '34832.25', '32000.02', '33054.53', '487486.989', 1609718399999, '16389111411.52760', 3325307, '238761.657', '8029365512.72767', '0']]

fund_rate = client.futures_funding_rate(symbol=SYMBOL,
                                       startTime=1568102400001,
                                       endTime=1612469148000,
                                        limit = 1000)
#
print(len(fund_rate))
pprint(fund_rate)

# futures_klines랑 그냥 같은 데이터 같음
continous_fut =client.futures_continous_klines(pair=SYMBOL,
                                contractType="PERPETUAL",
                                interval=Client.KLINE_INTERVAL_1DAY,
                                startTime = 1546473600000,  # 2021년 January 1일 Friday AM 12:00:00
                                endTime = 1609632000000)
# print(len(continous_fut))
# pprint(continous_fut)