from time import sleep
import os
import requests
import random
import sys
def ketik(s):
  for c in s + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      sleep(random.random() * 0.2)
os.system('clear')
os.system('bash banner.sh')
ketik('please your input command "help" ')
hel = raw_input('KEBUMEN_> ')
if hel == 'help':
   sleep(2)
   os.system('clear')
else:
   print 'Failed Your Input'
   os.system('exit')
os.system('bash banner.sh')


ex = '''
COMMAND        INFORMATION
-------        -----------

help           for help
info           info this tool
ctrl+l         clear screen
exit           exit this tool
show           show command tools
banner         show banner
'''
def main():
    print (ex)
    a = raw_input('KEBUMEN_> ')
    if a == 'help':
       sleep(2)
       os.system('clear')
       os.system('bash banner.sh')
       main()

    if a == 'info':
       sleep(2)
       os.system('clear')
       ketik('~# CREATE BY : ARJUN-ID')
       ketik('~# SUPPORT   : n3koPo!61')
       ketik('~# TEAM GC   : Kebumen Grey Hat')
       os.system('clear')
       os.system('bash banner.sh')
       main()
    else:
       os.system('exit')


    if a == 'ctrl+l':
       sleep(1)
       ketik('Ctrl+C Detected')
       sleep(1)
       os.system('exit')
    if a == 'exit':
       sleep(2)
       ketik('Thanks udah pake script ini gansz')
       os.system('exit')

    if a == 'banner':
       os.system('clear')
       os.system('bash banner.sh')
       sleep(5)
       main()



    if a == 'show':
       print " [A] => [SPAM TOKOPEDIA UNLIMITED ]"
       print " [B] => [SPAM KHUSUS TRI UNLIMITED]"
       print " [C] => [BRUTEFORCE FACEBOOK HCK  ]"
       print " [D] => [MULTI BRUTE FORCE MBF AF ]"
       print " [E] => [DEFACE TEBAS INDEX WEBDAV]"
       print " [F] => [CREATE VIRUS MALICIOUS V2]"
       wil = raw_input("Choice => ")
       if wil == 'A':
          os.system("python2 cash.py")
       if wil == 'B':
          os.system("python tray.py")
       if wil == 'C':
          os.system("python2 foce.py")
       if wil == 'D':
          os.system("python2 mbf.py")
       if wil == 'E':
          os.system("unzip ARJUNZ-ID.zip")
          os.system("cd ARJUNZ-ID")
       if wil == 'F':
          os.system("unzip Malicious.zip")
          os.system("cd Malicious")
          os.system("cd Malicious")
          os.system("python2 malicious.py")
main()
