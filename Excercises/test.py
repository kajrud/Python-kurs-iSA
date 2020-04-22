import requests

data = requests.get("https://api.exchangeratesapi.io/2000-01-03")
print(data.text)