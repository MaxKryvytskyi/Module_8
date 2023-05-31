import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

case1 = [Cat(nickname='Mick', age=5, owner='Sara'), Cat(nickname='Barsik', age=7, owner='Olga'), Cat(nickname='Simon', age=3, owner='Yura')]
case2 = [{'nickname': 'Mick', 'age': 5, 'owner': 'Sara'}, {'nickname': 'Barsik', 'age': 7, 'owner': 'Olga'}, {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}]

def convert_list(cats):
    # Повернутися та зрозуміти детальніше 
    list_cat = []
    if type(cats[0]) == dict:
        for i in cats:
            list_cat.append(Cat(**i))
        return list_cat
    else:
        for cat in cats:
            list_cat.append({"nickname": cat.nickname, "age": cat.age, "owner": cat.owner })
        return list_cat

print(convert_list(case2))
        
            