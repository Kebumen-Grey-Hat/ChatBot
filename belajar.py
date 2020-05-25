import time, sys, os

os.system("clear")

a = 5
b = 5
c = 5
os.system('figlet ARJUN-ID')
soal1 = """
[1]. Apakah yang di maksud dengan requests di dalam bahasa python?

A. Sebuah Module untuk mengirimkan data
B. Sebuah fungsi untuk merespon url yang di kirimkan
C. module untuk mendecode sxcript
D. Module yang di gunakan untuk parsing data dari session
"""
soal2 = """

[2]. Apa saja bahasa pemrograman yang mudah untuk di
     gunakan bersamaan dengan html

A. Shell bash,curl,visual basic,C++,dan power shell
B. Python,C++,bash,Power shell
C. Python,php,curl,perl,html,javascript
D. C++,python,perl,Html,Power shell

"""



def menu1():
    print(soal1)
    AA = raw_input('JAWAB: ')
    if AA == 'A' or AA == 'a':
       time.sleep(2)
       print "JAWABAN ANDA BENAR"
       tmb = (a + b)
       print "POIN ANDA : ", tmb
    else:
       print "JAWABAN ANDA SALAH"
       kur = (a - b)
       print "POIN ANDA : ", kur


    print(soal2)
    BB = raw_input('JAWAB: ')
    if BB == 'C' or BB == 'c':
       time.sleep(1)
       print "JAWABAN ANDA BENAR"
       Tmb = (tmb + a)
       print "POIN ANDA : ", Tmb
    else:
       print "JAWABAN SALAH"
       Kur = (tmb - a)
       print "POIN ANDA : ", kur
menu1()
