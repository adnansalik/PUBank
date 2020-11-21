import transactions as tr
import database as db


def login(account):
    if not account:
        return True

    else:
        print('\nYou have successfully logged in!')
        while True:
            print('1. Show Account Info\n2. Show Balance\n3. Deposit Money\n4. Withdraw Money\n5. Do Transfer\n6. Close Account\n7. Log Out\n8.Transactions\n0. Exit')
            choice = input()
            if choice == '1':
                account_number, name, card_number, pin, balance = db.get_account_info(account)[0]
                print(f'Name: {name}\nAccount Number: {account_number}\nCard Number: {card_number}\nBalance: {balance}\n')
            elif choice == '2':
                tr.balance(account)
            elif choice == '3':
                amount = int(input('Enter the amount you want to add: '))
                tr.add_income(account, amount)
            elif choice == '4':
                amount = int(input('Enter the amount you want to take: '))
                tr.sub_income(account, amount)
                print(f'{amount} has been debited\n')
            elif choice == '5':
                tr.do_transfer(account)
            elif choice == '6':
                tr.del_account(account)
                return True
            elif choice == '7':
                print('You have successfully logged out!')
                return True
            elif choice == '8':
                db.transaction_details(account)
            elif choice == '0':
                return False
