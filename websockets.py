from binance.websockets import BinanceSocketManager
from binance.client import Client
import pandas as pd
from pprint import pprint
import time
from twisted.internet import reactor

cred = pd.read_csv("credentials.csv", index_col=0).loc["binance", :]
client = Client(cred.api_key, cred.secret_key)
SYMBOL = "BTCUSDT"

bm = BinanceSocketManager(client, user_timeout=60)

def process_message(msg):
    if msg['e'] == 'error':
        pprint("message type: {}".format(msg['e']))
        # close and restart the socket
    else:
        # process message normally
        # print("message type: {}".format(msg['e']))
        pprint(msg)
        # do something


def process_raw_message(msg):
    pprint(f"A: {(msg['a'][0])}")
    pprint(f"B: {(msg['b'][0])}")
    # pprint(msg)


# trade data socket
# conn_key_trade = bm.start_trade_socket(SYMBOL, process_m_message)

# depth data socket
# conn_key_depth_partial = bm.start_depth_socket(SYMBOL, process_raw_message, depth=BinanceSocketManager.WEBSOCKET_DEPTH_5)
# conn_key_depth_diff = bm.start_depth_socket(SYMBOL, process_raw_message)

# 체잔 socket (for 현물, 마진)
# conn_key_spot_trade = bm.start_user_socket(process_message)
# conn_key_fut_cross_trade = bm.start_margin_socket(process_message)
# conn_key_fut_iso_trade = bm.start_isolated_margin_socket(SYMBOL, process_message)


# 체결 socket
# aggtrade : "Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same price will have the quantity aggregated."

# conn_key_agg = bm.start_aggtrade_socket(SYMBOL, process_message)
# conn_key_trade = bm.start_trade_socket(SYMBOL, process_message)

# conn_key_fut_agg = bm.start_aggtrade_futures_socket(SYMBOL, process_raw_message)
#
conn_key_depth = bm.start_depth_socket(SYMBOL, process_raw_message)
# conn_key_fut_depth = bm.start_depth_futures_socket(SYMBOL, process_raw_message)


# multiplex_socket
# conn_key_multi = bm.start_multiplex_socket(['btcusdt@aggTrade', 'btcusdt@ticker'], process_m_message)

bm.start()
# time.sleep(10)

# conn_key 하나에 대해서 작동을 중지 할수있다.
# bm.stop_socket(conn_key)

# # 쓰레드만 종료, 다시 키려면 다시 설정 전부해줘야함.
# bm.close()

# print("restart")
#
# time.sleep(10)
#
# # 아예 코드가 종료됨
# reactor.stop()

# if websocket gets disconnected!
# {
#     'e': 'error',
#     'm': 'Max reconnect retries reached'
# }
