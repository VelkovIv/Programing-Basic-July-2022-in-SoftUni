from math import pi

# print("square, rectangle, circle or triangle")
fugure = input()
ареа = 0
if fugure == "square" :
    side = float(input())
    area = side * side
elif fugure == "rectangle" :
    side = float(input())
    side1 = float(input())
    area = side * side1
elif fugure == "circle" :
    rad = float(input())
    area = pi * rad ** 2
else:
    side = float(input())
    height = float(input())
    area = side * height / 2
print(f"{area:.3f}")
