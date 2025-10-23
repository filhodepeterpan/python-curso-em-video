# Soma ímpares múltiplos de três

soma : int = 0
qt_impares : int = 0

for i in range (1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        qt_impares += 1

print(f"A soma de todos os {qt_impares} números ímpares que são múltiplos de 3 no intervalo entre 1 e 500 é: {soma}")