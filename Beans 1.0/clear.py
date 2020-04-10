import platform
import os

sistem = platform.system()

def clear():
    if sistem == "Linux" or "Darwin":
        os.system('clear')
    elif sistem == "Windows":
        os.system('cls')
    else:
        print('The OS detection has failed. Exiting...')
        exit() 
