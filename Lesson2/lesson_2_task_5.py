month = int(input("Введите порядковый номер месяца: "))
def month_to_season(month):
        if month in [12, 1, 2]:
            print("На дворе зима")
        elif month in [3, 4, 5]:
            print("На дворе весна")
        elif month in [6, 7, 8]:
             print("На дворе лето")
        elif month in [9, 10, 11]:
             print("На дворе осень")
        else:
             print("Неверный номер месяца")
month_to_season(month)