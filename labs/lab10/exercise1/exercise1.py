position = input("enter position: ")
overtime_hours = int(input("enter overtime_hours: "))
is_weekend = input("enter weekend: ")

# Your code here
if position=="manager":
    hourly_rate=35
elif position=="supervisor":
    hourly_rate=25
elif position=="staff":
    hourly_rate=18

if is_weekend==True:
    additional=5*overtime_hours
else:
    additional=0

overtime_rate=1.5*hourly_rate
overtime_pay=overtime_rate*overtime_hours
total_pay=overtime_pay + additional

print(hourly_rate)
print(overtime_pay)
print(total_pay)