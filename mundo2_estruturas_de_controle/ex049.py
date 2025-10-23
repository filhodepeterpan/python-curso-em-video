# Tabuada v.2.0

while True:
    try:
        numero = int(input("Digite um número inteiro para visualizar sua tabuada: "))

        print(f"\n{'=' * 12}")

        for i in range (1, 11):
            print(f"{numero} X {i} = {numero * i}")

        print(f"{'=' * 12}")
        break
    except ValueError:
        print("\nDigite apenas numeros inteiros!\n")