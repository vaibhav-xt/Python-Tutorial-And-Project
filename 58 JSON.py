# JSON(inbuilt module) = Java Script Option Notation

import json
# json not include comments in files
data = '{"var1": "Harry", "var2": "56"}'
parsed = json.loads(data)
print(type(parsed))
print(parsed)

# task = working of jason.load

data2 = '{"Channel_name": "CodeWithHarry", "cars": ["bmw", "audi a8", "ferrari"], "fridge": ("roti", "bidi")}'
jscomp = json.dumps(data2)
print(jscomp)

# Task2 = what is sort keys parameter in dumps
