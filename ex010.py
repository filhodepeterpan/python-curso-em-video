# Conversor de moedas

valorDolar: float = 5.53 # no dia 12/10/2025

dinheiro = float(input("Quanto dinheiro você tem na carteira? R$"))

print(f"Com {dinheiro} você pode comprar US${dinheiro/valorDolar:.2f}.")