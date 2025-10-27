score = float(input("Enter your score : "))

# TODO: Your code here
score_count = 0 
total_score = 0

while score >= 0 and score <= 100:
    score_count += score
    total_score += 1
    score = float(input("Enter your score : "))

average_score = score_count / total_score
print(f"Score count : {score_count}")
print(f"Total score : {total_score}")
print(f"Score average : {average_score:.2f}")
