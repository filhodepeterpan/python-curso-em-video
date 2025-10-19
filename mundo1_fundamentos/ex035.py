# Analisando Triângulo v1.0

numeros: list[int] = []
triangulo: bool = False

for i in range(1,4):
    numeros.append(int(input(f"Digite o {i}º segmento: ")))

numeros.sort()

if numeros[0] + numeros[1] > numeros[2]:
    triangulo = True

print(f"Estes segmentos {'podem' if triangulo else 'nao podem'} formar um triângulo.")