import sqlite3
import database as db
import random


def luhn(number):
    _sum = 0
    for i in range(0, len(number)):
        j = int(number[i])
        if (i + 1) % 2 != 0:
            j = j * 2
        if j > 9:
            j = j - 9
        _sum = _sum + j
    if _sum % 10 == 0:
        return 0
    else:
        return 10 - (_sum % 10)


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
