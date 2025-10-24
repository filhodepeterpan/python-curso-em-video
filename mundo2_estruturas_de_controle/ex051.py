# Progressão Aritmética

while True:
    try:
        primeiro_termo = int(input("Primeiro termo: "))
        razao = int(input("Razão: "))
        termo_atual : int = primeiro_termo

        for i in range (1, 11):
            print(f"{i}º termo: {termo_atual}")

            termo_atual += razao
        break

    except ValueError:
        print("\nValor inválido. Tente novamente\n")