# YOU HAVE DELECTED ALL THE CODE AS IT IS ALL INCORRECT

# YOU HAVE TO START ALL AGAIN

print ("ERROR 404")
print ("NETWORK ERROR")
print ("CHECK YOUR MODEM / INTERNET CONNECTION")
print ("CONTACT YOUR ADMINISTRATOR OR INTERNET SERVICE PROVIDER")


Usernames=["Admin","T.Kalvin22"]
Passwords=["1111","windous22","Bluedog16","Bluemonkey16"]
user=input("Username Required")

if user in Usernames:
    password = input("Password Required")
    if password in Passwords:
        print ("Access Granted")
    else:
        print ("Access Denied")
else:
    print ("Invalid Password")

import time
time.sleep(5) 

import string
from random import*
print ("Generating Random Password...")
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print (password)      
