from pyfiglet import Figlet
from termcolor import colored
import socket

def title():
    titleformat = Figlet(font='larry3d')
    title = titleformat.renderText('UDON KNOW ME')
    print(colored(title, 'green'))
def menu():
    print('1. Scan for Open Ports\n2. IP Address Identifier\n3. Exit Program')

def ipidentifier():
    hoster = input('Enter host to search up: ')
    ipresult = socket.gethostbyname(hoster)
    print("The IP Address found is: " + ipresult)
while True:
    title()
    menu()
    userInput = input('Enter a selection from 1-3 here: ')
    if userInput == '1':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        targweb = input('Website you would like to ping? ')
        targip = socket.gethostbyname(targweb)
        print('Starting scan on ' + targip)
        for x in range(1, 1000):
            sopen = sock.connect_ex((targip, x))
            if sopen == 0:
                print('Port %d: OPEN' % (i, ))
            sock.close()
        print('No other ports found to be open!')
    elif userInput == '2':
        ipidentifier()
    elif userInput == '3':
        print("\033c")
        print(colored('''                龴ↀ ◡ ↀ  龴               ''', 'green'))
        print(colored('°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸', 'green'))
        print(colored('Have a nice day, fellow hacker!', 'green', attrs=['bold']))
        print(colored('°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸', 'green'))
        break
