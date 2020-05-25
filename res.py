import requests
req = requests.get('https://github.com/timeline.json')
send = req.text
print(send)
