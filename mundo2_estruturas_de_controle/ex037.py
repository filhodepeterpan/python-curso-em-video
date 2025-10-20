# Conversor de Bases Numéricas

num = int(input("Digite um número inteiro: "))
resultado = ""
tipo_conversao : str = ""

print("Escolha uma das bases para conversão:\n"
      "[ 1 ] converter para BINÁRIO\n"
      "[ 2 ] converter para OCTAL\n"
      "[ 3 ] converter para HEXADECIMAL\n")

while True:
    try:
        opcao = int(input("\nSua opção: "))

        if opcao == 1:
            resultado = bin(num)
            tipo_conversao = "binário"
            break
        elif opcao == 2:
            resultado = oct(num)
            tipo_conversao = "octal"
            break
        elif opcao == 3:
            resultado = hex(num)
            tipo_conversao = "hexadecimal"
            break
        else:
            print("Opção inválida. Escolha apenas 1, 2 ou 3.")

    except ValueError:
        print("\nDigite apenas números. Escolha 1, 2 ou 3.")

print(f"\n{num} em {tipo_conversao} é {resultado[2:]}.")