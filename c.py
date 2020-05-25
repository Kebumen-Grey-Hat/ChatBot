import smtplib, random, sys, time, os, hide 
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()                                              
        time.sleep(random.random() * 0.1)
mengetik(''' _____           _ _                                |   __|_____ ___|_| |
|  |  |     | .'| | |                                           |_____|_|_|_|__,|_|_|''')
        bct = input("gmail: ")                                          anjk = input("kirim pesan ke: ")                                bla = input("masukan pesan: ")                                  pesan = bla                                                     (bct,anjk)                                                      try:
        pas = hide.hide("masukan password email: ")                     smtpobj = smplib.SMTP("gmail.com",120)                          smtpobj = login(bct, pas)                                       smtpobj = sendmail(bct, anjk, pesan)
        print("berhasil mengirim pesan")                        except Exception:
        print("mengirim gagal")
