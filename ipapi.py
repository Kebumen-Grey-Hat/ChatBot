import requests



url = 'http://kansascitynova.org'

send = requests.post(url).text

print(send)
