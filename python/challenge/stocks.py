stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

print("Enter a quantity of stocks followed by stock symbol(s):")
num_items = int(input())

selected_stocks = []
total = 0

for i in range(num_items):
    selected_stocks.append(input().upper())

for item in selected_stocks:
    total += stocks[item]
    
print(f"Total price: ${total:.2f}")
