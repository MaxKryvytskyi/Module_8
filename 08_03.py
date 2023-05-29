from datetime import datetime

date = '2021-05-27 17:08:34.149Z'

def get_str_date(date):
    date = date.split()
    date = datetime.strptime(date[0], r'%Y-%m-%d')
    date = datetime.strftime(date, r'%A %d %B %Y')
    return date
print(get_str_date(date))
    
    
    
    
