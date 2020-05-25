import requests
from bs4 import BeautifulSoup
from time import sleep



url = "http://app-articledetail.qianshouguanyin666.com/app-articledetail/aarticle?userid=8781967&articleid=592096&v=3.62&s=2&fontType=2&lang=id_ID&Reward=50&articleid=592096&country=Indonesia&appName=Cashzine&packageName=com.sky.sea.cashzine"

UA = {
   "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; ASUS_A007 Build/MMB29P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"

}


data = {
   "_ga": "GA1.2.1069712659.1588827749; _gid=GA1.2.566108456.1588827749; language=in_ID"

}


c = requests.Session()

def login():
    r = c.post(url, cookies=data, headers=UA)
    soup = BeautifulSoup(r.content, "html.parser")
    print(soup)
    ball = soup.find_all('div', class_="text clearfix", '</div')
    for bali in ball:
        print ("COIN: ", bali.text)
login()



