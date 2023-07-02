'''
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, 
що випали випадковим чином і в певному діапазоні під час чергового тиражу. 
Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Напишіть функцію, яка випадково підбиратиме набір чисел для лотерейного квитка. 
Серед цих чисел не має бути дублікатів.

Формат функції get_numbers_ticket(min, max, quantity), де параметри:

min - мінімальне значення діапазону, не може бути менше 1
max - максимальне значення діапазону, не може бути більше 1000
quantity - кількість чисел у наборі (має бути min < quantity < max)
Функція повинна повернути перелік випадкових чисел за зростанням. 
Якщо порушено умови обмежень на параметри функції, тоді повернути пустий список.
'''

from random import randrange

min_1 = 1
max_1 = 49
quantity = 6
def get_numbers_ticket(min_1, max_1, quantity):
    list_ticket_number = []
    if min_1 < 0 or min_1 < 1 or min_1 > max_1 or quantity > max_1 or max_1 > 1000:
        return []
    for _ in range(0, quantity*10):
        num = randrange(min_1, max_1)
        if num in list_ticket_number:
            continue
        if len(list_ticket_number) == quantity:
            break
        list_ticket_number.append(num)
    list_ticket_number.sort()
    return list_ticket_number
print(get_numbers_ticket(min_1, max_1, quantity))