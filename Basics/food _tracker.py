# food tracker
food = ['Rice', 'Eggs', 'Beef', 'Vegetables', 'Yam', 'Potato', 'Beans', 'Garri', 'Plantain', 'Maize']
prices = [50000, 5000, 10000, 3000, 20000, 10000, 30000, 5000, 4000, 7000]

print("           FOOD ITEMS           ")
print("________________________________________")

for index, items in enumerate(food, start=1):
    print(f"\n{index}. {items} - ₦{prices[index-1]}")

print("\n________________________________________")

# check minimum price
cheapest_price = min(prices)
cheapest_food = food[prices.index(cheapest_price)]
print(f"\nCheapest item: {cheapest_food} - ₦{cheapest_price}")
print("________________________________________")

# check maximum price
most_expensive_price = max(prices)
most_expensive_food = food[prices.index(most_expensive_price)]
print(f"\nMost-expensive item: {most_expensive_food} - ₦{most_expensive_price}")
print("________________________________________")

# total price
print(f"\nTotal: ₦{sum(prices)}")
