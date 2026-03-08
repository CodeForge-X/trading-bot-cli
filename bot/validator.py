from . import client
import sys

#This checks for valid symbols from all the symbols received
def symbol_check(symbol,api_key,api_secret):
    symbol_list = client.get_symbols(api_key,api_secret)

    if symbol in symbol_list:
        return
    print("Invalid symbol!")
    sys.exit()

#This check for valid side
def side_check(side):
    side_lower = side.lower()

    if side_lower in ["buy","sell"]:
        return
    else:
        print("Invalid side!")
        sys.exit()

#This checks for valid order type
def ot_check(ot):
    ot_lower = ot.lower()

    if ot_lower in ["market", "limit"]:
        return
    else:
        print("Order type invalid!")
        sys.exit()

#This checks for valid quantity
def quantity_check(quantity):
    if isinstance(quantity, int) and quantity>0:
        return
    else:
        print("Invalid quantity!")
        sys.exit()

#This checks for valid price as well as whether order type is limit or market
def price_check(price, order_type):
    try:
        val = float(price)
    except (ValueError, TypeError):
        print(f"Error: '{price}' is not a valid number.")
        sys.exit(1)
    if order_type.lower() == "limit":
        if val <= 0:
            print("Error: Limit orders must have a price greater than 0.")
            sys.exit(1)

