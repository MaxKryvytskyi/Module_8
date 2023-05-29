from datetime import datetime

date = "2021-10-09"

def get_days_from_today(date):
    date = datetime.strptime(date, r'%Y-%m-%d')
    current_datetime = datetime.now()
    result = current_datetime - date
    return result.days
print(get_days_from_today(date))
