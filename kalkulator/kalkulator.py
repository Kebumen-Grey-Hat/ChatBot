import sys, time, os



ex = """
[1] PENAMBAHAN
[2] PENGURANGAN
[3] PERKALIAN
[4] PEMBAGIAN
"""

def main():
    print(ex)
    pil = raw_input("Input Number: ")
    if pil == '1' or pil == '01':
       a = input("Inpur Number One: ")
       b = input("Input Number Two: ")
       tmb = (a + b)
       print "Hasil Dari", a, "+", b, "=", tmb
       print "Ingin Mengulang y/N ?"
       yo = raw_input("==> ")
       if yo == "y" or yo == "Y":
          main()

    if pil == '2':
       c = input("input Number one: ")
       d = input("Input Number two: ")
       kur = (c - d)
       print "Hasil Dari", c, "-", d, "=", kur
       print "Ingin Mengulang y/N ?"
       xe = raw_input("==> ")
       if xe == "y":
          main()

    if pil == '3':
       f = input("input number one: ")
       g = input("input number two: ")
       kal = (f * g)
       print "Hasil Dari", f, "*", g, "=", kal
       print "Ingin Mengulang y/N ? "
       yuk = raw_input("==> ")
       if yuk == "y":
          main()

    if pil == "4":
       h = input("input number one: ")
       hh = input("input number two: ")
       bagi = (h / hh)
       print "Hasil Dari", h, ":", hh, "=", bagi
       print "Ingin Mengulang y/N ? "
       go = raw_input("==> ")
       if go == "y":
          main()
    else:
       print "Wrong Input Eror!!"
       os.system("exit")
main()
