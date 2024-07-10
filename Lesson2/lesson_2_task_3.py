import math
def square(side):
    if not isinstance(side, int):
        side = math.ceil(side)
    square_area = side * side
    return square_area
side_string = input("Введите сторону квадрата: ")
side_length = float(side_string)
result = square(side_length)
print(f"Площадь квадрата составляет: {result} см²")
