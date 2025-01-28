import getpass
import os

# Creating lists of users, their PINs, and account balances
users = ['user', 'user2', 'user3']  # List of usernames
pins = ['1234', '2222', '3333']  # Corresponding PINs for the users
amounts = [1000, 2000, 3000]  # Account balances for each user
count = 0  # Counter for invalid PIN attempts

# Loop to check if the entered username exists
while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()  # Convert to lowercase to handle case insensitivity
    if user in users:  # Check if the entered username exists in the user list
        # Identify the index of the user for later reference
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break  # Exit the loop if the username is valid
    else:
        # Notify the user of an invalid username
        print('----------------')
        print('****************')
        print('INVALID USERNAME')
        print('****************')
        print('----------------')

# Loop to compare the entered PIN
while count < 3:  # Allow up to 3 attempts
    print('------------------')
    print('******************')
    pin = str(getpass.getpass('PLEASE ENTER PIN: '))  # Input PIN securely
    print('******************')
    print('------------------')

    # Validate if the entered PIN is numeric
    if pin.isdigit():
        # Check if the PIN matches the username's PIN
        if user == 'user' and pin == pins[0]:
            break
        elif user == 'user2' and pin == pins[1]:
            break
        elif user == 'user3' and pin == pins[2]:
            break
        else:
            count += 1  # Increment the invalid attempt counter
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()
    else:
        # Notify the user if the PIN is not numeric or invalid
        print('------------------------')
        print('************************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('************************')
        print('------------------------')
        count += 1

# Exit if the user fails to enter the correct PIN in 3 attempts
if count == 3:
    print('-----------------------------------')
    print('***********************************')
    print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('***********************************')
    print('-----------------------------------')
    exit()

# Login successful
print('-------------------------')
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')    
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')

# Main menu loop
while True:
    print('-------------------------------')
    print('*******************************')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
    print('*******************************')
    print('-------------------------------')

    valid_responses = ['s', 'w', 'l', 'p', 'q']
    response = response.lower()

    # Option to view account balance
    if response == 's':
        print('---------------------------------------------')
        print('*********************************************')
        print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'RS ON YOUR ACCOUNT.')
        print('*********************************************')
        print('---------------------------------------------')

    # Option to withdraw money
    elif response == 'w':
        print('---------------------------------------------')
        print('*********************************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('*********************************************')
        print('---------------------------------------------')

        # Validate withdrawal amount
        if cash_out % 10 != 0:
            print('------------------------------------------------------')
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST MATCH 100 RS NOTES')
            print('******************************************************')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
            print('-----------------------------')
        else:
            amounts[n] = amounts[n] - cash_out  # Deduct from balance
            print('-----------------------------------')
            print('***********************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RS')
            print('***********************************')
            print('-----------------------------------')

    # Option to deposit money
    elif response == 'l':
        print('---------------------------------------------')
        print('*********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
        print('*********************************************')
        print('---------------------------------------------')

        if cash_in % 10 != 0:
            print('----------------------------------------------------')
            print('****************************************************')
            print('AMOUNT YOU WANT TO LODGE MUST MATCH 100 RS NOTES')
            print('****************************************************')
            print('----------------------------------------------------')
        else:
            amounts[n] = amounts[n] + cash_in  # Add to balance
            print('----------------------------------------')
            print('****************************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RS')
            print('****************************************')
            print('----------------------------------------')

    # Option to change PIN
    elif response == 'p':
        print('-----------------------------')
        print('*****************************')
        new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
        print('*****************************')
        print('-----------------------------')

        # Validate new PIN
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            print('------------------')
            print('******************')
            new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
            print('*******************')
            print('-------------------')

            if new_ppin != new_pin:
                print('------------')
                print('************')
                print('PIN MISMATCH')
                print('************')
                print('------------')
            else:
                pins[n] = new_pin  # Save the new PIN
                print('NEW PIN SAVED')
        else:
            print('-------------------------------------')
            print('*************************************')
            print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
            print('*************************************')
            print('-------------------------------------')

    # Option to quit
    elif response == 'q':
        print('Thanks for using ATM Service!')
        exit()

    # Handle invalid responses
    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')
