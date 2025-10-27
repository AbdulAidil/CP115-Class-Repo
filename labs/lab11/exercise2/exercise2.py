num_days = int(input())
temperature = int(input())
danger_threshold = float(input())
danger_days = ""

# TODO: Your code here
# Use input() inside the loop to get each day's temperature

if temperature > danger_threshold:
    average_temp = temperature / num_days
print(danger_days)
print(f"{average_temp:.1f}")