# Maior e menor da sequência

qt_pessoas : int = 5
mais_pesado : float = 0.0

for i in range(0, qt_pessoas):
    peso = float(input(f"Peso da {i+1}ª pessoa: "))

    if peso > mais_pesado:
        mais_pesado = peso

print(f"\nA pessoa mais pesada pesa {mais_pesado:.2f}kg.")