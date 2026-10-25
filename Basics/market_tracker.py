# market_tracker

items = ['Fan', 'refrigerator', 'TV', 'Micro-wave', 'Blender']

prices = [5000, 70000, 50000, 20000, 4000]

print("------ MARKET TRACKER ------")

for index , items in enumerate(items, start=1):
      print(f"\n{index}. {items} - ₦{prices[index-1]}")

# Find the cheapest item
print(f"\nCheapest: ₦{min(prices)}")
# Find the most expensive item
print(f"Most expensive: ₦{max(prices)}")
# calculate the total price of items
print(f"Total: ₦{sum(prices)}")
# calculate the average price
print(f"Average: ₦{sum(prices) / len(prices):.2f}")
