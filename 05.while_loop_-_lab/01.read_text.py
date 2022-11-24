# Напишете програма, която чете текст от конзолата(стринг) и го принтира, докато не получи командата "Stop"

while True:
    name = input()
    if name == 'Stop':
        break
    print(name)