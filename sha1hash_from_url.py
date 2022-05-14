#! /usr/bin/python

from urllib.request import urlopen
import hashlib

hashlib = (input("[*] Enter sha1 hash value: "))

url_passw = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"

print("Connecting to url password list")
passlist = str(urlopen(url_passw).read(), "utf-8")
print("Url password list connection established")

for passw in passlist.split("\n"):
	hashguess = hashlib.sha1(bytes(passw, "utf-8")).hexdigest()
	if hashguess == sha1hash:
		print("[+] The Password is: ", passw)
		quit()
	else:
		print("[-] Password guess: ", str(passw), " doesn't match, trying next...")


print("Password not in passwordList")
