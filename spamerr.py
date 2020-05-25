import requests



c = requests.Session()


url = "https://www.tokocash.com/oauth/otp"

no = input('NO : ')

data = {
"msisdn":no,
}


respon = c.post(url, data=data).text

print(respon)
