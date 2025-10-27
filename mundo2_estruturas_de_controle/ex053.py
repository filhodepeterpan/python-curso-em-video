# Detector de Palíndromo

while True:
    frase = str(input("Digite uma frase: "))
    
    if all(c.isalpha() or c.isspace() for c in frase):
        break
    print("\nA frase pode conter apenas letras!\n")

frase = frase.strip().upper().replace(" ", "")
fraseInvertida = frase[::-1]

print(f"\nO inverso de '{frase}' é '{fraseInvertida}'")
print(f"A frase digitada {'é' if fraseInvertida == frase else 'não é'} um palíndromo.")
