employee_name = input("emplyee name: ")
base_salary = float(input("base_salary: "))
overtime_hours = int(input("overtime_hours: "))
tax_status = input("tax status: ")
salary_tax = overtime_hours * 35 + base_salary
total_income = float(input("total income: "))
tax_rates = ""
EPF_rates = 0.11
SOSCO_rates= 0.005

# TODO your code here
if total_income >= 5000 and tax_status == "Single" :
    tax_rates = 0.22 
else :
    tax_rates = 0.18
if total_income >= 5000 and tax_status == "Married" :
    tax_rates = 0.2 
else :
    tax_rates = 0.15
if total_income >= 5500 and tax_status == "Head" :
    tax_rates = 0.25 
else :
    tax_rates = 0.19

EPF = total_income * EPF_rates
SOSCO = total_income * SOSCO_rates
tax = total_income * tax_rates
net = total_income - tax - EPF - SOSCO
net_salary = net + base_salary

print(employee_name)
print(tax_rates)
print(f"{net_salary:.2f}")