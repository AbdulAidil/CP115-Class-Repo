correct_password = "python123"
login_successful = False
attempts_used = 0


for i in range(3):  # 3 attempts
    password = input('Enter password: ')
    attempts_used += 1
    
    if password == correct_password:
        login_successful = True
        break  # stop loop if correct

print(login_successful)
print(attempts_used)
