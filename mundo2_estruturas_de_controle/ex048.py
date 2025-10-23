# Soma ímpares múltiplos de três

soma : int = 0

for i in range (1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i

print(f"Esta é a soma de todos os números ímpares que são múltiplos de 3 no intervalo entre 1 e 100: {soma}")