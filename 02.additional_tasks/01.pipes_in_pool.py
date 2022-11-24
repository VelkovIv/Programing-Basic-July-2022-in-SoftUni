# Басейн с обем V има две тръби от които се пълни.
# Всяка тръба има определен дебит (литрите вода минаващи през една тръба за един час).
# Работникът пуска тръбите едновременно и излиза за N часа.
# Напишете програма, която изкарва състоянието на басейна, в момента, когато работникът се върне.
# Вход
# От конзолата се четат четири реда:
# •	Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
# •	Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
# •	Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
# •	Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала [1.0…24.00]
# Изход
# Да се отпечата на конзолата едно от двете възможни състояния:
# •	До колко се е запълнил басейна и коя тръба с колко процента е допринесла.
# o	"The pool is {запълненост на басейна в проценти}% full. Pipe 1: {процент вода от първата тръба}%. Pipe 2: {процент вода от втората тръба}%."
# Aко басейнът се е препълнил – с колко литра е прелял за даденото време.
# o	"For {часовете, които тръбите са пълнили вода} hours the pool overflows with {литрите вода в повече} liters."
pool_volume_lt = int(input())
pipe1_debit_lt = int(input())
pipe2_debit_lt = int(input())
missing_workers_h = float(input())
pipe1_volume = pipe1_debit_lt * missing_workers_h
pipe2_volume = pipe2_debit_lt * missing_workers_h
total_volume_pipes = pipe1_volume + pipe2_volume
volume_pipe1 = pipe1_volume / total_volume_pipes * 100
volume_pipe2 = pipe2_volume / total_volume_pipes * 100
pool_fuliness = total_volume_pipes / pool_volume_lt * 100
diff = abs(pool_volume_lt - total_volume_pipes)
if pool_fuliness > 100:
    print(f"For {missing_workers_h:.2f} hours the pool overflows with {diff:.2f} liters.")
else:
    print(f"The pool is {pool_fuliness:.2f}% full. Pipe 1: {volume_pipe1:.2f}%. Pipe 2: {volume_pipe2:.2f}%.")