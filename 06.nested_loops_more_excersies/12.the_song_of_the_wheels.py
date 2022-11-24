control_value = int(input())
password =""
pass_counter = 0

for digit_one in range(1,10):
    for digit_two in range(1,10):
        for digit_three in range(1,10):
            for digit_four in range(1,10):
                if control_value == digit_one * digit_two + digit_three * digit_four and digit_one < digit_two and digit_three > digit_four:
                    print(f"{digit_one}{digit_two}{digit_three}{digit_four}", end = " ")
                    pass_counter += 1
                if pass_counter == 4:
                    password =str(digit_one)+str(digit_two)+str(digit_three)+str(digit_four)
                    password = int(password)
                    pass_counter +=1
print()
if password == "":
    print("No!")
else:
    print(f"Password: {password}")