import json
# JSON(inbuilt module) = Java Script Option Notation
# Json - it is a lightweight data interchange format inspired by Java Script object literal syntax

# json not include comments in files
"""
data = '{"var1": "Harry", "var2": "56"}'
parsed = json.loads(data)
print(type(parsed))
print(parsed)
"""
# task = working of jason.load

# json.dump helps you to make java script compatible means it convert into java script
"""
data2 = '{"Channel_name": "CodeWithHarry", "cars": ["bmw", "audi a8", "ferrari"], "fridge": ("roti", "bidi")}'
jscomp = json.dumps(data2)
print(jscomp)
print(type(jscomp))
"""
# Task2 = what is sort keys parameter in dumps
"""
a = json.dumps(['foo', {'bar': (None, 1.0, 2)}])
print(a)
print(type(a))

print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

print(json.loads(' "\\"foo\\bar"'))
"""

# from io import StringIO
# i = StringIO('["streaming API"]')
# print(json.load(i))


