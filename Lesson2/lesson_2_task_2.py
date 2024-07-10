requirеd_year= input("Введите год: ")
year = int(requirеd_year)
def is_year_leap():
    if year % 4 == 0:
        print("Год", year, ":", True)
    else:
        print("Год", year, ":", False)
is_year_leap()