import os, sys, time



def main():
    user = input("USERNAME: ")
    PASS = input("PASSWORD: ")


    if user == "admin":
       print('USERNAME FOUND..')
    else:
       print('USERNAME SALAH')
       print('LOGIN GAGAL')
       main()

    if PASS == "12345":
       print("PASSWORD FOUND")
    else:
       print("PASSWORD SALAH")
       print("LOGIN GAGAL")
       main()
main()
