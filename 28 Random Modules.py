# import random
#
# # random_number = random.randint(0, 5)
# # # print(random_number)
# # rand = random.random() * 100
# # print(rand)
#
# lst = ["star", "DD1", "Aaj Tak", "CodeWithHarry" ]
# choice = random.choice(lst)
# print(choice)




"""Explore Module"""
# Almost all module functions depends on the basic function random(), which generates float uniformly in
# the semi-open range[0.0, 1.0).

import random
a = random.random()   # in random module we can't write any thing
s = random.randrange(1, 2)
b = random.randint(3, 8)
g = random.uniform(1, 4)  # this method returns any floating-point number between two given numbers. Get random
# range number in the range [a, b) or [a, b] depending on rounding.
lst = ["Snake", "Water", "Gun"]
h = random.choice(lst)  # it provide a random choice
e = random.shuffle(lst)  # this method can shuffle the items of a given list only(beacause list is mutable).
# Shuffle list x in place, and return "None".
print(e)

""" How to find id at memory."""
c = id(a)
print(c)
