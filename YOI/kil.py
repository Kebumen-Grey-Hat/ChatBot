import sys, os, time


pw = input("Masukan List: ")

ex = open('login.txt', "r").readlines()

for i in ex:
    fil = i.strip()
    if "fil" == "admin":
        print("Password Di Temukan => ", pw)
    else:
        print("Gagal Di Temukan => ", pw)
