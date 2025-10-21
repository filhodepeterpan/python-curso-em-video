# Analisando Triângulos v2.0

while True:
    try:
        segmentos: list[float] = []
        triangulo: bool = False
        tipo_triangulo: str = ""

        for i in range(1, 4):
            segmentos.append(float(input(f"Digite o {i}º segmento: ")))

        segmentos.sort()

        triangulo = (segmentos[0] + segmentos[1]) > segmentos[2]

        if triangulo:
            if segmentos[0] == segmentos[1] and segmentos[1] == segmentos[2]:
                tipo_triangulo = "EQUILÁTERO"
            elif segmentos[0] != segmentos[1] and segmentos[1] != segmentos[2] and segmentos[2] != segmentos[0]:
                tipo_triangulo = "ESCALENO"
            else:
                tipo_triangulo = "ISÓSCELES"

            print(f"\nEste triângulo é do tipo {tipo_triangulo}.\n")
            break

        else:
            print("\nEstes segmentos não podem formar um triangulo.\n")

    except ValueError:
        print("\nValor inválido. Tente novamente.\n")