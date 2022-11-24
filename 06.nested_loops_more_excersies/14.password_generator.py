number_one = int(input())
number_two = int(input())

for one in range(1, number_one):
    for two in range(1 , number_one):
        for three in range(1, number_two + 1):
            for four in range(1, number_two + 1):
                for five in range(1, number_one + 1):
                    third = chr(three +96)
                    fourth = chr(four +96)
                    if five > one and five > two:
                        print(f"{one}{two}{third}{fourth}{five}", end = " ")