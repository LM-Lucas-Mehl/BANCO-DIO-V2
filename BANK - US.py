# Libraries used
import random, textwrap
from time import sleep as ts
# --------------------- CREATION FUNCTIONS ----------------------

# -------------------------- USER ----------------------------
class user:
    # Starting the list of users
    def __init__(self):
        self.users = []

    # User and their main information
    def create_user(self, id, name, birth_date, address, number, neighborhood, city, state):
        user_info = {'ID/CPF': id, 'name': name, 'birth_date': birth_date, 'address': address, 'number': number, 'Neighborhood': neighborhood, 'city': city, 'state': state, 'accounts': []}
        self.users.append(user_info)
        print("User created successfully!")

    # User verification system
    def user_verify(self, user_id):
        for user in self.users:
            if user['ID'] == user_id:
                return user
        return None

# --------------------- BIRTH DATE ---------------------
def create_birth_date():
    while True:
        birth_date = input('| BIRTH DATE (MM/DD/YYYY): ')
        if len(birth_date) == 10 and birth_date[2] == '/' and birth_date[5] == '/':
            try:
                month, day, year = map(int, birth_date.split('/'))
                if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100:
                    return birth_date
            except ValueError:
                pass
        print('Invalid date')

# ----------------------- ACCOUNT NUMBER -----------------------
def account_number_generation():
    return '{:010d}'.format(random.randint(0, 9999999999))

# ---------------------------- ACCOUNT ----------------------------
class account:
    def __init__(self):
        self.accounts = []

    def account_creation(self, agency, owner, balance):
        account_number = account_number_generation()
        account_info = {'agency': agency, 'number': account_number, 'owner': owner, "balance": balance, "transactions": [], "transactions_today": 0}

        self.accounts.append(account_info)
        owner['accounts'].append(account_info)
        return account_info

    # ACCOUNT SELECTION
    def account_selection(self, user):
        if len(user['accounts']) == 0:
            print('No accounts found for this user')
            return None
        
        for index, account in enumerate(user['accounts']):
            print(f"|[{index}] ACCOUNT: {account['number']} = BALANCE: {account['balance']}")

        selected_index = int(input('Select the desired account: '))
        if 0 <= selected_index < len(user['accounts']):
            return user['accounts'][selected_index]
        else:
            print('Invalid index')
            return None

# --------------------- VERIFICATION FUNCTIONS --------------------------

def has_number(string): # Checking for the existence of numbers in important strings 
    return any(char.isdigit() for char in string)

# VERIFYING STRINGS
def str_input(prompt):
    while True:
        value = input(prompt)
        if not has_number(value):
            return value
        print("Invalid data")
        
# VERIFYING NUMBERS
def int_input(prompt):
    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            print("Invalid data")


# ------------------------------ CREATION PROMPT ------------------------------ 
def user_creation_prompt():
    userID = int_input("| CPF: ") 
    username =str_input("| NAME: ")
    birth_date = create_birth_date()
    address = str_input("| STREET: ")
    number = int_input("| NUMBER: ")    
    neighborhood = str_input("| NEIGHBORHOOD: ")
    city = str_input("| CITY: ")
    state = str_input("| STATE: ")
    
    return userID, username, birth_date, address, number, neighborhood, city, state

# --------------------- TRANSACTION FUNCTIONS ---------------------

# --------------------- DEPOSIT ---------------------
def deposit(account, amount):
    account['balance'] += amount
    
    # Recording the transaction
    transaction = {'type': 'DEPOSIT', 'amount': amount, 'new_balance': account['balance']}
    account['transactions'].append(transaction)
    print(f'Deposit successful. New balance: {account["balance"]}')

