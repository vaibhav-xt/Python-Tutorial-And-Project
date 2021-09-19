# F strings

# 1st Method -
import math
me = "Harry"
a1 = 3
# a = "this is %s %s" %(me, a1)
# print(a)


# 2nd Method
"""
a = "This is {1} {0}"  # here 1 and 0 are the position as 0 is me and 1 is a1.
b = a.format(me, a1)
print(b)
"""
# 3rd Method
"""
a = f"this is {me} {a1} {4 * 65}"
print(a)
"""

s = f"this is {me} {a1} {math.cos(90)}"
print(s)