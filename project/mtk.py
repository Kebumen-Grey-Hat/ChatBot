import os, sys, random, time
os.system('clear')
def main(s):
  for c in s + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(random.random() * 0.2)
main('Loading to open project mtk.. wait ')
time.sleep(2)
os.system('clear')
os.system('figlet Kalkulator | lolcat')
ex = """
[1]. penambahan
[2]. pengurangan
[3]. perkalian
[4]. pembagian
"""

def project():
    print (ex)
    pil = raw_input('Masukan Pilihan: ')
    if pil == '1':
       a = input('Masukan Angka Pertama: ')
       b = input('Masukan Angka Kedua: ')
       tmb = (a + b)
       print 'Hasil Dari', a, '+', b, '=', tmb
       print 'ingin mengulang lagi y/n ?'
       bac = raw_input('$ ')
       if bac == 'y' or bac == 'Y':
          os.system('clear')
          project()
       else:
          print ('Uyy Bye Bye Sayang')
          os.system('exit')

    if pil == '2' or pil == '02':
       c = input('Masukan Angka Pertama: ')
       d = input('Masukan Angka Kedua: ')
       kur = (c - d)
       print 'Hasil Dari', c, '-', d, '=', kur
       print 'Ingin mengulang y/n ?'
       fo = raw_input('$ ')
       if fo == 'y' or fo == 'Y':
          project()
       else:
          print ('Bye Bye... Ganteng')
          os.system('exit')

    if pil == '3':
       e = input('Masukan Angka Pertama: ')
       f = input('Masukan Angka Kedua: ')
       kal = (e * f)
       print 'Hasil Dari', e, '*', f, '=', kal

    if pil == '4':
       g = input('Masukan Angka Pertama: ')
       h = input('Masukan Angka Kedua: ')
       ba = (g / h)
       print 'Hasil Dari', g, ':', g, '=', ba
project()
