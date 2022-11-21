# Напишете програма, която чете от конзолата число r и пресмята и отпечатва лицето и периметъра на кръг
# / окръжност с радиус r, като форматирате изхода в следния вид: "<calculated area>"
# "<calculated parameter>". Форматирайте изходните данни до втория знак след десетичната запетая.
import math

radius = float(input())
area = math.pi * radius ** 2
perim = 2 * math.pi * radius
print(f"{area:.2f}")
print(f"{perim:.2f}")