import time
import sys
import random
import os

os.system('clear')

def main(s):
  for c in s + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(random.random() * 0.1)

nam = raw_input('Input Wordlist [root.txt] : ')
ul = raw_input('Input Wifi Name : ')
main('Scaning Wifi...')
time.sleep(1)
main('Information Wifirels')
print "=> Wifi Name : ", ul
time.sleep(1)
main('=> Status    : Not Vulnrability')
time.sleep(1)
main('=> Ip        : 182.97.42.74')
time.sleep(1)
main('=> Type      : WPA2 PSK')
time.sleep(1)
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Crack Password Wifi => [NotFound]')
main('Failed To Crack System Wifi NotVulnrabylity')
"""
			}
			echo "\e[96m[*] \e[0mLooping : ";
			$loop = trim(fgets(STDIN));
			if (is_numeric($loop) !==true) {
				throw new Exception("\e[91m[!]\e[0m Looping woy/limit, begokk!!\n");
				exit(0);
			}

			$spam->MyPoin(
				$nomor, $loop
			);

		} else if ($choice == 2) {
			echo "\e[96m[*] \e[0mNomor (62) : ";
			$nomor = trim(fgets(STDIN));

			if (substr($nomor, 0, 2) !== "62") {
				throw new Exception("\e[91m[!]\e[0m Nomor awalan harus 62 gan!!\n");
				exit(0);
			}
			echo "\e[96m[*] \e[0mLooping : ";
			$loop = trim(fgets(STDIN));
			if (is_numeric($loop) !==true) {
				throw new Exception("\e[91m[!]\e[0m Looping woy/limit, begokk!!\n");
				exit(0);
			}

			$spam->AltBaljai(
				$nomor, $loop
			);

		} else if ($choice == 3) {
			echo "\e[96m[*] \e[0mNomor (62) : ";
			$nomor = trim(fgets(STDIN));

			if (substr($nomor, 0, 2) !== "62") {
				throw new Exception("\e[91m[!]\e[0m Nomor awalan harus 62 gan!!\n");
				exit(0);
			}
			echo "\e[96m[*] \e[0mPesan (min 10 karakter) : ";
			$pesan = trim(fgets(STDIN));
			if (strlen($pesan) < 10) {
				throw new Exception("\e[91m[!]\e[0m Gue bilang minimal 10 karakter, babi bandel amat lu jadi org!!\n");
				exit(0);
			}
			$response = $spam->SmsPayuTerusBis(
				$nomor, $pesan
			);
			if (strpos($response, "SMS Gratis Telah Dikirim")) {
				echo "\e[92m[*] \e[0mTerkirim broo [ $pesan ]\n";

			} else if (strpos($response, "MAAF....!")) {
				echo "\e[91m[*] \e[0mTunggu 15 menit sebelum mengirim Pesan yang sama!!\n";

			} else {
				echo "\e[91m[*] \e[0mGagal silahkan coba lagi!!\n";
			}

		} else if ($choice == 4) {
			echo "\e[96m[*] \e[0mNomor (62) : ";
			$nomor = trim(fgets(STDIN));

			if (substr($nomor, 0, 2) !== "62") {
				throw new Exception("\e[91m[!]\e[0m Nomor awalan harus 62 gan!!\n");
				exit(0);
			}
			echo "\e[96m[*] \e[0mLooping : ";
			$loop = trim(fgets(STDIN));
			if (is_numeric($loop) !==true) {
				throw new Exception("\e[91m[!]\e[0m Looping woy/limit, begokk!!\n");
				exit(0);
			}
"""
