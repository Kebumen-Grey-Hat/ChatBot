import requests, sys, time
import re



s = requests.Session()

url = "https://www.indihome.co.id/verifikasi-layanan/login-verifikasi-otp"

no = input("No : ")

token = s.get(url).text
token = re.findall(r"name=\"_token\" value=\"(.*?)\"",token)[0]
print(token)

data = {
"_token":token,
"msisdn":no,
}

send = s.post(url, data=data).text


if "Gagal!" in send:
    print("Sukses")
else:
    print("Gagal")
