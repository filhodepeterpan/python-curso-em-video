# Aumentando múltiplos

salario = float(input("Digite o salário: R$ "))
porcentagem_aumento : int = 10 if salario > 1250 else 15
salarioFinal = salario + (salario * (porcentagem_aumento / 100))

print(f"Parabéns, o seu salário era de R$ {salario:.2f}, mas você recebeu um aumento de {porcentagem_aumento}% e agora passará a receber R$ {salarioFinal:.2f}.")

