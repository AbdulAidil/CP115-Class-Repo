# Inefficient search - checks all 10 numbers even after finding target
#target = 7
#found = False

#for number in range(10):
#    print(f"Checking number: {number}")
#    if number == target:
#        found = True
#        print(f"Found {target}!")
#    # Loop continues even after finding target

#print(f"Search complete. Found: {found}")


#for item in range(100):
#    if condition:
#        break  # Exit loop immediately
    # This code runs only if break hasn't executed
# Python jumps here after break

# Efficient search - stops immediately after finding target
target = 12
found = False

for number in range(10):
    print(f'Checking number: {number}')
    if number == target:
        found = True
        print(f'Found {target}!')
        break  # Exit loop immediately
    print(f'Still inside loop, checking next...')  # This runs before break

print(f'Search complete. Found: {found}')  # Python jumps here after break