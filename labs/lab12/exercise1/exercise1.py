price = float(input("Enter price (put (-ve) number to stop): "))

# TODO: Your code here
total_cost = 0 
item_count = 0

while price >= 0:
    total_cost += price
    item_count += 1
    price = float(input("Enter price (put (-ve) number to stop): "))

print(f"Item count :{item_count}")
print(f"Total cost :{total_cost:.2f}")
