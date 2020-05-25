




import requests



id = input("USERNAME: ")
pw = input("PASSWORD: ")

url = "https://m.facebook.com/login.php"

data = {"email":id, "pass":pw}


r = requests.post(url, data=data)
print (r.url)
