age = int(input("Enter your age: "))
accident_count = int(input("Enter your accident count: "))

# Your code here
if age<25:
    base_premium=2400
elif age<=50:
    base_premium=1800
elif age>50:
    base_premium=2000

if accident_count==0:
    penalty=0
    discount=0.01
elif accident_count<=2:
    penalty=300
elif accident_count>=3:
    penalty=600

final_premium=base_premium+penalty
discount_amount=discount*final_premium

print(f"base_premium   :{base_premium}")
print(f"final_premium  :{final_premium}")
print(f"discount_amount:{discount_amount}")