# Time Module in Python

'''
The time module in Python provides a set of functions to work with time-related operations, 
such as timekeeping, formatting, and time conversions. 
'''

# time.time()
'''
The time.time() function returns the current time as a floating-point number, 
representing the number of seconds since the epoch (the point in time when the time module was initialized). 
The returned value is based on the computer's system clock 
and is affected by time adjustments made by the operating system, such as daylight saving time.
'''

# Example-

import time
print(time.time())

# Output: 1602299933.233374

# time.sleep()
'''
The time.sleep() function suspends the execution of the current thread for a specified number of seconds. 
This function can be used to pause the program for a certain period of time, 
allowing other parts of the program to run, or to synchronize the execution of multiple threads.
'''

# Example-

import time

print("Start:", time.time())
time.sleep(2)
print("End:", time.time())

# Output:
# Start: 1602299933.233374
# End: 1602299935.233376

time.strftime()
'''
The time.strftime() function formats a time value as a string, based on a specified format. 
This function is particularly useful for formatting dates and times in a human-readable format, 
such as for display in a GUI, a log file, or a report.
'''

# Example-

import time

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)

# Output: 2022-11-08 08:45:33

## Conclusion-

'''
The time module in Python provides a set of functions to work with time-related operations, 
such as timekeeping, formatting, and time conversions. Whether you are writing a script, 
a library, or an application, the time module is a powerful tool 
that can help you perform time-related tasks with ease and efficiency. 
So, if you haven't already, be sure to check out the time module in Python 
and see how it can help you write better, more efficient code.
'''