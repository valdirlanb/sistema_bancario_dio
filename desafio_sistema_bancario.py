menu = """


[1] Depositar
[2] Sacar
[3] Extrato

[0] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor a ser depositado: "))
        
        if valor > 0:
         saldo += valor
         extrato += f"Depósito de R$ {valor:.2f}\n"
         print(extrato)

        else:
            print("Valor inválido!")
    
    elif opcao == 2:
        valor = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")

        elif excedeu_limite:
            print("Limite excedido!")

        elif excedeu_saques:
            print("Limite de saques excedido!")

        
        elif valor > 0:
           saldo -= valor
           extrato += f"Saque de R$ {valor:.2f}\n"
           numero_saques += 1
           print(extrato)
            
            
        else:
            print("Valor inválido!")

    elif opcao == 3:
        print("\n========= EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == 0:
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Operação falhou! Digite uma opção válida.")

