#! /usr/bin/python

import hashlib
from termcolor import colored


sha1hash = (input("[*] Enter sha1 hash value: "))

print("Opening password list")
passwlist = open("10-million-password-list-top-1000000.txt")
print(colored("Password list opened", "green"))

for passw in passwlist.readlines():
	hashguess = hashlib.sha1(bytes(passw.strip("\n"), "utf-8")).hexdigest()
	if hashguess == sha1hash:
		print(colored("[+] The Password is: %s" % str(passw), "green"))
		quit()
	else:
		print(colored("[-] Password guess: %s doesn't match, trying next..." % str(passw), "red"))
passwlist.close()

print("Password not in passwordList")

