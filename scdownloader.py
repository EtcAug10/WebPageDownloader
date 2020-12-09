#!/usr/bin/python3.9
# Source Code Web Downloader Using UrlLib example

import os,urllib
from urllib import request

banner = """
/////  ________
/ SC Downloader\\
/ By EtcAug10  |
/////  ________/
"""

def ekse(t):
	pil = input("Apakah url "+t+" sudah benar?(y/n)")
	if pil == "y":
		try:
			print("Mendowload..")
			tpath = t.replace("https://","")
			urllib.request.urlretrieve(t,tpath+".html")
			print("Terinstall.")
		except:
			print("Modul tidak terinstall.\nMenginstall modul..")
			os.system("pip install urllib")
			main()
	elif pil == "n":
		print("Kembali")
		main()
	else:
		quit("Salah command. Keluar")

def main():
	print(banner)
	url = input("Masukkan url (http(s)): ")
	ekse(url)
	
main()