# Запрашиваем сумму у пользователя
bill_amount = float(input("Введите сумму счёта в рублях: "))

# Запрашиваем информацию о % оставляемых на чай
# Сразу выводим значение
tips = int(input("Сколько % на чай вы хотите оставить? 10, 15, 20? : "))
if tips == 10:
    tip_10 = round(bill_amount * 0.10, 2)
    total_with_10 = round(bill_amount + tip_10, 2)
    print(f"Сумма вашего счёта = {bill_amount}, сумма чаевых 10% = {tip_10}. Итого к оплате: {total_with_10}")
elif tips == 15:
    tip_15 = round(bill_amount * 0.15, 2)
    total_with_15 = round(bill_amount + tip_15, 2)
    print(f"Сумма вашего счёта = {bill_amount}, сумма чаевых 15% = {tip_15}.  Итого к оплате: {total_with_15}")
elif tips == 20:
    tip_20 = round(bill_amount * 0.20, 2)
    total_with_20 = round(bill_amount + tip_20, 2)
    print(f"Сумма вашего счёта = {bill_amount}, сумма чаевых 20% = {tip_20}.  Итого к оплате: {total_with_20}")
else:
    print("Ошибка: введите только 10, 15 или 20.")