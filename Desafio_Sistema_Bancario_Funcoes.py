import textwrap
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_saques = 3
saque_total = 0
extrato_depositos = ""
extrato_saques = ""
usuario = []
contas = []
agencia = "0001"


menu = """

Digite a operção que deseja realizar:

1 - Depositar
2 - Sacar
3 - Extrato
4 - Cadastrar Usuário
5 - Criar Conta
6 - Listar Contas
7 - Sair 
"""

def deposito(valor, *, saldo, extrato_depositos):
    saldo += valor
    extrato_depositos += f"Depósito: R$ {valor:,.2f}\n"
    print(f"Valor de R$ {valor:,.2f} depositado com sucesso!")
    
    return saldo, extrato_depositos

def saque(*, saldo, saque_total, numero_de_saques, limite_saques, extrato_saques):
    saque = float(input("Valor a ser sacado:"))

    if saque <= saldo:
        if saque > saldo:
            print("Valor indisponível para saque!")
        elif numero_de_saques >= limite_saques:
            print("Limite máximo de saques diários atingidos!")
        elif saque > 500:
            print("Valor máximo para saque é R$500,00")
        elif (saque_total + saque) > 1500:
            print("Valor de R$1500,00 de saque diário excedido!")
        else:
            print(f"Valor de R$ {saque:,.2f} sacado com sucesso")
            numero_de_saques += 1
            saldo -= saque
            saque_total += saque
            extrato_saques += f"Saque de: R${saque:,.2f}\n"
    else:
        print("Saldo insuficiente!")
    
    return saldo, saque_total, numero_de_saques, extrato_saques


def funcao_extrato(*, extrato_saques="", extrato_depositos="", saldo=0):
    if extrato_saques == "" and extrato_depositos == "":
        print("Não foram realizadas movimentações.")
    else:
        print("Depósitos:")
        print(extrato_depositos)
        print("Saques:")
        print(extrato_saques)
        print(f"Saldo atual da conta R${saldo:,.2f}")


def cadastrar_usuario(usuarios):
    cpf = input("Insira seu CPF (Apenas números): ")
    if cpf_ja_cadastrado(cpf, usuarios):
        print("CPF já cadastrado")
        return

    
    nome = input("Digite seu nome completo: ")
    data_de_nascimento = input("Insira sua data de nascimento: ")
    endereco = input("Digite seu endereço completo (Rua, Número, Bairro, Cidade e Estado): ")


    usuarios +=  [{"nome": nome, "data_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco}]

    print("Usuario cadastrado!")

def cpf_ja_cadastrado(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return True
    return False
     
def conta(agencia, usuarios, numero_da_conta):
    cpf = input("Digite o CPF a ser vinculado: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Conta criada com sucesso!")
            return {"agencia": agencia, "numero_conta": numero_da_conta, "usuario": usuario}
    print("CPF não cadastrado no sistema!")
    return None

        

def lista_de_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("*" * 60)
        print(textwrap.dedent(linha))
    



while True:
    
    opcao = input(menu)

    if opcao == "1":
         
        valor = float(input("Digite o valor a ser depositado: "))
        saldo, extrato_depositos = deposito(valor, saldo=saldo, extrato_depositos=extrato_depositos)
    
    
    elif opcao == "2":
        
        saldo, saque_total, numero_de_saques, extrato_saques = saque(saldo=saldo, saque_total=saque_total, numero_de_saques=numero_de_saques, limite_saques=limite_saques, extrato_saques=extrato_saques)
                 
    elif opcao == "3":
         
        funcao_extrato(extrato_saques=extrato_saques, extrato_depositos=extrato_depositos, saldo=saldo)
          
    elif opcao == "4":
        cadastrar_usuario(usuario)
        
    elif opcao == "5":
        numero_da_conta = len(contas) + 1
        nova_conta = conta(agencia, usuario, numero_da_conta)
        if nova_conta:
            contas.append(nova_conta)
        
    
    elif opcao == "6":
        lista_de_contas(contas) 
        
        
    elif opcao == "7":
        print("Encerrando sistema, obrigado pela preferência")
        break
         
    else:
        print("Opção invalida!")

