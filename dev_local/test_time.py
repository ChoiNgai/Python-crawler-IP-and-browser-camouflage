import datetime,time
import os
#now = time.strftime("%Y-%m-%d %H:%M:%S")
while 1:
    now = time.strftime("%H")
    print(now)
    if  str(now) == str(18) :
        os._exit(0)
    else:
        continue
    nowT = datetime.datetime.now()
