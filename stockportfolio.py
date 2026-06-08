stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}

total = 0

print("Stock Portfolio Tracker")

while True:

    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:

        quantity = int(input(f"Enter quantity of {stock}: "))

        portfolio[stock] = quantity

    else:
        print("Stock not available.")

print("\nPortfolio Summary:")

for stock, quantity in portfolio.items():

    value = stock_prices[stock] * quantity

    total += value

    print(f"{stock} - {quantity} shares = ${value}")

print("Total Investment Value: $", total)