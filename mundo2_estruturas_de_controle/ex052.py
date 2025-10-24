# Números primos

print(f"{'=-' * 20}")
print("IDENTIFICADOR DE NÚMEROS PRIMOS")
print(f"{'=-' * 20}\n")
while True:
    try:
        num = int(input("Digite um número inteiro: "))
        num_primo : bool = True

        if num < 3:
            num_primo = False
        else:
            for i in range (2, num-1):
                if num % i == 0:
                    num_primo = False
                    break

        print(f"\n{num} {'é' if num_primo else 'não é'} um número primo.")
        break

    except ValueError:
        print("\nDigite apenas um número inteiro.\n")