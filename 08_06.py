'''
Створіть функцію decimal_average(number_list, signs_count), яка обчислюватиме середнє арифметичне типу Decimal з кількістю значущих цифр signs_count. 
Параметр number_list — список чисел

Увага
Не забувайте приводити всі числа у списку до типу `decimal`

Приклад:

виклик функції decimal_average([3, 5, 77, 23, 0.57], 6) поверне 21.714
виклик функції decimal_average([31, 55, 177, 2300, 1.57], 9) поверне 512.91400
'''

from decimal import Decimal, getcontext

number_list = [4.5788689699797, 34.7576578697964, 86.8877666656633, 12]
signs_count = 6
def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    sums = Decimal(0)
    for i in number_list:
        sums += Decimal(i)
    return sums/len(number_list)
print(decimal_average(number_list, signs_count))


