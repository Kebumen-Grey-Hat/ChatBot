
import requests, json, demjson



r = requests.post('http://ip-api.com/json/24.48.0.1')
a = json.loads(r.text)
b = demjson.encode(a)
print(b)
