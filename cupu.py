import requests, os


r = requests.Session()

id = input("MASUKAN ID: ")
pas = input("MASUKAN PASSWORD: ")


url = "https://m.facebook.com/login.php"


data = {
"email":id,
"pass":pas,
}

res = r.post(url, data=data)
print(res.url)
