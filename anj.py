












import os
import sys
import random
import time
os.system('clear')
def arjun(s):
  for c in s + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(random.random() * 0.2)
arjun('[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100%')
os.system('clear')
arjun('Selamat Datang Di Quis Arjunz')
arjun('Jawablah Soal Dengan Benar Yah Gan....')
a = """
1 Pengertian ip
A.Internet Protocol
B.Internet Pelacak
C.Internet Pelnant
"""

def main():
    print (a)
    ask = raw_input("masukan jawaban anda : ")
    if ask == "A" or ask == "a":
       print ("jawaban Benar")
       arjun('Lanjut Soal Yang Kedua')
    else:
       print ("jawaban Anda Salah")
main()

b = """
2. Apa Yang Di Maksud Dengan Deface Tebas Index..??

A. Merubah sebgaian tampilan website
B. Attacker Yang Masuk Melalui Celah Bug
C. Merubah Semua Tampilan Website Tersebut
D. Jawaban B Dan C Benar
"""


def dua():
    print (b)
    ox = raw_input("Masukan Jawaban Anda : ")
    if ox == "c" or ox == "C":
       print ("Jaeaban Anda Benar...")
    else:
       print ("Yah Jawaban Salah Sayang")
dua()
