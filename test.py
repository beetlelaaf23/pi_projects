import sys
import time
import os
import random

def name():
    g = input('Username: ')
    if g != 'close':
        if g.lower().replace(" ", "") == 'admin':
            a = input('password: ')
            if a == '123':
                print('\nWelcome ', g.lower().replace(" ", ""))
                print('\nProcessing...')
                time.sleep(.5)
                print('Searching Database...')
                time.sleep(.5)
                print('Checking For Valid User...')
                time.sleep(.5)
                print('retrieving User Info...')
                time.sleep(.5)
                print('Done.\n')
                comment()
            else:
                print('Wrong Password!\n')
                name()
        else:
            print('It looks like your not registered in the system. \n')
            name()
    else:
        print('\n Goodbye!')
        time.sleep(2)
        sys.exit(0)


def comment():
    print('Ready.')
    action = input('> ')
    action = action.lower().replace(" ", "")
    if action == '/logout':
        os.system('cls')
        name()
        return
    elif action == '/exit':
        print('Goodbye')
        time.sleep(1)
        sys.exit(0)
    elif action == '/numgame':
        os.system('cls')
        for x in range(25):
            print('>>> #Rob Ottenhof#')
            time.sleep(.05)
        os.system('cls')
        numgame()
    elif action == '/help':
        print('\navailable commands: \n'
              '- /help\n'
              '- /exit\n'
              '- /logout\n'
              '- /numgame\n')
        comment()
    else:
        print('command does not exist \n')
        comment()


def numgame():
    print('\n[NumberGame]')
    print('\nWelcome to the number game!\n')
    y = input('type "/start" to begin. or type "/close" to exit\n>')

    if y == '/close':
        os.system('cls')
        comment()
        return
    elif y == '/start':
        
        def number_game():
            random_number = random.randint(0, 11)
            os.system('cls')
            input_number = int(input("Guess the number between 0 to 10 \n"))

            if input_number == random_number:
                print("Correct!\n")
                z = input('Do you want to play again? type "yes" or "no"\n')
                if z == 'yes':
                    number_game()
                else:
                    os.system('cls')
                    comment()
                    return
            else:
                print("Wrong")
                time.sleep(.5)
                number_game()

        number_game()
    numgame()


name()
comment()
numgame()

