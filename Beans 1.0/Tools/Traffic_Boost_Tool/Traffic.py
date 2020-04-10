import os
import random
from time import sleep


link = str(input('The URL: '))
running = True
i = 0
countries = ['br', 'us', 'uk', 'cn', 'jp', 'sa', 'hk']

try:
    while running:
        i += 1
        os.system('curl {}'.format(link))
        os.system('exit')
        print('Try {}'.format(i))
        sleep(1)

        try:
            if i%100 == 0:
                choice = random.choice(countries)
                os.system('nordvpn disconnect')
                sleep(2)
                os.system('nordvpn c {}'.format(choice))
                print('Connected at nordvpn in: {}'.format(choice))
        except Exception as e:
            print('Error on try to connect with nordvpn, keeping in same ip')
            print('Error {}'.format(e))


except Exception as e:
    print('Error. Exiting because {}'.format(e))
    running = False
    exit()
