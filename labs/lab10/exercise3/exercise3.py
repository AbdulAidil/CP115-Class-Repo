monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

# Your code here
if monthly_income >= 4000:
    approval = "approve"
else:
    approval = "disapprove"

if credit_score >= 700:
    interest_rate = 0.035
elif credit_score >= 600:
    interest_rate = 0.055
elif credit_score < 600:
    interest_rate = 0

max_loan_amount = 5*monthly_income

print(interest_rate)
print(max_loan_amount)
print(approval_status)