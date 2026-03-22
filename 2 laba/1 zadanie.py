money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0 # номер месяца
while True:
    money_capital = money_capital + salary - spend - spend * increase * month
    month = month + 1
    if money_capital + salary < spend + spend * increase * month:
        break


print("Количество месяцев, которое можно протянуть без долгов:",month-1)
