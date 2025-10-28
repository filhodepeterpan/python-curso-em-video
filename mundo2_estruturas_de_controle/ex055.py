# Maior e menor da sequência

qt_pessoas : int = 5
mais_pesado : float = 0.0
menos_pesado : float = 0.0

for i in range(0, qt_pessoas):
    peso = float(input(f"Peso da {i+1}ª pessoa: "))

    if i == 0 : menos_pesado = peso

    if peso > mais_pesado : mais_pesado = peso
    if peso < menos_pesado: menos_pesado = peso

print(f"\nAMaior peso: {mais_pesado:.1f}kg.\n"
      f"Menor peso: {menos_pesado:.1f}kg.")