from draw import clear, RESET

def main():
    clear()
    print("Please set up all needed on the email spam tool path, once is done press enter.{0}".format(RESET))
    a = input()
    if a == "":
        from Tools.Email_Spam_Tool import Emailing
    else:
        print("I told you to press enter")
        exit()
        
main()
