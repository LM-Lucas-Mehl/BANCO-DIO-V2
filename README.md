# PROJETO: SISTEMA BANCÁRIO

Projeto baseado na proposta feita por [DIO](https://www.dio.me), através do curso **Formação Python Developer**


## DESCRIÇÃO

Aprimorando o sistema bancário, agora com cadastro de clientes e contas, e um sistema de armazenamento para ambos.
 
Como solicitado, foram utilizados argumentos posicionais e palavras chaves nas seguintes funções: **SAQUE**, **DEPÓSITO**, **EXTRATO**.



**FUNÇÕES REQUISITADAS:** Depósito, Saque, Extrato, Criação de conta e Usuário, Vínculo entre usuário e conta.


### DEPOSITO
----
Atualização de função para trabalhar com múltiplos usuários e contas

Identificação de agência e número de conta

Todos os depósitos devem ser armazenados em uma variável e devem ser apresentados na função **EXTRATO**



### SAQUE 
----
Limite de saques por dia: 3, limite máximo de saque: R$ 500,00

Checar o saldo disponível na conta atual, verificar se é possível realizar a operação.

Todos os saques devem ser armazenados em uma variável e devem ser apresentados na função **extrato**


### EXTRATO 
----
Todos os **depositos** e **saques** da conta atual devem ser apresentados

No final, o saldo atual deve ser apresentado

**Valores** devem ser exibidos no seguinte **formato**: R$ XXX.XX
1500.45 = R$ 1500.45**

----
### CADASTRO DE USUÁRIO
Realizando o cadastro e coletando as seguintes informações:

    > CPF
    > Nome
    > Data de aniversário
    > Endereço:
        > Número
        > Bairro
        > Cidade
        > Estado

armazenando-as, posteriormente em um dicionário.

----

### CRIAÇÃO DE CONTA
Realizando a criação de conta, contendo agencia e números.

Armazenando-as posteriormente em uma lista e vinculando a mesma a um usuário existente.

Lembrando que:
    
    Número da agencia: 0001 - Sendo um número fixo imutável
    Uma conta pertence a apenas um usuário.

<br>
<br>
<br>

----

<br>
<br>
<br>

# PROJECT: BANKING SYSTEM

Project based on the proposal made by [DIO](https://www.dio.me), through the **Formação Python Developer** course.

## DESCRIPTION

Enhancing the banking system, now with customer and account registration, and a storage system for both.

As requested, positional and keyword arguments were used in the following functions: **WITHDRAW**, **DEPOSIT**, **STATEMENT**.

**REQUIRED FUNCTIONS:** Deposit, Withdraw, Statement, Account Creation, and User Creation, Link between user and account.

### DEPOSIT

----

Function update to work with multiple users and accounts.

Identification of agency and account number.

All deposits must be stored in a variable and should be displayed in the **STATEMENT** function.

### WITHDRAW

----

Daily withdrawal limit: 3, maximum withdrawal limit: $500.00.

Check the available balance in the current account and verify if the operation is possible.

All withdrawals must be stored in a variable and should be displayed in the **statement** function.

### STATEMENT

----

All **deposits** and **withdrawals** of the current account must be displayed.

At the end, the current balance must be presented.

**Values** should be displayed in the following **format**: $XXX.XX (1500.45 = $1500.45)

----

### USER REGISTRATION

Registering and collecting the following information:

    > CPF
    > Name
    > Birth Date
    > Address:
        > Number
        > Neighborhood
        > City
        > State

storing them in a dictionary.

----

### ACCOUNT CREATION

Creating an account, containing agency and numbers.

Storing them in a list and linking them to an existing user.

Keep in mind that:

    Agency Number: 0001 - Being a fixed immutable number
    An account belongs to only one user.

----