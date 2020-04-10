from draw import clear, RESET

def main():
    clear()
    print("Please connect to a nordvpn account, once is done press enter.{0}".format(RESET))
    a = input()
    if a == "":
        from Tools.Traffic_Boost_Tool import Traffic
    else:
        print("I told you to press enter")
        exit()
        
main()
