# Напишете програма, която прочита скрито съобщение в поредица от символи.
# Те се получават по един на ред до получаване на командата "End".
# Думите се образуват от буквите в реда на четенето им.
# Символите, които не са латински букви трябва да бъдат игнорирани.
# Думите скрити в потока са разделени от тайна команда от три букви – "c", "o" и "n".
# При първото получаване на една от тези букви, тя се маркира като срещната, но не се запазва в думата.
# При всяко следващо нейно срещане се записва нормално в думата.
# След като са налични и трите символа от командата, се печата думата и интервал " ".
# Започва се нова дума, която по същия начин чака тайната команда, за да бъде отпечатана.
# Вход
# От конзолата се чете поредица от редове с един символ на всеки до получаване на командата "End".
# Изход
# На конзолата се печата на един ред всяка дума след тайната команда, следвана от интервал.
letter = input()
message = ''
c_count = 0
o_count = 0
n_count = 0
letter_check =0
end_words =''

while letter != 'End':
    #преверка дали да се добавя към massage 65-90 ABC, 97-122 abc
    if c_count > 0 and o_count > 0 and n_count > 0:
        end_words += str(message) + " "
        c_count = 0
        o_count = 0
        n_count = 0
        message= ''
    letter_check = ord(letter)
    if 65 <= letter_check <= 90 or 97 <= letter_check <= 122 :
        if letter == "c" and c_count ==0:
            c_count += 1
            letter = input()
            continue
        elif letter == 'o' and o_count == 0:
            o_count += 1
            letter = input()
            continue
        elif letter == 'n' and n_count == 0:
            n_count += 1
            letter = input()
            continue

        message += str(letter)
    # if c_count >0 and o_count>0 and n_count >0:
    #     end_words += str(message) + " "
    #     c_count = 0
    #     o_count = 0
    #     n_count = 0
    #     message= ''

    letter = input()
if c_count >0 and o_count>0 and n_count >0:
    end_words += str(message) + " "
print(f'{end_words} ')