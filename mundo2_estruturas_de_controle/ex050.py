# Soma dos pares

print("Digite 6 números inteiros:\n")
soma : int = 0

while True:
    try:
        for i in range (1, 7):
            num = int(input(f"Digite o {i}º número: "))

            if num % 2 == 0:
                soma += num

        print(f"\nA soma dos números pares digitados é: {soma}")
        break
    except ValueError:
        print("\nDigite apenas valores inteiros!\n")