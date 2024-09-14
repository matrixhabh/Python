# Timestamp Project

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
if (timestamp < '12:00:00' and timestamp > '24:00:00'):
    print("Good Morning")
if (timestamp > '12:00:00' and timestamp < '18:00:00'):
    print("Good Afternoon")
else:
    print("Good Evening")