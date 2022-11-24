days = int(input())
total_liters = 0
average_degree = 0
final_degree = 0

for rakia in range(1, days + 1):
    liters = float(input())
    degree = float(input())
    total_liters += liters
    average_degree += degree * liters
print(f"Liter: {total_liters:.2f}")
final_degree = average_degree / total_liters
print(f"Degrees: {final_degree:.2f}")
if final_degree < 38:
    print("Not good, you should baking!")
elif 38 <= final_degree <= 42:
    print("Super!")
elif final_degree > 42:
    print("Dilution with distilled water!")
