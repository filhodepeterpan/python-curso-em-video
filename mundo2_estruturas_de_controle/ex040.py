# Aquele clássico da média

print("Vamos calcular sua média do semestre!\n")

while True:
    try:
        nota1 = float(input("Digite sua primeira nota: "))
        nota2 = float(input("Digite sua segunda nota: "))
        resultado : str = ""
        mensagem : str = ""

        media : float = (nota1 + nota2) / 2

        if media >= 7:
            resultado = "APROVADO"
            mensagem = "PARABÉNS"
        elif media >= 5:
            resultado = "EM RECUPERAÇÃO"
            mensagem = "Cuidado"
        else:
            resultado = "REPROVADO"
            mensagem = "Que pena"

        print(f"\n{mensagem}. Você está {resultado}.")
        break

    except ValueError:
        print("Digite apenas números.")