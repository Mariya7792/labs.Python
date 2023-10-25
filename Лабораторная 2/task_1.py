money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = money_capital + salary
balance = budget - spend
months = 0

while balance > 0:
    if balance < 0:
        break
    months += 1
    spend *= 1 + increase
    balance = balance + salary - spend
print("Количество месяцев, которое можно протянуть без долгов:", months)
