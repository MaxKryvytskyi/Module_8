'''
Розробіть функцію get_days_from_today(date), яка повертатиме кількість днів від поточної дати, 
де параметр date - це рядок формату '2020-10-09' (рік-місяць-день).

Підказки:

Параметр date розбити на рік, місяць та день можна використовуючи метод рядків split.
datetime приймає аргументи типу int, використовуйте перетворення типів.
ігноруйте години, хвилини та секунди для вашої дати, важливі повні дні.
кількість днів ви можете отримати відніманням з поточної дати, заданої в змінній date (без часу).
Наприклад: Якщо поточна дата - '5 травня 2021', то виклик get_days_from_today("2021-10-09") поверне нам -157.
'''

from datetime import datetime

date = "2021-10-09"

def get_days_from_today(date):
    date = datetime.strptime(date, r'%Y-%m-%d')
    current_datetime = datetime.now()
    result = current_datetime - date
    return result.days
print(get_days_from_today(date))
