import time
from draw import *


def email_spam():
    from Tools import Email_Spam


def traffic_boost():
    from Tools import Traffic_Boost


def main():
    menu1()
    choise = int(input("{0}Your turn:{1} ".format(GREEN, BOLD)))
    if choise == 1:
        email_spam()
    elif choise == 2:
        traffic_boost()
    elif choise == 3:
        print("{0}It was good to work with you...{1}".format(BOLD, RESET))
        input()
        clear()
        exit()



if __name__ == '__main__':
    cabecalho()
    input("{0}Press {1}{2}[ENTER]{1} {0}to continue...".format(BOLD, RESET, BLUE))
    main()
