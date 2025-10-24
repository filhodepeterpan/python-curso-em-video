# Progressão Aritmética

while True:
    try:
        primeiro_termo = int(input("Primeiro termo: "))
        razao = int(input("Razão: "))
        termo_atual : int = primeiro_termo

        for i in range (1, 11):
            print(f"{termo_atual}", end=" → " if i < 10 else ".")

            termo_atual += razao
        break

    except ValueError:
        print("\nValor inválido. Tente novamente\n")