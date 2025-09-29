#Name : Abdul Aidil Shah Bin Ajibir
#This program asks the user to enter the monthly usage and then calculates and displays the amount.

#User enter the monthly usage
monthly_usage = float(input("Enter the monthly usage: RM " ))

#Determine the discount based on monthly usage
if monthly_usage > 100 :
    discount = 0.2
elif monthly_usage >=50 :
    discount = 0.05
else :
    discount = 0

#Calculate the amount
discounts = monthly_usage * discount
amount = monthly_usage - discounts

#displays the amount of the bill to be paid after receiving the discount.
print("Discount amount: RM", discounts)
print("Amount of the bill to be paid: RM", amount)