import os, sys, random, time
os.system('clear')
def mengetik(s):
  for c in s + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(random.random() * 0.2)
mengetik('Welcome To My Kalkulator Python')
os.system('clear')

ex = '''
[1]. penambahan
[2]. pengurangan
[3]. perkalian
[4]. pembagian
'''

def main():
    print (ex)
    pil = raw_input('Masukan Pilihan Anda: ')
    if pil == '1':
       a = input('Masukan Angka Pertama: ')
       b = input('Masukan Angka Kedua: ')
       tmb = (a + b)
       print 'Hasil Dari', a, '+', b, '=', tmb

    if pil == '2':
       c = input('Masukan Angka pertama: ')
       d = input('Masukan angka kedua: ')
       kur = (c - d)
       print 'Hasil Dari', c, '-', d, '=', kur

    if pil == '3':
       e = input('Masukan angka pertama: ')
       f = input('Masukan Angka kedua: ')
       kal = (e * f)
       print 'Hasil Dari', e, '*', f, '=', kal


    if pil == '4':
       g = input('Masukan Angka pertama: ')
       h = input('Masukan Angka kedua: ')
       ba = (g / h )
       print 'Hasil Dari', g, ':', h, '=', ba
main()
