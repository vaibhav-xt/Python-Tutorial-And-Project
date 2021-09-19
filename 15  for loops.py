"""
list1 = [["Harry", 1], ["Larry", 23], ["Carry", 45], ["Marie", 54], [1, 2]]
dict1 = dict(list1)
for i, j in list1:
    print(i, j)
for item in dict1.items():  # dict.item() represent the sub item in dictionary
    print(item)
"""

d = ["Hat", 1, 3, "car", "bike", 45, 34, 6]
for i in d:
    if str(i).isnumeric() and i > 6:
        print(i)
