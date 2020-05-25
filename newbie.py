from requests import Session
import re, sys

s = Session()



no = int(input("No : "))


msg = int(input("Pesan : "))


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; ASUS_A007 Build/MMB29P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36'
    'Referer': 'https://alpha.payuterus.biz/'
}


bypas = r.get("https://aplha.payuterus.biz/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypas)[0]
jml = re.findall(r'<span>(.*?) = </span>', bypas)[0]
captcha = eval(("x", "*").replace(":", "/"))



data = {
        'nohp':no,
        'pesan':msg,
        'captcha':captcha,
        'key':key
}


send = s.post("http://sms.payuterus.biz/alpha/send.php", headers=headers, data=data).text

if 'SMS Gratis Telah Dikirim' in send:
        print(f"\nSukses dikirim! \n[{no}] => {msg}")
elif 'MAAF....!' in send:
        print("\n\t* Mohon Tunggu 15 Menit Lagi Untuk Pengirima>*")
elif 'Pesan yang dikirimkan minimal 10 karakter' in send:
        print('\n\t* Pesan yang dikirimkan minimal 10 karakter >*')
else:
        print("\n\t* Gagal dikirim! *")
