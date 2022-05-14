#! /usr/bin/python

import crypt
from termcolor import colored


def crackPassw(cryptWord):
	salt = cryptWord[0:2] #salt is 1st two letters
	dictionary = open("dictionary_passw.txt") # Open files with potential passwords
	for word in dictionary.readlines():
		word = word.strip("\n")
		cryptPassw = crypt.crypt(word, salt) # Turn passwords to hashed values with salt
		if (cryptWord == cryptPassw): # Compare salt hashed values
			print(colored("[+] Found Password: %s" % word, "green"))
			return True


def main():
	passFile = open("login_and_hashed_passw.txt") # Open file with a hased pass

	for login_hash in passFile.readlines():
		if ":" in login_hash:
			user = login_hash.split(":")[0]
			cryptWord = login_hash.split(":")[1].strip(" ").strip("\n")
			print("[*] Cracking Password for %s" % user)
			if crackPassw(cryptWord):
				quit()
			else:
				print(colored("[-] Password Not Found", "red"))



if __name__ == "__main__":
	main()
