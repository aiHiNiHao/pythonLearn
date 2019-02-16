import datetime
import time

dd = datetime.date(2018, 12, 26)
print(dd)
print(dd.ctime())
print(dd.weekday())

d = datetime.datetime(2018, 12, 26)
print(d.today())
print(d.now())
print(d.fromtimestamp(time.time()))
