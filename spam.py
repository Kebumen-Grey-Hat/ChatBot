import requests



ex = requests.get("https://spamcheck.postmarkapp.com/filter")
send = ex.text
print(send)
