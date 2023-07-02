'''
Є список IP адрес:

IP = [
    "85.157.172.253",
    ...
]
Реалізуйте дві функції. 
Перша get_count_visits_from_ip за допомогою Counter повертатиме словник, де ключ це IP, а значення – кількість входжень у вказаний список.

Приклад:

{
    '85.157.172.253': 2,
    ...
}
Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто уживаним в списку IP і кількістю його появ в списку.

Пример:

('66.50.38.43', 4)
'''

from collections import Counter


ips = ['85.157.172.253', '143.231.49.229', '173.37.214.238', '27.137.126.114', 
       '76.98.129.245', '66.50.38.43', '248.95.93.236', '173.37.214.238', '76.98.129.245', 
       '76.98.129.245', '85.157.172.253', '66.50.38.43', '66.50.38.43', '66.50.38.43']



def get_count_visits_from_ip(ips):
    return Counter(ips)


def get_frequent_visit_from_ip(ips):
    return Counter(ips).most_common(1)[0]



print(get_count_visits_from_ip(ips))
print(get_frequent_visit_from_ip(ips))
    