#! /usr/bin/python

import hashlib


hashvalue = input("* Enter a string to hash: ")


# md5
hashobj1 = hashlib.md5() # Create a hash-object
hashobj1.update(hashvalue.encode()) #Encode value to bytes and hash it
print(hashobj1.hexdigest()) # Concert to hexdigest representation


# sha1
hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print(hashobj2.hexdigest())


# sha224
hashobj3 = hashlib.sha224()
hashobj3.update(hashvalue.encode())
print(hashobj3.hexdigest())


# sha256
hashobj3 = hashlib.sha256()
hashobj3.update(hashvalue.encode())
print(hashobj3.hexdigest())


# sha1
hashobj4 = hashlib.sha512()
hashobj4.update(hashvalue.encode())
print(hashobj4.hexdigest())
