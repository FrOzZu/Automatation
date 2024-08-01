import math

def square(side):
    area = side * side
    
    # Если сторона не целая, округляем площадь вверх
    if not side.is_integer():
        area = math.ceil(area)
    
    return area

try:
    side_string = input("Введите длину стороны квадрата: ")
    side_length = float(side_string)
    result = square(side_length)
    print(f"Площадь квадрата со стороной {side_length} равняется {result}")
except ValueError as e:
    print(f"Ошибка: {e}")