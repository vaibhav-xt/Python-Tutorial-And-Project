# Pickling Iris

import requests
import pickle

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
file = requests.get(url).text

l1 = file.split("\n")
print(l1)

l2 = [item.split(",") for item in l1 if len(item) != 0]
print(l2)

with open("myiris.pkl", "wb") as f:
    pickle.dump(l2, f)

print("\n\n")

with open("myiris.pkl", "rb") as f:
    print(pickle.load(f))