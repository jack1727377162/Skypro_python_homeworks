def bank(x, y):
    rate = 0.1
    future_sum = x * (1 + rate) ** y
    return future_sum
x = float(input("Какую сумму вы хотите положить на счет? "))
y = int(input("Сколько лет вы плаинруете держать дениги на счете? "))
result = bank(x, y)
print(f"Если вы положите {x} ₽ на {y} года/лет в наш банк, вы будите иметь {result:.2f} ₽ на вашем счету.")