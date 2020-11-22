import sqlite3
import database as db
import random


def luhn(number):
    card_number = list(number)
    card_number = [int(x) for x in card_number]  # Converts the digits of the AccountNumber to <class 'int'>

    for i in range(0, len(card_number), 2):  # Multiplies the digits at odd(here even) index by 2
        card_number[i] = card_number[i] * 2

    for i in range(len(card_number)):  # Subtracts the digits of the AccountNumber by 9 if they are greater than 9
        if card_number[i] > 9:
            card_number[i] = card_number[i] - 9

    total = 0
    for x in card_number:
        total = total + int(x)  # Calculates the sum of digits in the AccountNumber

    last = 0
    for i in range(10):
        if (total + i) % 10 == 0:
            last = i  # Calculates the digit which when added to sum is a multiple of 10
            break

    return last


def create_card():
    fname = input('Enter your first name: ')
    lname = input('Enter your last name: ')
    name = fname + ' ' + lname
    age = int(input('Enter your age: '))
    if age <= 10:
        print('You cannot create an account now')
        return False
    bin = '400000'
    while True:
        account = str(random.randint(0, 999999999)).rjust(9, '0')
        checksum = luhn(f'{bin}{account}')
        card_number = f'{bin}{account}{checksum}'
        card_pin = str(random.randint(0, 9999)).rjust(4, '0')
        try:
            db.do_entry(account, name, age, card_number, card_pin, 0)
            db.create_transact(account)
        except sqlite3.IntegrityError:
            continue
        break
    print(f'Congratulations {name}! Your account has been created')
    print(f'Your account number:\t{account}')
    print(f'Your card number:\t{card_number}')
    print(f'Your card pin:\t{card_pin}')


def check_card():
    card_number = str(input('Enter your card number: '))
    card_pin = str(input('Enter your PIN: '))
    account = db.check_acno(card_number, card_pin)
    if account:
        return account[0]
    print('Wrong card number or PIN!')
    return False
