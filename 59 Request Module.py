import requests
r = requests.get("https://www.battlegroundsmobileindia.com/")
print(r.text)

url = "www.something.com"
data = {"p1": 4, "p2": 8}
r2 = requests.post(url=url, data=data)

# google http status code
