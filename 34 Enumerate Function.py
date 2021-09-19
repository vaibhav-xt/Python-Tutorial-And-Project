# enumerate functions

# below code is without enumerate function

n = ["bhindi", "aloo", "chopsticks", "chowmein"]
"""
i = 1
for item in n:
    if i % 2 != 0:
        print(f"Jarvis please buy {item}")
    i = i + 1
"""

# let's talk about enumerate function

for index, item in enumerate(n):
    if index % 2 == 0:
        print(f"Jarvis please buy {item}")