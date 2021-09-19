
# List And Functions

# LIST
"""grocery = ["Harpic", "vem bar", "deodrant", "bhindi", "lollypop", 56]
print(grocery)
print(grocery[4])"""
# Extend List - means that adding two list together to form a one single list
"""grocery = ["Harpic", "vem bar", "deodrant", "bhindi", "lollypop", 56]
numbers = [1, 3, 43, 4, 5, 6, 7]
# grocery.extend(numbers)
print(grocery)
del numbers[1]
print("List Items after deleting item at index 1 : ", numbers)"""


numbers = [1, 3, 43, 4, 5, 6, 7]
"""print(numbers[2])
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)                            # GOOGLE PYTHON FUNCTION
print(max(numbers))"""
# numbers.remove(5)
# numbers.pop()
# numbers.append(4)
# numbers.insert(1, 5)
# numbers[0] = 456
grocery = ["Harpic", "vem bar", "deodrant", "bhindi", "lollypop", 56]
numbers.copy()      # i can't understand copy function
print(numbers)



# Mutable = can change  Ex - List
# Immutable = can't change  Ex - tuple

# TUPLE                           """ GOOGLE TUPLE FUNCTION """

tp = (1, 3, 4, 5)
tp2 = (1, 3, 4, 5)
print(tp + tp2)  # tuple can concatenate
# tp[1] = 4  # this statement can't run because write now i have read above that it is immutable
# tp = (1)   # if we write only one word or number is parenthesis then it return in result only the value that hase
# inserted by the user not parenthesis
"""tp1 = (1,)    # if we inserted only comma then it becomes tuple otherwise we have seen above case
print(tp1)"""

# How to interchange value
a = 3
b = 2
"""first method
temp = a
a = b
b = temp"""
# second method
a, b = b, a
print(a, b)
