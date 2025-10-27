# TODO: Your code here
found_number = False

for number in range(1, 101):
    print(f'Checking number: {number}')
    if number % 7 == 0 and number % 13 == 0 :
        found_number = True
        print(f'Found {found_number}!')
        break  # Exit loop immediately
    print(f'Still inside loop, checking next...')  # This runs before break

print(found_number)