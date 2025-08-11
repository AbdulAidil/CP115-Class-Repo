print("Welcome to the Average Score Calculator!")
print("This program will display total and average score")

first_score = float(input("Enter your first score : "))
sec_score = float(input("Enter your second score : "))
third_score = float(input("Enter your third score : "))

total_score = first_score + sec_score + third_score
avg_score = total_score / 3

print("total score : " ,total_score)
print("Score average: " ,avg_score)