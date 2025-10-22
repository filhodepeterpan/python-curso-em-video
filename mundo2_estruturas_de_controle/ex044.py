# Gerenciador de pagamentos

while True:
    try:
        valor_compras = float(input("Digite o valor da compra: R$ "))
        valor_total : float = 0.0
        desconto: int = 0
        juros: int = 0
        forma_pagamento : str = ""

        print("\nFORMAS DE PAGAMENTO:\n")
        print("[ 1 ] à vista dinheiro/cheque\n"
              "[ 2 ] à vista cartão\n"
              "[ 3 ] 2x no cartão\n"
              "[ 4 ] 3x ou mais no cartão\n")

        opcao = int(input("Qual sua opção?: "))

        if 1 <= opcao <= 4:

            if opcao == 1 or opcao == 2:
                forma_pagamento = "À vista (dinheiro/cheque)" if opcao == 1 else "À vista (cartão)"
                desconto = 10 if opcao == 1 else 5
                valor_total = valor_compras - (valor_compras * (desconto / 100))
            elif opcao == 3:
                forma_pagamento = "2x no cartão"
                valor_total = valor_compras
            else:
                forma_pagamento = "3x ou mais no cartão"
                juros = 20
                valor_total = valor_compras + (valor_compras * (juros / 100))

            print(f"\nValor da compra: R$ {valor_compras:.2f}\n"
                  f"Forma de pagamento: {forma_pagamento}\n"
                  f"Porcentagem de desconto: {desconto}%\n"
                  f"Porcentagem de juros: {juros}%\n"
                  f"VALOR TOTAL: R$ {valor_total:.2f}\n")
            break
        else:
            print("\nOpção válida. Digite um número entre 1 e 4.\n")
    except ValueError:
        print("\nOpção inválida. Tente novamente.")