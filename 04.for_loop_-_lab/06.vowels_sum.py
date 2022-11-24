# Да се напише програма, която чете текст (стринг), въведен от потребителя, и изчислява и отпечатва сумата от
# стойностите на гласните букви според таблицата по-долу:
# буква	    a	e	i	o	u
# стойност	1	2	3	4	5
some_text = input()
vowels_sum = 0
for _ in range(len(some_text)):
    if some_text[_] == "a":
        vowels_sum += + 1
    elif some_text[_] == "e":
        vowels_sum += + 2
    elif some_text[_] == "i":
        vowels_sum += + 3
    elif some_text[_] == "o":
        vowels_sum += + 4
    elif some_text[_] == "u":
        vowels_sum += + 5
print(vowels_sum)