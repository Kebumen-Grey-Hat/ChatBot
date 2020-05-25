import requests
import re
import sys



s = requests.Session()

no = input("No : ")

url = "https://www.indihome.co.id/verifikasi-layanan/login-otp"


token = s.get(url).text
token = re.findall(r"name=\"_token\" value=\"(.*?)\"", token)[0]


data = {
"_token":token,
"msisdn":no,
}

sen = s.post(url, data=data).text
print(sen)
