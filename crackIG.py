import requests


url = "https://www.instagram.com/login.php"


id = input("USERNAME: ")
pw = input("PASSWORD: ")


data = {"email":id, "pass":pw}


respon = requests.post(url, data=data)
print(respon.url)
