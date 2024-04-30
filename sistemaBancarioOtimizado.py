import textwrap

def menu():
    menu_text = """
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """

    return input(textwrap.dedent(menu_text))

def depositar(saldo, extrato):
    print("Opção selecionada: Depósito.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    valor_deposito = float(input("Insira o valor que deseja depositar: "))

    if valor_deposito < 0:
        print("Valor negativo. Por gentileza insira um valor positivo para depósito!")
    else:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"\nSaldo: R$ {saldo:.2f}")
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    print("Opção selecionada: Saque")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    valor_saque = float(input("Insira o valor que deseja sacar: "))

    if numero_saques < limite_saques and valor_saque <= limite and valor_saque <= saldo:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        numero_saques += 1
        print(f"\nSaldo: R$ {saldo:.2f}")
    else:
        print("Valor inválido ou limite de saques diários excedidos. Tente novamente!")

    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("Opção selecionada: Extrato")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    usuarios.append({"nome": nome, "cpf": cpf})
    print("Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário associado à conta: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            conta = {"agencia": agencia, "numero_conta": numero_conta, "cpf": cpf}
            print(f"Conta criada com sucesso para o usuário: {usuario['nome']}")
            return conta
    print("Usuário não encontrado. Não foi possível criar a conta.")
    return None

def listar_contas(contas):
    print("Listagem de Contas:")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(f"Agência: {conta['agencia']} | Número da Conta: {conta['numero_conta']} | CPF: {conta['cpf']}")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
