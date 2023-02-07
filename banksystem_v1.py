import random
# skrald mig i øret, jeg afhængig af if else

# global variables
cards = {}
balance = 0
correct = False

print("""1. Create an account
2. Log into account
0. Exit""")


# creates an account with card number and pin, prints and stores in cards{}
def create_account():
    global cards
    bin_number = str(400000)
    account_number = str(random.randint(1, 999999999))
    check_sum = str(random.randint(1, 9))
    pin_number = str(random.randint(1000, 9999))
    card_number = bin_number + account_number + check_sum
    store_account(card_number, pin_number)
    print('Your card has been created\n'
          'Your card number:\n' + card_number +
          '\nYour card PIN:\n' + pin_number)


# stores account in cards {}
def store_account(number, pin):
    global cards
    cards[number] = pin


# "logs in" the user if the input is correct
def login():
    global cards
    global correct
    print('Enter your card number:')
    card_number = input()
    print('Enter your PIN:')
    pin_number = input()
    if card_number in cards and pin_number in cards[card_number]:
        print('You have successfully logged in!')
        correct = True
    else:
        print('Wrong card number or PIN!')


# shows balance, will probably be changeable later
def show_balance():
    global balance
    print('Balance : ' + str(balance))


# logs out the user
def logout():
    print('You have successfully logged out!')


# exits the program
def exit_bank():
    print('Bye!')
    quit()


# runs the whole thing, baby
while True:
    print('\n1. Create an account\n'
          '2. Log into account\n'
          '0. Exit')
    choice = input()
    if choice == '1':
        create_account()
        continue
    elif choice == '2':
        login()
        while correct:
            print('\n1. Balance\n'
                  '2. Log out\n'
                  '0. Exit')
            choice = input()
            if choice == '1':
                show_balance()
                continue
            elif choice == '2':
                logout()
                break
            elif choice == '0':
                exit_bank()
        else:
            continue
    elif choice == '0':
        exit_bank()
