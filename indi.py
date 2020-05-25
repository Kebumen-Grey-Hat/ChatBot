import requests
import re

r = requests.Session()

no = input("NO: ")

url = "https://www.indihome.co.id/verifikasi-layanan/login-verifikasi-otp"


token = r.get(url).text
token = re.findall(r"name=\"_token\" value=\"(.*?)\"",token)[0]


data = {
"msisdn":no,
"_token":token,
}

send = r.post(url, data=data).text
print (send)
