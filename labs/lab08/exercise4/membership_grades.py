# exercise 4

membership = 120
personal_training = 80
training_sessions = 6
locker_rental = 25
towel_service = 15
one_time_regitration = 50

total_training_cost = personal_training * training_sessions
first_month_cost = ( membership + total_training_cost + locker_rental + towel_service + one_time_regitration )
monthly_cost = membership + total_training_cost + locker_rental + towel_service
annual_cost = first_month_cost + (monthly_cost - one_time_regitration) * 11

print(f"First-month cost: {first_month_cost}")
print(f"Monthly cost after first month: {monthly_cost}")
print(f"Annual cost: {annual_cost}")
