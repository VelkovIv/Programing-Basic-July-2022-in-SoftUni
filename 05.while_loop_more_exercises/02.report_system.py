# На благотворително събитие плащанията за закупените продукти винаги се редуват: плащане в брой и плащане с карта.
# Установени са следните правила за заплащане:
# •	Ако продуктът надвишава 100лв., за него не може да се плати в брой
# •	Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
# Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.
# Вход
# От конзолата се четат:
# •	Сумата, която се очаква да бъде събрана от продажбите - цяло число в интервала [1 ... 10000]
# На всеки следващ ред, до получаване на командата "End" или докато не се съберат нужните средства:
# цените на предметите, които ще бъдат закупени - цяло число в интервала [1 ... 500]
# Изход
# На конзолата да се отпечата:
# •	При успешна транзакция: "Product sold!"
# •	При неуспешна транзакция: "Error in transaction!"
# •	Ако сумата на всички закупени продукти надвиши или достигне очакваната сума,
# програмата трябва да приключи и на конзолата да се изпишат два реда:
# o	"Average CS: {средно плащане в кеш на човек}"
# o	"Average CC: {средно плащане с карта на човек}"
#               Плащанията трябва да бъдат форматирани до втората цифра след десетичния знак.
# •	При получаване на команда "End", да се изпише един ред:
# o	"Failed to collect required money for charity."
charity_amount = int(input())
collected_money = 0
counter = 0
cash_payments = 0
card_payment = 0
average_cash_payment = 0
average_card_payment = 0
card_payment_num = 0

while True:
    item_price = input()
    if item_price == 'End':
        if collected_money >= charity_amount:
            average_cash_payment = (collected_money - card_payment) / cash_payments
            average_card_payment = card_payment / (counter - card_payment)
            print(f"Average CS: {average_cash_payment:.2f}")
            print(f"Average CC: {average_card_payment:,2f}")
            break
        else:
            print("Failed to collect required money for charity.")
            break
    item_price = int(item_price)
    counter +=1
    if counter % 2 == 0:
        if item_price < 10:
            print("Error in transaction!")
            continue
        else:
            card_payment += item_price
            card_payment_num += 1
    else:
        if item_price > 100:
            print("Error in transaction!")
            continue
        else:
            cash_payments += 1
    collected_money += item_price
    print("Product sold!")
    if collected_money >= charity_amount:
        average_cash_payment = (collected_money - card_payment) / cash_payments
        average_card_payment = card_payment / card_payment_num
        print(f"Average CS: {average_cash_payment:.2f}")
        print(f"Average CC: {average_card_payment:.2f}")
        break


