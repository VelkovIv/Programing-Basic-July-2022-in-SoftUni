import math

balls_number = int(input())
point_counter = 0
devided_counter = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_color_balls = 0

for balls in range(balls_number):
    color = input()
    if color == 'red':
        point_counter +=5
        red_balls += 1
    elif color == 'orange':
        point_counter += 10
        orange_balls += 1
    elif color == 'yellow':
        point_counter += 15
        yellow_balls += 1
    elif color == 'white':
        point_counter += 20
        white_balls += 1
    elif color == 'black':
        point_counter = math.floor(point_counter/2)
        devided_counter += 1
    else:
        other_color_balls += 1
print(f"Total points: {point_counter}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_color_balls}")
print(f"Divides from black balls: {devided_counter}")
