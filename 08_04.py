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