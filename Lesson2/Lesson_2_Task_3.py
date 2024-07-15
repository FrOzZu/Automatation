import math

def square(side):
    if not isinstance(side, int):
        side = math.ceil(side)
    
    area = side * side
    return area

side_string = input("Введите длину стороны квадрата: ")
side_length = float(side_string)
result = square(side_length)
print(f"Площадь квадрата со стороной {side_length} равняется {result}")