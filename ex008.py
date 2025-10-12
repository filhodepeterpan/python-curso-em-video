# Conversor de Medidas (+ formatação de casas após a vírgula)
valor = float(input("Digite uma medida em metros: "))

print(f"A medida de {valor}m corresponde a:\n"
      f"{(valor / 1000):.3f}km\n"
      f"{(valor / 100):.2f}hm\n"
      f"{(valor / 10):.1f}dam\n"
      f"{(valor * 10):.0f}dm\n"
      f"{(valor * 100):.0f}cm\n"
      f"{(valor * 1000):.0f}mm")