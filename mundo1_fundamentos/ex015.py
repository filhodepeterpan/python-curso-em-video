# Aluguel de Carros

diasAlugados = int(input("Por quantos dias o carro foi alugado? "))
kmRodados = float(input("Quantos km foram rodados? "))

valorFinal: float = (diasAlugados * 60) + (kmRodados * 0.15)

print(f"O total a pagar é {valorFinal:.2f}.")