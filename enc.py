import random, base64

def randStr(lenght):
	d = []
	for a in range(lenght):
		d.append(random.choice(list("abcdefghijklmnopqrstuvwxyz1234567890")))
	return "".join(d)

def leftOther(enc, appd):
	d = []
	jml = int(enc.count("="))
	for a in range(jml):
		d.append(appd)
	return "".join(d)

def randBase(teks):
	enc = base64.b64encode(teks.encode())
	return "".join(reversed(enc.decode()))

def encrypt(teks, key):
	random.seed(teks)
	base = randBase(teks)
#	print (base64.b64encode(teks.encode()).decode())
	keyRand = base64.b16encode(key.encode()).decode()
	other = leftOther(base, "+")
	base = base.replace("=", "")
	result = keyRand+"%"+base+"|"+keyRand+other
	open("result.txt", "w").write(result+"\n")
	print (result)

teks = input("Masukan Teks: ")
key = input("Key: ")
encrypt(teks, key)

