import requests


ex = raw_input("Masukan Search : ")

url = "https://www.google.com"

data = {"url":url, "search":ex}

r = requests.post(url, data=data)
print(r.url)
