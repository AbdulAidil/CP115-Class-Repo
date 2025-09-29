
employee_name = input("Employee name: ")
base_salary = float(input("Base salary: "))
overtime_hours = int(input("Overtime hours: "))
tax_status = input("Tax status (Single/Married/Head): ")

OVERTIME_RATE = 35
EPF_RATE = 0.11
SOSCO_RATE = 0.005

overtime_pay = overtime_hours * OVERTIME_RATE
total_income = base_salary + overtime_pay

if tax_status == "Single":
    tax_rate = 0.22 if total_income >= 5000 else 0.18
elif tax_status == "Married":
    tax_rate = 0.20 if total_income >= 6000 else 0.15
elif tax_status == "Head":
    tax_rate = 0.25 if total_income >= 5500 else 0.19
else:
    tax_rate = 0  # Default if status is invalid

# Deductions
epf = total_income * EPF_RATE
sosco = total_income * SOSCO_RATE
tax = total_income * tax_rate

# Net salary
net_salary = total_income - tax - epf - sosco

# Output
print("\n--- Salary Summary ---")
print(f"Employee Name: {employee_name}")
print(f"Total Income: RM{total_income:.2f}")
print(f"Tax Rate: {tax_rate * 100:.0f}%")
print(f"Net Salary: RM{net_salary:.2f}")
