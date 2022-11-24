# Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход.
# •	при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
# •	при въвеждане на правилна парола: отпечатваме "Welcome {username}!".
username = input()
password = input()
user_password = input()
while password != user_password:
    user_password = input()
print(f"Welcome {username}!")
