from datetime import datetime
import time

a = datetime.strptime('2018-01-01 17:50', '%Y-%m-%d %H:%M')

print(a)
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))