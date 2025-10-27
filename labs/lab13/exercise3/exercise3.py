grade = float(input())

# TODO: Your code here
number = 0

while number < 101:
    number += 1  # Counter BEFORE continue

    if number % 2 != 0:  # If odd
        continue  # Skip odd numbers

    # This only executes for even numbers
    print(f"Processing even number: {number}")

print('valid_count')
print(f"{'average':.2f}")
