import time
import datetime

now = time.time()

print(now)
print(now - int(now))

millisecond = int ((now - int(now)) * 1000)
print(millisecond)
#print(time.localtime(now))
t = time.localtime(now)
time_str = "%d-%d-%d-%d-%d-%d-%d" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec, millisecond)
print(time_str)

