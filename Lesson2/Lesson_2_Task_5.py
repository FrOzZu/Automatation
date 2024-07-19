def month_to_season(a):
 if a == 12 or a < 3:
  return ("Зима")
 elif a == 3 or a <6:
  return("Весна")
 elif a == 6 or a <9:
  return("Лето")
 elif a == 9 or a <=11:
  return("Осень")
 else:
  return("Укажите правильное число месяца")
print(month_to_season(int(input('Введите число месяца '))))
