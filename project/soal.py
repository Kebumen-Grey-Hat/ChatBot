import os, random, sys, time
os.system('clear')
def main(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(random.random() * 0.2)
main('Welcome To Soal Bucin New 2020 Jawab Dengan Jujur Yah')
os.system('clear')
main('Soal Yang Pertama...')
print 'Apa yang kamu lakukan jika pasangan kamu ngajak jalan'
print 'namun kamu ada kepentingan keluarga?'
print 'A. Minta izin gak bisa karna ada keprentingan Keluarga'
print 'B. Batalin Kepentingan keluarga dan jalan sama pacar'
print 'C. Nolak untuk jalan karena ada kepentingan keluarga'
print 'D. Selesaian dulu kepentingan keluarga lalu pergi jalan'
print 'sama pacar'
print
pil = raw_input('Jawab: ')
if pil == 'D':
   main('Yeeeeah Jawaban Kamu Betul... Tingkat Kepekaan Kamu Bagus')
else:
   main('Jawaban Kamu Salah Kamu Kurang Peka Goblok')

