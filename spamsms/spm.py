import requests

s = requests.Session()

no = input("NO: ")

url = "https://registrasi.tri.co.id/daftar/generateOTP/"

data = {
"msisdn":no,
}

send = s.post(url, data=data).text
print(send)
