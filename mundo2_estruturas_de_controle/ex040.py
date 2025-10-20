# Aquele clássico da média

print("Vamos calcular sua média do semestre!\n")

while True:
    try:
        nota1 = float(input("Digite sua primeira nota: "))
        nota2 = float(input("Digite sua segunda nota: "))
        resultado : str = ""

        media = (nota1 + nota2) / 2

        if media >= 7:
            resultado = "APROVADO"

        elif media >= 5:
            resultado = "EM RECUPERAÇÃO"
        else:
            resultado = "REPROVADO"

        print(f"\n{'PARABÉNS' if resultado == 'APROVADO' else 'Que pena' if resultado == 'REPROVADO' else 'Cuidado'}. Você está {resultado}.")
        break

    except ValueError:
        print("Digite apenas números.")