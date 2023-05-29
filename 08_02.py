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