# Bibliotecas utilizadas
import random, textwrap
from time import sleep as ts
# --------------------- FUNÇÕES DE CRIAÇÃO ----------------------

# -------------------------- USUÁRIO ----------------------------
class user:
    # Iniciando a lista de usuários
    def __init__(self):
        self.users = []

    # Usuário e suas informações principais
    def create_user(self, id, name, birth_date, address, number, neighborhood, city, state):
        user_info = {'ID/CPF': id, 'name': name, 'birth_date': birth_date, 'address': address, 'number': number, 'Neighborhood': neighborhood, 'city': city, 'state': state, 'accounts': []}
        self.users.append(user_info)
        print("Usuário criado com sucesso!")

    # Sistema de verificação de usuários
    def user_verify(self, user_id):
        for user in self.users:
            if user['CPF'] == user_id:
                return user
        return None

# --------------------- DATA DE ANIVERSÁRIO ---------------------
def create_birth_date():
    while True:
        birth_date = input('| NASCIMENTO (DD/MM/AAAA): ')
        if len(birth_date) == 10 and birth_date[2] == '/' and birth_date[5] == '/':
            try:
                day, month, year = map(int, birth_date.split('/'))
                if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100:
                    return birth_date
            except ValueError:
                pass
        print('Data inválida')

# ----------------------- NÚMERO DE CONTA -----------------------
def account_number_generation():
    return '{:010d}'.format(random.randint(0, 9999999999))

# ---------------------------- CONTA ----------------------------
class account:
    def __init__(self):
        self.accounts = []

    def account_creation(self, agency, owner, balance):
        account_number = account_number_generation()
        account_info = {'agency': agency, 'number': account_number, 'owner': owner, "balance": balance, "transactions": [], "transactions_today": 0}

        self.accounts.append(account_info)
        owner['accounts'].append(account_info)
        return account_info

    # SELEÇÃO DE CONTA
    def account_selection(self, user):
        if len(user['accounts']) == 0:
            print('Nenhuma conta encontrada para este usuário')
            return None
        
        for index, account in enumerate(user['accounts']):
            print(f"|[{index}] CONTA: {account['number']} = SALDO: {account['balance']}")

        selected_index = int(input('Selecione a conta desejada: '))
        if 0 <= selected_index < len(user['accounts']):
            return user['accounts'][selected_index]
        else:
            print('Índice inválido')
            return None

# --------------------- FUNÇÕES DE VERIFICAÇÃO  --------------------------

def has_number(string): # Verificando a existência de números em strings importantes 
    return any(char.isdigit() for char in string)

# VERIFICANDO STRINGS
def str_input(prompt):
    while True:
        value = input(prompt)
        if not has_number(value):
            return value
        print("Dado inválido")
        
# VERIFICANDO NÚMEROS
def int_input(prompt):
    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            print("Dado inválido")


# ------------------------------ PROMPT DE CRIAÇÃO ------------------------------ 
def user_creation_prompt():
    userID = int_input("| CPF: ") 
    username =str_input("| NOME: ")
    birth_date = create_birth_date()
    address = str_input("| RUA: ")
    number = int_input("| NÚMERO: ")    
    neighborhood = str_input("| BAIRRO: ")
    city = str_input("| CIDADE: ")
    state = str_input("| ESTADO: ")
    
    return userID, username, birth_date, address, number, neighborhood, city, state

# --------------------- FUNÇÕES DE TRANSAÇÃO ---------------------

# --------------------- DEPÓSITO ---------------------
def deposit(account, amount):
    account['balance'] += amount
    
    # Registrando a transação
    transaction = {'type': 'DEPÓSITO', 'amount': amount, 'new_balance': account['balance']}
    account['transactions'].append(transaction)
    print(f'Depósito realizado com sucesso. Novo saldo: {account["balance"]}')

# --------------------- SAQUE ------------------------
def withdraw(account, *, amount):
    
    # Estabelecendo limite de transações diárias
    if account['transactions_today'] >= 3:
        print('Limite de saque diário atingido!')

    # Valor máximo de saque 
    elif amount > 500:
        print('Valor máximo para saque: R$500,00.')
    elif amount <= account['balance']:
        account['balance'] -= amount
        account['transactions_today'] += 1 # Contador para o limite de transações

        # Registrando a transação
        transaction = {'type': 'SAQUE', 'amount': amount, 'new_balance': account['balance']}
        account['transactions'].append(transaction)
        print(f'Saque realizado com sucesso. Novo saldo: {account["balance"]}')
    else:
        print('Saldo insuficiente')

