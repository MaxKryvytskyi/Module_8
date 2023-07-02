'''
Напишіть функцію визначення кількості днів у конкретному місяці. 
Ваша функція повинна приймати два параметри: month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 і year - рік, 
що складається із чотирьох цифр. 
Перевірте, чи функція коректно обробляє місяць лютий високосного року.
'''


from datetime import *


month = [3, 12, 2]
year = [2021, 2021, 2020]

def get_days_in_month(month1, year1):
    for i in range(27,32):
        try:
            d1 = datetime(year=year1, month=month1, day=i)
        except ValueError:
            d1 = datetime(year=year1, month=month1, day=i-1)
            break
    return d1.day

print(get_days_in_month(month[2], year[2]))