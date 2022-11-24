# Напишете програма, която отпечатва класа на животното според неговото име, въведено от потребителя.
# 1.	dog -> mammal
# 2.	crocodile, tortoise, snake -> reptile
# 3.	others -> unknown
animal_type = input()
if animal_type == "dog":
    print("mammal")
elif animal_type == "crocodile" or animal_type == "tortoise" or animal_type == "snake":
    print("reptile")
else:
    print("unknown")