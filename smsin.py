import requests
import re



s = requests.Session()

url = "http://sms.payuterus.biz/alpha/"

no = int(input("No : "))

msg = input("Pesan : ")
headers = {

 "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; ASUS_A007 Build/MMB29P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"
}


bypass = s.get("http://sms.payuterus.biz/alpha/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypass)[0]
jml = re.findall(r'<span>(.*?) = </span>', bypass)[0]
captcha = eval(jml.replace("x", "*").replace(":", "/"))



data = {
        'nohp':no,
        'pesan':msg,
        'captcha':captcha,
        'key':key
}

send = s.post("http://sms.payuterus.biz/alpha/send.php", headers=headers).text


if 'SMS Gratis Telah Dikirim' in send:
        print(f"\nSukses dikirim! \n[{no}] => {msg}")
elif 'MAAF....!' in send:
        print("\n\t* Mohon Tunggu 15 Menit Lagi Untuk Pengiriman Pesan*")
elif 'Pesan yang dikirimkan minimal 10 karakter' in send:
        print('\n\t* Pesan yang dikirimkan minimal 10 karakter *')
else:
        print("\n\t* Gagal dikirim! *")
