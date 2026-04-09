# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"Added {stock}: ₹{value}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: ₹", total_investment)

# Optional: Save to file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: ₹{total_investment}")