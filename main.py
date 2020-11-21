import card as cd
import database as db
import menu as mn

db.create_account()


def stop():
    db.conn.close()
    print('Bye!')


def main_menu():
    while True:
        print('\n1. Create an account\n2. Log into account\n3. Show all accounts\n0. Exit')
        choice = input()
        if choice == '1':
            cd.create_card()
            continue
        elif choice == '2':
            loggedin = mn.login(cd.check_card())
            if loggedin:
                continue
            else:
                stop()
                break
        elif choice == '3':
            db.show_details()
        elif choice == '0':
            stop()
            break


if __name__ == '__main__':
    main_menu()
