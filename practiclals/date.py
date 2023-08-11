# from datetime import date
# d=date.today()
# print(d.year)
# print(d.month)
# print(d.day)

# from datetime import datetime
# d=datetime.now()
# print(d.hour)
# print(d.minute)
# print(d.second)

from datetime import date,datetime
d=date.today()
d2=date(year=12,month=2,day=3)
d3=d2-d
print(d)