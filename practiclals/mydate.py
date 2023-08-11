import datetime
from datetime import date
from datetime import timedelta
# d=datetime.datetime.now()
# print(d)
# y=d.year
# print(y)
# d=datetime.date.today()
# print(d)
# d=date(2022,12,1)
# print(d)
#total_second
t=timedelta(days=10,hours=3,minutes=39,seconds=46)
print("total seconds",t.total_seconds())