import os, sys
from time import sleep
os.system("clear")
def main():
    os.system('figlet LOGIN BOZ | lolcat')
    a = raw_input("USERNAME: ")
    b = raw_input("PASSWORD: ")
    sleep(1)

    jk = "{}".format(a)
    bl = "{}".format(b)

    if jk == "admin":
       print "USER FOUND"
    else:
       print "USER FAILED"
       main()

    if bl == "1234":
       print "PASSWORD FOUND"
    else:
       print "GAGAL !!"
       main()
main()


