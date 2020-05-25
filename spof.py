import smtplib


email = "newbie240604@gmail.com"

rec_email = "hackerdarknet@gmail.com"


pw = input("masukan password : ")
message = "Hello Im Mr.Crot"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, pw)
print ("LOGIN SUKSES")
server.sendmail(email, rec_email, message)
print ("SUKSES")
