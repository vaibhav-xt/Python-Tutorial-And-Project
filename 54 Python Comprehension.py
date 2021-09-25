# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)
# print(ls)

# second method

# ls = [i for i in range(100) if i % 3 == 0]
# print(ls)

# dict1 = {i:f"item{i}" for i in range(5)}
# dict1 = {value : key for key, value in dict1.items()}
# print(dict1)
#
# print(dict1.items())
"""
dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2"]}
# Here in Above statement we have seen that when we use dictionary then it will not print a duplicate string if we use
# list then it will print all the dresses whether it is duplicate or not.
print(type(list))
print(dresses)
"""

# Generators In Comprehension

# evens = (i for i in range(100) if i % 2 == 0)
# # print(evens.__next__())
# for item in evens:
#     print(item)


no_of_list = int(input("How many items add in a list: "))
list = []
for i in range(no_of_list):
    input_string = input("Enter a list element separated by space ")
    list.append(input_string.split())
    i += 1
t = int(input("Which type of comprehension you use 1. List Comprehension 2.Dictionary Comprehension 3. Set Comprehension "))
if t==1:
    ls = [i for i in list]
    print(ls)
    print(type(ls))
elif t==2:
    dict1 = {f'item{i}': i for i in list}
    print(dict1)
    print(type(dict1))
elif t==3:
    s ={i for i in list}
    print(s)
    print(type(s))