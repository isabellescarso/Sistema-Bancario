menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        print("Opção selecionada: Depósito.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        valor_deposito = float(input("Insira o valor que deseja depositar: "))

        if valor_deposito < 0:
                print("Valor negativo. Por gentileza insira um valor positivo para depósito!")
        else:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"\nSaldo: R$ {saldo:.2f}")


    elif opcao == "s":
        print("Opção selecionada: Saque")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        valor_saque = float(input("Insira o valor que deseja sacar: "))
        if numero_saques <= LIMITE_SAQUES and valor_saque <= limite and valor_saque < saldo:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
        else:
             print("Valor inválido ou limite de saques diários excedidos. Tente novamente!")

    elif opcao == "e":
        print("Opção selecionada: Extrato")   
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        
    elif opcao == "q":
       break
    
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")