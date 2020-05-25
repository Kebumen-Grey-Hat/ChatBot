from time import sleep

ex = """
ingin di ulang berapa kali?
"""

print(ex)
ro = "Perulangan Sukses"
pil = input("=> ")

for i in range(int(pil)):
    sleep(1)
    print(ro)
