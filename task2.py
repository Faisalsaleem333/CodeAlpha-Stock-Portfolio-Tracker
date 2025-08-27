# 📈 Stock Portfolio Tracker
# Developed by Faisal Saleem for CodeAlpha Internship Project

# Predefined stock prices (you can add more)
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOGL": 2800, # Google
    "MSFT": 310,   # Microsoft
    "AMZN": 135    # Amazon
}

portfolio = {}  # Dictionary to store user's portfolio

print("📈 Welcome to Stock Portfolio Tracker 📊")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when you are finished.\n")

# User input loop
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not found! Please choose from available stocks.")
        continue
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        if qty <= 0:
            print("❌ Quantity must be greater than 0.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("❌ Please enter a valid number for quantity.")

# Calculation
total_value = 0
result_lines = []
result_lines.append("\n📊 Your Portfolio Summary:\n")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    result_lines.append(f"{stock} - {qty} shares × ${price} = ${value}")

result_lines.append(f"\n💰 Total Investment Value = ${total_value}")

# Display on console
print("\n".join(result_lines))

# Save to file
with open("portfolio.txt", "w") as f:
    f.write("\n".join(result_lines))

print("\n✅ Portfolio saved to 'portfolio.txt'")
