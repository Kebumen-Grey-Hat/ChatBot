import requests


s = requests.Session()

nomor = raw_input("NO: ")
jml = raw_input("jumlah: ")
url = "https://registrasi.tri.co.id/daftar/generateOTP/"


data = {
"msisdn":nomor,
}

for i in range(int(jml)):
      respon = s.post(url, data=data).text
      print(respon)
