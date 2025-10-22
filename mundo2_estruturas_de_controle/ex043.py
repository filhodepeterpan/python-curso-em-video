# Índice de Massa Corporal

while True:
    try:
        peso = float(input("Digite seu peso em quilos: "))
        altura = float(input("Digite sua altura em metros: "))
        classificacao : str = ""

        imc : float = peso / (altura * altura)

        if imc < 18.5:
            classificacao = "ABAIXO DO PESO"
        elif imc <= 25:
            classificacao = "PESO IDEAL"
        elif imc <= 30:
            classificacao = "SOBREPESO"
        elif imc <= 40:
            classificacao = "OBESIDADE"
        else:
            classificacao = "OBESIDADE MÓRBIDA"

        print(f"Seu IMC é de {imc:.2f} e sua classificação é: {classificacao}.")

        break
    except ValueError:
        print("\nValores inválidos. Tente novamente.")