from requests import get




te = input("INPUT NUMBER PHONE: ")
ip = get('https://api.ipify.org').text
print('YOUR PUBLIK  IP ADDRESS IS: {}'.format(ip))