# --------------------- WITHDRAW ------------------------
def withdraw(account, *, amount):
    
    # Setting daily transaction limit
    if account['transactions_today'] >= 3:
        print('Daily withdrawal limit reached!')

    # Maximum withdrawal amount
    elif amount > 500:
        print('Maximum withdrawal amount: $500.00.')
    elif amount <= account['balance']:
        account['balance'] -= amount
        account['transactions_today'] += 1 # Counter for the transaction limit

        # Recording the transaction
        transaction = {'type': 'WITHDRAW', 'amount': amount, 'new_balance': account['balance']}
        account['transactions'].append(transaction)
        print(f'Withdrawal successful. New balance: {account["balance"]}')
    else:
        print('Insufficient funds')

# --------------------- STATEMENT ----------------------
def show_statement(account, **kwargs):
    (print('''
============================
        STATEMENT
============================
          '''))
    for transaction in account['transactions']:
        print(f'''| {transaction["type"]}: $ {transaction["amount"]:.2f} | Balance after transaction: $ {transaction["new_balance"]:.2f}''')
    print(f'''| ACCOUNT: {account["number"]} = CURRENT BALANCE: $ {account["balance"]:.2f}''')

# --------------------- INFORMATION CENTER ---------------------
user_row = user()
account_row = account()


# ---------------------------- MAIN MENU -----------------------------
while True:
    menu = int(input(textwrap.dedent('''
    
    ============================
    |        DIO BANK          |
    ============================             
    |     Create User    - [1] |
    |     Create Account - [2] |
    ============================
    |     LOGIN          - [3] |    
    ============================
    OPTION:           ''')))
#  -------------------------------------------------------------------------
    
    # User creation
    if menu == 1:
        # Calling the user prompt with measures for invalid data
        userID, username, birth_date, address, number, neighborhood, city, state = user_creation_prompt()
        
        # checking if the entered CPF/ID already exists
        if user_row.user_verify(userID) is not None:
            print("User already registered!")
        
        else:
            # Storing the information in the user list
            user_row.create_user(userID, username, birth_date, address, number, neighborhood, city, state)

    # Account creation
    elif menu == 2:
        
        userID = int(input('| Account owner ID: '))
        user = user_row.user_verify(userID)
    
        
        if user:
            agency = "{:04d}".format(1)
            balance = float(input('| Initial Balance: '))
            
            # Creating and linking the account to the user
            account_info = account_row.account_creation(agency, user, balance)
            print(f'| Account created successfully. Account number: {account_info["number"]}')
        else:
            print('Invalid user')

    # Login and account selection
    elif menu == 3:
        login_id = int(input('ENTER YOUR ID: '))
        user = user_row.user_verify(login_id)
        
        if user:
            account = account_row.account_selection(user)
            if account:
                while True:
                    print(textwrap.dedent(f'''
                    ========================================
                    | WELCOME, {account["owner"]["name"]}               
                    ========================================
                          '''))
                    ts(0.5) #  simulating a loading screen
                
                    # TODO:
                    #   - Edit the menu. Position account number and username
                    transacao_menu = int(input(textwrap.dedent(f'''
                    ========================================
                    |             DIO BANK
                    ========================================   
                    | ACCOUNT = {account["number"]}     
                    | BALANCE = $ {account["balance"]:.2f}    
                    ========================================
                    |        SELECT AN OPERATION          
                    ========================================     
                    |    DEPOSIT       -              [1] |
                    |    WITHDRAW      -              [2] |
                    |    STATEMENT     -              [3] |
                    ========================================
                    |    EXIT          -              [4] |
                    ========================================
                    |    OPTION:                        ''')))

                    # DEPOSIT
                    if transacao_menu == 1:
                        amount = float(input('Enter deposit amount: '))
                        deposit(account, amount)
                    
                    # WITHDRAW
                    elif transacao_menu == 2:
                        amount = float(input("Enter withdrawal amount: "))
                        withdraw(account, amount = amount)
                    
                    # STATEMENT
                    elif transacao_menu == 3:
                        show_statement(account)
                    
                    # EXIT
                    elif transacao_menu == 4:
                        break
                        
                    else:
                        print('Invalid option')
            # else:
            #     print('Invalid account')
        else:
            print('Invalid user')
    
    else:
        print("INVALID FUNCTION")    