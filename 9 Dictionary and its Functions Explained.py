
# DICTIONARIES AND ITS FUNCTIONS

d1 = {"Vaibhav":"burger", "Rohan":"fish", "skillf":"roti", "Tanish":{"Breakfast":"Samosa","Lunch":"Halwa"}}

d1["Ayush"] = "Juck Food"
d1["420"] = "Fruits"
# del d1["420"]
# print(type(d1))
# print(d1.copy())  # copy function print the copy of the dictionary

"""d3 = d1
del d3["Vaibhav"]   # here we have seen that we are deleting from d3 but also deleting from d1 this is because we have
print(d1)"""        # not used copy function when we use then d3 get a copy of d1 see below

# d3 = d1.copy()
# del d3["Vaibhav"]
print(d1)

# print(d1.update({"leena":"bhindi"})      # is a wrong method
"""d1.update({"leena":"bhindi"}            # but not working
print(d1)"""

# print(d1.keys())
# print(d1.items())     # it return key value pairs
# print(d1.values())