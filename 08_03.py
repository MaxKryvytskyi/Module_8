from datetime import datetime

s = '10 January 2020'
print(datetime.strptime(s, '%d %B %Y')) # 2020-01-10 00:00:00