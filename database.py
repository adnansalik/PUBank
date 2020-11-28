import sqlite3

conn = sqlite3.connect('bank.s3db')
c = conn.cursor()


def create_account():
    c.execute('''CREATE TABLE IF NOT EXISTS account 
                            (   account_number  INTEGER UNIQUE PRIMARY KEY,
                                name            TEXT,
                                age             INTEGER,
                                card_number     TEXT,
                                pin             TEXT,
                                balance         INTEGER DEFAULT 0)''')
    conn.commit()


def do_entry(account_number, name, age, card_number, pin, balance):
    c.execute('INSERT INTO account VALUES(?,?,?,?,?,?)', (account_number, name, age, card_number, pin, balance))
    conn.commit()


def create_transact(account_number):
    c.execute(f'''CREATE TABLE IF NOT EXISTS ac{account_number} 
                            (   date            TEXT,
                                type            TEXT,
                                amount          INTEGER)''')
    conn.commit()


def do_transact(account, transact_type, transact_amount):
    account_number = 'ac' + str(account)
    values = (transact_type, transact_amount)
    c.execute(f"INSERT INTO {account_number} VALUES (datetime('now','localtime'),?,?)", values)
    conn.commit()


def get_bal(account_number):
    c.execute("SELECT balance FROM account WHERE account_number = (?)", (account_number,))
    amount = c.fetchone()
    return amount


def update_bal(account_number, amount):
    c.execute("UPDATE account SET balance = (?) WHERE account_number = (?)", (amount, account_number))
    conn.commit()


def get_acno(card_number):
    c.execute('SELECT account_number FROM account WHERE card_number = (?)', (card_number,))
    acno = c.fetchone()
    return acno


def del_account(account_number):
    c.execute('DELETE FROM account WHERE account_number = (?)', (account_number,))
    c.execute(f'DROP TABLE IF EXISTS ac{account_number}')
    conn.commit()


def check_acno(card_number, pin):
    c.execute("SELECT account_number FROM account WHERE card_number = (?) AND pin = (?)", (card_number, pin))
    account = c.fetchone()
    return account


def show_details():
    print('{:<18}{:<24}{:<7}{:<20}{:<8}{}'.format('ACCOUNT NUMBER', 'NAME', 'AGE', 'CARD NUMBER', 'PIN', 'BALANCE'))
    for acno, name, age, card, pin, bal in c.execute(f'SELECT * FROM account'):
        print("{:<18}{:<24}{:<7}{:<20}{:<8}{}".format(acno, name, age, card, pin, bal))


def get_account_info(account_number):
    c.execute('SELECT * from account WHERE account_number = (?)', (account_number,))
    info = c.fetchall()
    return info


def transaction_details(account_number):
    for ele1, ele2, ele3 in c.execute(f'SELECT * FROM ac{account_number}'):
        print("{:<23}{:<13}{}".format(ele1, ele2, ele3))


def show_mini(account_number):
    print("{:<23}{:<13}{}".format('Date', 'Type', 'Amount'))
    for ele1, ele2, ele3 in c.execute(f'SELECT * FROM ac{account_number} ORDER BY date DESC Limit 5'):
        print("{:<23}{:<13}{}".format(ele1, ele2, ele3))
