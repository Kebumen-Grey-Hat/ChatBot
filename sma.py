import requests, sys, time, os

r = requests.Session()
no = input('Masukan Nomor : ')

b = r.post('https://www.indihome.co.id/verifikasi-layanan/login-verifikasi-otp', data = {'msisdn': no}).text

if "Gagal!" in str(b):
    print("Sukses")
else:
    print("Gagal")

