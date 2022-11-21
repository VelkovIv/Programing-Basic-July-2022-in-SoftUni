lenght = int(input())
width = int(input())
height = int(input())
persent = float(input())
volume = lenght * width * height
volume_lt = volume / 1000
remain_lt = volume_lt * (1 - persent / 100)
print(remain_lt)
