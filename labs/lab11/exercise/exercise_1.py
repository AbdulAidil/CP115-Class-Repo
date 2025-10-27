# Count determined by user input
team_size = int(input("How many team members? "))
print(f"Registering {team_size} team members:")

for member in range(1, team_size + 1):
    name = input(f"Enter name for member {member}: ")
    print(f"Member {member}: {name} registered")

print("Team registration complete!")
print("")

# Count from calculation
months_in_year = 12
years = 3
total_months = months_in_year * years

print(f"Monthly report for {years} years:")
for month in range(1, total_months + 1):
    year_number = (month - 1) // 12 + 1
    month_in_year = (month - 1) % 12 + 1
    print(f"Month {month}: Year {year_number}, Month {month_in_year}")