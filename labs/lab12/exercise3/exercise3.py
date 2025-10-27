age_input = input("Enter your age (type done if you want to stop): ")

# TODO: Your code here
age_count = 0 
total_age = 0

while age_input != "done":
    age = int(age_input) 
    age_count += age
    total_age += 1
    age_input = input("Enter your age (type done if you want to stop): ")

average_age = age_count / total_age

print(f"Count of ages : {age_count}")
print(f"Total age : {total_age}")
print(f"Age average : {average_age:.2f}")
