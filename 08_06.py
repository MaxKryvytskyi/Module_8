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


