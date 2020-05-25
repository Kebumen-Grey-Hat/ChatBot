import requests
import time
import os
import sys
import random


def project1(s):
  for c in s + "\n":
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(random.random() * 0.2)
os.system("figlet SPAM TRI | lolcat")
project1('~# AUTHOR : ARJUNZ-LOVERSS')
print
print
r = requests.Session()

nom = input("MASUKAN NOMOR  : ")
jml = input("MASUKAN JUMLAH : ")

url = "https://registrasi.tri.co.id/daftar/generateOTP"

data = {"msisdn":nom}

respon = r.post(url, data=data).text
for c in range(int(jml)):
    print (respon)
    time.sleep(2)
