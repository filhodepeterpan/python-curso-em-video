# Detector de Palíndromo

while True:
    frase = str(input("Digite uma frase: ")).lower().strip()
    
    if all(c.isalpha() or c.isspace() for c in frase):
        break
    print("\nA frase pode conter apenas letras!\n")

fraseInvertida = frase[::-1]

print(f"\nA frase digitada {'é' if fraseInvertida == frase else 'não é'} um palíndromo.")
