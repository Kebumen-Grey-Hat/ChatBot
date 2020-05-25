import os, sys, time


def login():
    os.system('figlet LOGIN BOZ | lolcat')
    user = raw_input('USERNAME: ')
    pasw = raw_input('PASSWORD: ')
    time.sleep(1)
    if user == 'admin':
       if pasw == 'root':
          print "PASSWORD FOUND"
          print "LOGIN SUCCES"
          time.sleep(1)
       else:
          print "PASSWORD FAILED"
          print "LOGIN GAGAL"
          login()
          time.sleep(2)
    else:
       print "USERNAME SALAH"
       print "LOGIN FAILED"
       time.sleep(2)
       login()
login()


main = """
[1] Penambahan
[2] Pengurangan
[3] Perkalian
[4] Pembagian
"""


def menu():
    os.system('clear')
    time.sleep(2)
    print(main)
    pil = raw_input('input number: ')
    if pil == '1' or pil == '01':
       a = input('input number one: ')
       b = input('input number two: ')
       tmb = (a + b)
       print "Hasil dari", a, "+", b, "=", tmb
       print "Ingin Mengulang Lagi (y/N)"
       ex = raw_input('==> ')
       if ex == 'y' or ex == 'Y':
          menu()

menu()
