# Отговаряте за логистиката на различни товари. В зависимост от теглото на товара е нужно различно превозно средство.
# Цената на тон, за която се превозва товара е различна за всяко превозно средство:
# •	До 3 тона – микробус (200 лева на тон)
# •	От 4 до 11 тона – камион (175 лева на тон)
# •	12 и повече тона – влак (120 лева на тон)
# Вашата задача е да изчислите средната цена на тон превозен товар, както и процента на тоновете
# превозвани с всяко превозно средство, спрямо общото тегло(в тонове) на всички товари.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на товарите за превоз – цяло число в интервала [1...1000]
# •	За всеки един товар на отделен ред – тонажа на товара – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 4 реда, както следва:
# •	Първи ред – средната цена на тон превозен товар (закръглена до втория знак след дес. запетая);
# •	Втори ред – процентът тона превозвани с микробус (процент между 0.00% и 100.00%);
# •	Трети ред – процентът  тона превозвани с камион (процент между 0.00% и 100.00%);
# •	Четвърти ред – процентът тона превозвани с влак (процент между 0.00% и 100.00%).
cargo_num = int(input())

bus_cargo = 0
truck_cargo = 0
train_cargo = 0
cargo_price = 0
total_cargo_tons = 0
for i in range(cargo_num):
    current_cargo_tons = int(input())
    total_cargo_tons += current_cargo_tons
    if current_cargo_tons <= 3 :
        cargo_price += current_cargo_tons * 200
        bus_cargo += current_cargo_tons
    elif current_cargo_tons >= 12 :
        cargo_price += current_cargo_tons * 120
        train_cargo += current_cargo_tons
    else:
        cargo_price += current_cargo_tons * 175
        truck_cargo += current_cargo_tons
average_ton_price = cargo_price / total_cargo_tons
print(f"{average_ton_price:.2f}")
print(f"{bus_cargo/total_cargo_tons*100:.2f}%")
print(f"{truck_cargo/total_cargo_tons*100:.2f}%")
print(f"{train_cargo/total_cargo_tons*100:.2f}%")