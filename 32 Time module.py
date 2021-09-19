""" How to find program execution time? """

import time
# lets find out the time difference between while and for loop in execution
initial = time.time()
print(initial)
k = 0
while (k < 3):
    print("This is harry bhai 3")
    k = k + 1
print("While loop ran in", time.time() - initial, "seconds")
initial2 = time.time()
for i in range(3):
    print("This is harry bhai")
print("For loop ran in", time.time() - initial2, "seconds")


# local time

localtime = time.asctime(time.localtime((time.time())))  # also can be written as time.ctime()
# local time return value in tuple and time.time() represent the time
# here asctime converts tuple into the formate of time
print(localtime)

""" Talk about Time.sleep() function"""
# -: this function is use to stop the program for few seconds for example
"""
while True:
    print("Vaibhav is a good boy.")
    time.sleep(2)
"""

""" Epoch - The epoch is the point where the time starts, and is platform dependent.
            This point is taken as the January 1st of the current year, 00:00:00.
            For unix, the epoch is january 1st 1970, 00:00:00 (UTC)
    UTC   - Coordinated Universal time
    DST   - Daylight Saving Time, an adjustment of the  timezone. 
    ctime() - this function is used to get current date and time.
    time() - this function return the time in seconds since the epoch as a floating point number.
    localtime() - this function is used to convert seconds into date and time. It return an object
                   struct_time which can be used to access the attributes either using an index or using a name."""

a =time.ctime()
print(a)
