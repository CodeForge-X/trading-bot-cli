import binance
from binance.enums import *
from . import logging_utils

#This retrieves symbols from the endpoint
def get_symbols(api_key,api_secret):
    client_setup = binance.Client(api_key,api_secret,testnet=True)
    exchange_info = client_setup.futures_exchange_info()
    all_symbols_data = exchange_info["symbols"]
    symbols = []

    for i in all_symbols_data:
        tmp_symbol = i["symbol"]
        symbols.append(tmp_symbol)
    return symbols

#This is just a test order and is not used anywhere in the code but only to debug
def test_order(api_key,api_secret):
    client_setup = binance.Client(api_key,api_secret,testnet=True)
    testorder = client_setup.futures_create_order(symbol="BTCUSDT",side=SIDE_BUY,type=ORDER_TYPE_MARKET, quantity=10)
    return testorder

#This sets up client and places buy market order
def market_order_buy(api_key,api_secret,symbol,quantity):
    try:
        client_setup = binance.Client(api_key,api_secret, testnet=True)
        testorder = client_setup.futures_create_order(symbol=symbol,side=SIDE_BUY,type=ORDER_TYPE_MARKET,quantity=quantity)
        logging_utils.log_info(f"SUCCESS: Order placed for {symbol}. Result: orderId = {testorder['orderId']}, executedQty = {testorder['executedQty']}, avgPrice = {testorder['avgPrice']}")
        return testorder
    except binance.BinanceAPIException as e:
        logging_utils.log_error(f"ERROR: Failed to place order for {symbol}. Details: {str(e)}")
        print(f"Order failed: {e.status_code} - {e.message}")

#This sets up client and places sell market order
def market_order_sell(api_key,api_secret,symbol,quantity):
    try:
        client_setup = binance.Client(api_key,api_secret, testnet=True)
        testorder = client_setup.futures_create_order(symbol=symbol,side=SIDE_SELL,type=ORDER_TYPE_MARKET,quantity=quantity)
        logging_utils.log_info(f"SUCCESS: Order placed for {symbol}. Result: orderId = {testorder['orderId']}, executedQty = {testorder['executedQty']}, avgPrice = {testorder['avgPrice']}")
        return testorder
    except binance.BinanceAPIException as e:
        logging_utils.log_error(f"ERROR: Failed to place order for {symbol}. Details: {str(e)}")
        print(f"Order failed: {e.status_code} - {e.message}")

#This sets up client and places buy limit order
def limit_order_buy(api_key,api_secret,symbol,quantity,price):
    try:
        client_setup = binance.Client(api_key,api_secret,testnet=True)
        testorder = client_setup.futures_create_order(symbol=symbol,side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=quantity,price=price)
        logging_utils.log_info(f"SUCCESS: Order placed for {symbol}. Result: orderId = {testorder['orderId']}, executedQty = {testorder['executedQty']}, avgPrice = {testorder['avgPrice']}")
        return testorder
    except binance.BinanceAPIException as e:
        logging_utils.log_error(f"ERROR: Failed to place order for {symbol}. Details: {str(e)}")
        print(f"Order failed: {e.status_code} - {e.message}")

#This sets up client and places sell limit order
def limit_order_sell(api_key,api_secret,symbol,quantity,price):
    try:
        client_setup = binance.Client(api_key,api_secret,testnet=True)
        testorder = client_setup.futures_create_order(symbol=symbol,side=SIDE_SELL,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=quantity,price=price)
        logging_utils.log_info(f"SUCCESS: Order placed for {symbol}. Result: orderId = {testorder['orderId']}, executedQty = {testorder['executedQty']}, avgPrice = {testorder['avgPrice']}")
        return testorder
    except binance.BinanceAPIException as e:
        logging_utils.log_error(f"ERROR: Failed to place order for {symbol}. Details: {str(e)}")
        print(f"Order failed: {e.status_code} - {e.message}")

