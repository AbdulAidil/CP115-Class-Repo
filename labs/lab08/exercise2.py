# BODMAS Exercise

main_dishes = 25
appetizers = 12
drinks = 8
charges = 0.1
delivery = 5

bill = (3*main_dishes) + (2*appetizers) + (4*drinks)
total_bill = (bill * charges) + delivery
amount = (total_bill + bill) / 6

print("The amount each person needs to pay :" ,int(amount))
