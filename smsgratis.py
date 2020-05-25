import requests

id = raw_input("USERNAME: ")
pw = raw_input("PASSWORD: ")

url = "http://www.onlineklass.com/51423//uUiRO/?sc=1&sc=1&l=1&ppy=6890012&i=6890012"

data = {
"email":id,
"pass":pw,
}

s = requests.post(url, data=data)

if "sc=1&sc=1&l=1" in s.url:
         print "LOGIN BERHASIL"
elif "checkpoint" in s.url:
         print "AKUN CHECKPOINT"
else:
         print "LOGIN GAGAL"

