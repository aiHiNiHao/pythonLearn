import time

print(time.daylight)
print(time.time())

t = time.localtime()
print(t.tm_hour)

print(time.asctime(t))

print(time.ctime())

time.sleep(2)
t = time.localtime()
mktime = time.mktime(t)
print(mktime)

print(time.ctime(mktime))
