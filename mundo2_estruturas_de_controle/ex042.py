# Analisando Triângulos v2.0

while True:
    try:
        numeros: list[int] = []
        triangulo: bool = False
        tipo_triangulo: str = ""

        for i in range(1, 4):
            numeros.append(int(input(f"Digite o {i}º segmento: ")))

        numeros.sort()

        triangulo = (numeros[0] + numeros[1]) > numeros[2]

        if triangulo:
            if numeros[0] == numeros[1] and numeros[1] == numeros[2]:
                tipo_triangulo = "EQUILÁTERO"
            if numeros[0] != numeros[1] and numeros[1] != numeros[2]:
                tipo_triangulo = "ESCALENO"
            else:
                tipo_triangulo = "ISÓSCELES"

            print(f"\nEste triângulo é do tipo {tipo_triangulo}.\n")
            break

        else:
            print("\nEstes segmentos não podem formar um triangulo.\n")

    except ValueError:
        print("\nValor inválido. Tente novamente.\n")