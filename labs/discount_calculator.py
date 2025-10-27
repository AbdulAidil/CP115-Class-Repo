#Movie discount in conjunction Deepavali festival
#This program determine the eligibility of individuals for discounts at a movie theater based on their age

#user input
age = int(input("Enter your age: "))
ticket_price = float(input("Enter the price of the movie ticket: "))

if age <= 0 or ticket_price < 0:
    print("Error: Age and ticket price cannot be negative.")
    exit()
else:
    if age <= 12:
        discount_rate = 0.5
        discount = "50% off"
        category = "Children"
    elif age <= 17:
        discount_rate = 0.25
        discount = "25% off"
        category = "Teenagers"
    else:
        discount_rate = 0
        discount = "No discount"
        category = "Adults"

#calculate final price
final_price = ticket_price - (ticket_price * discount_rate)

#print the if the user eligible
if discount_rate > 0:
    print(f"You are eligible for the {category} discount ({discount}).")
else:
    print(f"You are not eligible for any discount.")

print(f"Discounted ticket price: ${final_price:.2f}")