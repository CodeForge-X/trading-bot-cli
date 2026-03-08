from . import client
import rich.console
import rich.table

#This is the main function called from cli which places appropriate order depending upon user input
def order(api_key,api_secret,symbol,side,ot,quantity,price):
    if side.lower() == "buy":
        if ot.lower() == "market":
            print_input(symbol,side,ot,quantity,0)
            testorder = client.market_order_buy(api_key,api_secret,symbol,quantity)
            if testorder is not None:
                print_summary(testorder)
            return testorder
        elif ot.lower() == "limit":
            print_input(symbol,side,ot,quantity,price)
            testorder = client.limit_order_buy(api_key,api_secret,symbol,quantity,price)
            if testorder is not None:
                print_summary(testorder)
            return testorder
    elif side.lower() == "sell":
        if ot.lower() == "market":
            print_input(symbol,side,ot,quantity,0)
            testorder = client.market_order_sell(api_key,api_secret,symbol,quantity)
            if testorder is not None:
                print_summary(testorder)
            return testorder
        elif ot.lower() == "limit":
            print_input(symbol,side,ot,quantity,price)
            testorder = client.limit_order_sell(api_key,api_secret,symbol,quantity,price)
            if testorder is not None:
                print_summary(testorder)
            return testorder

#This places test order, used only for debugging
def test_order(api_key,api_secret):
    testorder = client.test_order(api_key,api_secret)
    if testorder is not None:
        print_summary(testorder)
    return testorder

#This prints the order summary in enhanced UI from rich module
def print_summary(testorder):
    console = rich.console.Console()
    table = rich.table.Table(title="Order Response Details")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="magenta")
    
    table.add_row("Order ID", str(testorder.get('orderId')))
    table.add_row("Status", testorder.get('status'))
    table.add_row("Executed Qty", testorder.get('executedQty', 'N/A'))
    
    console.print(table)

#This prints the user inputs in enhanced UI from rich module
def print_input(symbol,side,ot,quantity,price):
    console = rich.console.Console()
    table = rich.table.Table(title="Order Input Details")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="magenta")
    
    table.add_row("Symbol", symbol)
    table.add_row("Side", side.upper())
    table.add_row("Order Type", ot.upper())
    table.add_row("Quantity",str(quantity))

    if ot.lower() == "limit":
        table.add_row("Price", str(price))
    
    console.print(table)
