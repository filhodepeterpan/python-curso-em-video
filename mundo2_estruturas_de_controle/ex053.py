# Detector de Palíndromo

while True:
    frase = str(input("Digite uma frase: "))
    
    if all(c.isalpha() or c.isspace() for c in frase):
        break
    print("\nA frase pode conter apenas letras!\n")

frase = frase.strip().upper()
fraseInvertida = frase[::-1]
palindromo = frase.replace(" ", "") == fraseInvertida.replace(" ", "")

print(f"\nO inverso de '{frase}' é '{fraseInvertida}'")
print(f"A frase digitada {'é' if palindromo else 'não é'} um palíndromo.")