# --------------------- EXTRATO ----------------------
def show_statement(account, **kwargs):
    (print('''
============================
         EXTRATO
============================
          '''))
    for transaction in account['transactions']:
        print(f'''| {transaction["type"]}: R$ {transaction["amount"]:.2f} | Saldo após a transação: R$ {transaction["new_balance"]:.2f}''')
    print(f'''| CONTA: {account["number"]} = SALDO ATUAL: R$ {account["balance"]:.2f}''')

# --------------------- CENTRO DE INFORMAÇÕES ---------------------
user_row = user()
account_row = account()


# ---------------------------- MENU PRINCIPAL -----------------------------
while True:
    menu = int(input(textwrap.dedent('''
    
    ============================
    |        BANCO DIO         |
    ============================             
    |     Criar Usuário - [1]  |
    |     Criar Conta   - [2]  |
    ============================
    |     ENTRAR        - [3]  |    
    ============================
    OPÇÃO:           ''')))
#  -------------------------------------------------------------------------
    
    # Criação de usuário
    if menu == 1:
        # Chamando o prompt de usuário com medidas para dados inválidos
        userID, username, birth_date, address, number, neighborhood, city, state = user_creation_prompt()
        
        # verificando se o CPF/ID inserido já existe
        if user_row.user_verify(userID) is not None:
            print("Usuário já cadastrado!")
        
        else:
            # Armazenando as informações na lista de usuário
            user_row.create_user(userID, username, birth_date, address, number, neighborhood, city, state)

    # Criação de conta
    elif menu == 2:
        
        userID = int(input('| CPF do proprietário da conta: '))
        user = user_row.user_verify(userID)
    
        
        if user:
            agency = "{:04d}".format(1)
            balance = float(input('| Saldo Inicial: '))
            
            # Criando e vinculando a conta ao usuário
            account_info = account_row.account_creation(agency, user, balance)
            print(f'| Conta criada com sucesso. Número da conta: {account_info["number"]}')
        else:
            print('Usuário inválido')

    # Login e seleção de conta
    elif menu == 3:
        login_id = int(input('INSIRA SEU CPF: '))
        user = user_row.user_verify(login_id)
        
        if user:
            account = account_row.account_selection(user)
            if account:
                while True:
                    print(textwrap.dedent(f'''
                    ========================================
                    | SEJA BEM VINDO, {account["owner"]["name"]}               
                    ========================================
                          '''))
                    ts(0.5) #  simulando uma tela de carregamento
                
                    # TODO:
                    #   - Editar o menu. Posicionar número de conta e nom de usuário
                    transacao_menu = int(input(textwrap.dedent(f'''
                    ========================================
                    |             BANCO DIO
                    ========================================   
                    | conta = {account_info["number"]}     
                    | SALDO = R$ {account_info["balance"]:.2f}    
                    ========================================
                    |        SELECIONE A OPERAÇÃO          
                    ========================================     
                    |    DEPÓSITO       -              [1] |
                    |    SAQUE          -              [2] |
                    |    EXTRATO        -              [3] |
                    ========================================
                    |    SAIR           -              [4] |
                    ========================================
                    |    OPÇÃO:                        ''')))

                    # DEPÓSITO
                    if transacao_menu == 1:
                        amount = float(input('Insira o valor de depósito: '))
                        deposit(account, amount)
                    
                    # SAQUE
                    elif transacao_menu == 2:
                        amount = float(input("Insira o valor de saque: "))
                        withdraw(account, amount = amount)
                    
                    # EXTRATO
                    elif transacao_menu == 3:
                        show_statement(account)
                    
                    # SAIR
                    elif transacao_menu == 4:
                        break
                        
                    else:
                        print('Opção inválida')
            # else:
            #     print('Conta inválida')
        else:
            print('Usuário inválido')
    
    else:
        print("FUNÇÃO INVÁLIDA")    