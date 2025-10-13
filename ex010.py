# Conversor de moedas

# Cotações do dia 12/10/2025
valorDolar: float = 5.53
valorEuro: float = 6.41

dinheiro = float(input("Quanto dinheiro você tem na carteira? R$"))

print(f"Com {dinheiro:.2f} você pode comprar US${dinheiro/valorDolar:.2f} ou €{dinheiro/valorEuro:.2f}.")