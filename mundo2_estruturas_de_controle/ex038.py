# Comparando números

while True:
    try:
        num1 = int(input("Digite um número inteiro: "))
        num2 = int(input("Digite outro número inteiro: "))

        if num1 > num2:
            print(f"\nO primeiro valor ({num1}) é maior")
        elif num2 > num1:
            print(f"\nO segundo valor ({num2}) é maior")
        else:
            print("\nOs números são iguais.")

        break

    except ValueError:
        print("\nDigite apenas números inteiros!")