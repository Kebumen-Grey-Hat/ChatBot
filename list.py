import os, sys, time





def login():
    os.system('figlet LOGIN')
    a = raw_input('USERNAME : ')
    b = raw_input('PASSWORD : ')


    if a == 'admin':
       print 'User Found'
       if b == 'maulanajr':
          print 'Login Sukses'
    else:
       print 'Login Gagal'
       login()
login()
