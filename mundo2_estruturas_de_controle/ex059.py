# Criando um menu de opções

opcao : int = 0

def pega_valores():
    while True:
        try:
            a = float(input("\nDigite o valor de x: "))
            b = float(input("Digite o valor de y: "))
            return a, b

        except ValueError:
            print("\nValor inválido. Tente novamente.")

x, y = pega_valores()

while opcao != 5:

    print("\nOPÇÕES:\n"
          "[ 1 ] Somar valores\n"
          "[ 2 ] Multiplicar valores\n"
          "[ 3 ] Maior valor\n"
          "[ 4 ] Novos valores\n"
          "[ 5 ] Sair do programa")

    while True:
        try:
            opcao = int(input("\nDigite qual a sua opção: "))

            if 5 >= opcao >= 1:
                if opcao == 1:
                    print(f"A soma dos valores é {x + y}.")
                if opcao == 2:
                    print(f"A multiplicação dos valores é {x * y}.")
                if opcao == 3:
                    print(f"O maior valor é {x if x > y else y}.")
                if opcao == 4:
                    x, y = pega_valores()
                break
            else:
                print("\nValor inválido. Tente novamente.")

        except ValueError:
            print("\nDigite apenas números inteiros.")

print("\nPrograma finalizado.")