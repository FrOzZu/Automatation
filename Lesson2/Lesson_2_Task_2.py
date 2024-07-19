def is_year_leap(year):
   if year %4 == 0:
    return True
   else:
    return False
year_to_check=int(input("Какой год високосный? "))

result=is_year_leap(year_to_check)
print(f"Год {year_to_check}:{result}")
