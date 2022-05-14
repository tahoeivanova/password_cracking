#! /usr/bin/python

from termcolor import colored
import hashlib

def try_open(wordlist):
	global pass_file
	try:
		pass_file = open(wordlist, "r")
	except:
		print("[!!] No such file ath that path!")
		quit()

pass_hash = input("[*] Enter MD5 Hash Value: ")
wordlist = input("[*] Enter Path to the Password File: ")
try_open(wordlist)

for word in pass_file:
	print(colored("[-] Trying: %s" % word.strip("\n"), "red"))
	enc_wrd = word.encode("utf-8")
	md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

	if md5digest == pass_hash:
		print(colored("Password found: %s" % word, "green"))
		exit()
print("[!!] Password not in list")
