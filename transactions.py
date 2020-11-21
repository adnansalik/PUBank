import database as db
import card as cd


def balance(account_number):
    cur_bal = db.get_bal(account_number)
    print(f'Your balance is:\n{cur_bal[0]}\n')


def add_income(account_number, amount):
    cur_bal = db.get_bal(account_number)
    cur_bal = cur_bal[0] + amount
    db.update_bal(account_number, cur_bal)
    t_type = 'Deposited'
    db.do_transact(account_number, t_type, amount)
    print(f'{amount} has been credited\n')


def sub_income(account_number, amount):
    cur_bal = db.get_bal(account_number)
    if amount > cur_bal:
        print("You don't have enough balance")
    else:
        cur_bal = cur_bal[0] - amount
        db.update_bal(account_number, cur_bal)
        t_type = 'Withdrawn'
        db.do_transact(account_number, t_type, amount)


def do_transfer(account):
    card = input(f"Transfer\nEnter recipient's card number:\n")
    transfer_id = db.get_acno(card)
    sender_bal = db.get_bal(account)
    if str(cd.luhn(card[:15])) != card[-1]:
        print('Probably you made a mistake in the card number. Please try again')
    elif not transfer_id:
        print('Such a card does not exist.')
    elif account == transfer_id[0]:
        print('Cannot transfer the money to the same account')
    else:
        amt = int(input('Enter the amount you want to transfer: '))
        if amt > sender_bal[0]:
            print("You don't have enough balance: ")
        else:
            add_income(transfer_id[0], amt)
            sub_income(account, amt)


def del_account(account_number):
    db.del_account(account_number)
    print('The account has been closed')
