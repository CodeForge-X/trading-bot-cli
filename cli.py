import argparse
from bot import validator
from bot import orders
from bot import logging_utils

#Sets up log file
logging_utils.setup_logger()

#parser object
parser = argparse.ArgumentParser()

#Adding arguments to parser object
parser.add_argument("Symbol", help="Valid symbol in all caps")

parser.add_argument("Side", help="Side to trade. BUY/SELL")

parser.add_argument("Order_Type", help="Type of order. MARKET/LIMIT")

parser.add_argument("Quantity", type=int, help="Order quantity.")

parser.add_argument("-price", default=0, help="Limit order price.")

#Getting all arguments
args = parser.parse_args()

validator.side_check(args.Side)

validator.quantity_check(args.Quantity)

validator.ot_check(args.Order_Type)

validator.price_check(args.price,args.Order_Type)

#Get api key
api_key = input("Binance Api key: ")
api_secret = input("Binance Api secret: ")

validator.symbol_check(args.Symbol,api_key,api_secret)

#Place order
testorder = orders.order(api_key,api_secret,args.Symbol,args.Side,args.Order_Type,args.Quantity,args.price)
