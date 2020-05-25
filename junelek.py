import requests



r = requests.Session()


no = input("NO: ")

url = "https://www.tokocash.com/oauth/otp"

data = {"msisdn":no}

res = r.post(url, data=data).text
print (res)
