import transactions as tr
import card as cd
import database as db


def login(account):
    if not account:
        return True

    else:
        print('\nYou have successfully logged in!')
        while True:
            print('1. Show Account Info\n2. Show Balance\n3. Deposit Money\n4. Withdraw Money\n5. Do Transfer\n6. Close Account\n7. Log Out\n8.Transactions\n9.Show Mini Statement\n0. Exit')
            choice = input()
            if choice == '1':
                account_number, name, age, card_number, pin, balance = db.get_account_info(account)[0]
                print(f'Name: {name}\nAge: {age}\nAccount Number: {account_number}\nCard Number: {card_number}\nBalance: {balance}\n')
            elif choice == '2':
                tr.balance(account)
            elif choice == '3':
                amount = int(input('Enter the amount you want to add: '))
                if amount < 100:
                    print('Amount must be more than Rs 99')
                elif amount > 500000:
                    print('Cannot add more than Rs 5,00,000')
                else:
                    tr.add_income(account, amount)
                    cur_bal = db.get_bal(account)
                    print(f'{amount} has been credited\nYour current balance now is: {cur_bal[0]}')
            elif choice == '4':
                amount = int(input('Enter the amount you want to take: '))
                tr.sub_income(account, amount)
                cur_bal = db.get_bal(account)
                print(f'{amount} has been debited\nYour current balance now is: {cur_bal[0]}')
            elif choice == '5':
                tr.do_transfer(account)
            elif choice == '6':
                check = cd.check_card()
                if check:
                    tr.del_account(check)
                    return True
            elif choice == '7':
                print('You have successfully logged out!')
                return True
            elif choice == '8':
                db.transaction_details(account)
            elif choice == '9':
                db.show_mini(account)
            elif choice == '0':
                return False
