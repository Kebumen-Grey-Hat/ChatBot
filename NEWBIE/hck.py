import requests, os, time, sys
os.system('clear')
baner = """
──────────────────▒
─────────────────░█
────────────────███
───────────────██ღ█
──────────────██ღ▒█──────▒█
─────────────██ღ░▒█───────██
─────────────█ღ░░ღ█──────█ღ▒█
────────────█▒ღ░▒ღ░█───██░ღღ█
───────────░█ღ▒░░▒ღ░████ღღღ█
───░───────█▒ღ▒░░░▒ღღღ░ღღღ██─────░█
───▓█─────░█ღ▒░░░░░░░▒░ღღ██─────▓█░
───██─────█▒ღ░░░░░░░░░░ღ█────▓▓██
───██────██ღ▒░░░░░░░░░ღ██─░██ღ▒█
──██ღ█──██ღ░▒░░░░░░░░░░ღ▓██▒ღღ█
──█ღღ▓██▓ღ░░░▒░░░░░░░░▒░ღღღ░░▓█
─██ღ▒▒ღღ░░ღღღღ░░▒░░░░ ღღღღ░░ღღღ██
─█ღ▒ღღ█████████ღღ▒░ღ██████████ღ▒█░
██ღღ▒████████████ღღ████████████░ღ█▒
█░ღღ████████████████████████████ღღ█
█▒ღ██████████████████████████████ღ█
██ღღ████████████████████████████ღ██
─██ღღ██████████████████████████ღ██
──░██ღღ██████████████████████ღღ██
────▓██ღ▒██████████████████▒ღ██
───░──░███ღ▒████████████▒ღ███
────░░───▒██ღღ████████▒ღ██
───────────▒██ღ██████ღ██
─────────────██ღ████ღ█
───────────────█ღ██ღ  ~# AUTHOR : ARJUN-ID
────────────────█ღღ█  ~# VERSI  : [0.2] BETA
────────────────█ღ█░  ~# CH YT  : ARJUN-NEWBIE
─────────────────██░  ~# TEAM   : KEBUMEN GREY HAT
                      ~# SUPPORT: restuxploit
"""


def login():
    print(baner)
    print
    id = input("USERNAME: ")
    pw = input("PASSWORD: ")

    os.system('bash jalan.sh')
    if id == 'ARJUN-NEWBIE':
       print
       print("USERNAME FOUND")
       time.sleep(1)
    else:
       print("USERNAME FAILED!!")
       time.sleep(2)

    if pw == 'exploit24':
       time.sleep(1)
       print("PASSWORD FOUND")
       time.sleep(1)
       print("LOGIN SUCCESFULYY [√]")
    else:
       print("LOGIN GAGAL")
       time.sleep(3)
       os.system('clear')
       login()
login()

os.system('clear')


ex = """

[A]   ===>    CREATE SCRIPT DEFACE

[B]   ===>    MD5 HASH CREATE BILAL

[C]   ===>    LACAK LOKASI [locator]

[D]   ===>    HACK KAMERA [saycheese]

[E]   ===>    DEFACE WEBDAV TEBAS INDEX
"""



def menu1():
    print(baner)
    print(ex)
    pil = input("CHOICE NUMBER ~#: ")
menu1()
