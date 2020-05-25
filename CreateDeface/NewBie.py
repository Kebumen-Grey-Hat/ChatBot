import os, random, sys, time


def mengetik(s):
  for c in s + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(random.random() * 0.2)
mengetik('Tools Ini versi 0.17 update next selanjutnya  akan memperbaharui system toolsnya..')
os.system('clear')
def main():
    os.system('figlet LOGIN SCRIPT ')
    ex = raw_input('USERNAME: ')
    xe = raw_input('PASSWORD: ')
    if ex == 'admin':
       if xe == 'MaulanaJr':
          print 'Username Found'
          print 'Login Succes'
          time.sleep(2)
       else:
          print 'Password Salah'
          print 'Login Gagal..'
          print 'ingin mengulang lagi (Y/n)'
          ux = raw_input('==> ')
          if ux == 'y' or ux == 'Y':
             main()
    else:
       print 'Username Salah'
       print 'Login Gagal'
       print 'Ingin mengulang lagi (Y/n)'
       gc = raw_input('==> ')
       if gc == 'y' or gc == 'Y':
          main()

main()
time.sleep(2)
os.system('clear')
