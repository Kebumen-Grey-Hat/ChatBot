import requests, json


r = requests.get('https://graph.facebook.com/putriy.kaeysha/subcribersz?access_token=')

res = json.loads(r.text)
print(res)
