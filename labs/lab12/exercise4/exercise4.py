score_input = input("Enter your score: ")

# TODO: Your code here
passing_count = 0 
failing_count = 0
score = 0

while score_input != "end":
    passing_count += score
    score_input += 1

    if score_input >= 60:
        passing_count += 1
    else :
        failing_count += 1

    score_input = input("Enter you score: ")

total_count = passing_count + failing_count
pass_rate = ( passing_count / total_count ) * 100

print(f"Total pass : {passing_count}")
print(f"Total fail : {failing_count}")
print(f"Overall pass rate percentage : {pass_rate:.2f}")

print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")
