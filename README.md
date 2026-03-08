# Binance Futures CLI Trading Bot

A command-line trading bot written in Python for placing Binance Futures orders.  
The program validates user inputs and executes market or limit orders through the Binance API.

---

## Features

- Command-line interface using argparse
- Supports MARKET and LIMIT orders
- BUY and SELL order types
- Symbol validation using Binance Futures exchange info
- Input validation for side, order type, quantity, and price
- Logging of successful and failed orders
- Rich formatted output tables for order details
- Uses Binance Futures Testnet

---

## Project Structure

trading_bot/
├── README.md
├── bot
│   ├── __init__.py
│   ├── client.py
│   ├── logging_utils.py
│   ├── orders.py
│   └── validator.py
├── cli.py
└── requirement.txt

---

## Installation

Clone the repository and install dependencies.
```
pip install -r requirements.txt
```

---

## Usage

Run the CLI program from the project root.

```
python cli.py SYMBOL SIDE ORDER_TYPE QUANTITY [-price PRICE]
```

---

### Example Market Order

```
python cli.py BTCUSDT BUY MARKET 1
```

---

### Example Limit Order

```
python cli.py BTCUSDT BUY LIMIT 1 -price 30000
```

---

## Parameters

SYMBOL
Trading pair symbol (example: BTCUSDT)

SIDE
BUY or SELL

ORDER_TYPE
MARKET or LIMIT

QUANTITY
Number of contracts to trade

PRICE
Required only for LIMIT orders

---

## Notes

- The program uses Binance Futures Testnet.
- Valid API key and secret are required.
- The program exits if input validation fails.

---

## Dependencies

- python-binance
- rich
