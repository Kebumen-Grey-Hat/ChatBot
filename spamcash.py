import requests
r = requests.Session()



url = "https://tokocash.com/oauth/otp"

t = r.post(url)
print(t)
