from binance.client import Client
import pandas as pd
from pprint import pprint
from binance.enums import *
import time

cred = pd.read_csv("credentials.csv", index_col=0).loc["binance", :]
client = Client(cred.api_key, cred.secret_key)
SYMBOL = "XRPUSDT"

# 현물 Order
def simulate_orders():
    # 주문생성

    # Limit order
    order = client.create_order(
        symbol='XRPUSDT',
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=30,
        price='0.35')
    pprint(order)

    # Market order
    # order = client.order_market_buy(
    #     symbol=SYMBOL,
    #     quantity=30)
    # pprint(order)

    time.sleep(5)

    # 주문취소
    order = client.cancel_order(
        symbol='XRPUSDT',
        orderId=order['orderId'])
    pprint(order)

    # 과거 cancel order까지 다보여줌
    order = client.get_all_orders(symbol=SYMBOL, limit=10)
    pprint(order)

    # 현재 미체결 order들만
    order = client.get_open_orders(symbol=SYMBOL)
    pprint(order)


# Account
def account_func():
    print("Account 보유정보")
    info = client.get_account()
    pprint(info)

    print("개별코인 보유정보")
    balance = client.get_asset_balance(asset='LTC')
    pprint(balance)

    print("계좌 상태") # {'msg': 'Normal', 'success': True}
    status = client.get_account_status()
    pprint(status)

    print("거래내역 정보, 주문정보 제외 실제 체결된 내역만")
    trades = client.get_my_trades(symbol=SYMBOL)
    pprint(trades)

    print("fee 정보, 내가 지불한 fee에 대한 내역 아님...!")
    fees = client.get_trade_fee(symbol=SYMBOL)
    pprint(fees)




if __name__ == "__main__":
    # simulate_orders()
    account_func()