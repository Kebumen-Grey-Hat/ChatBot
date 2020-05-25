import requests


s = requests.Session()


url = "https://m.facebook.com/login.php"


send = s.post(url)
print(send)
