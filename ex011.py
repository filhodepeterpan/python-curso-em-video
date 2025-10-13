# Pintando parede

largura = float(input("Largura da parede em metros: "))
altura = float(input("Altura da parede em metros: "))
area: float = largura * altura

print(f"Sua parede tem a dimensão de {largura}m x {altura}m e sua área é de {area:.2f}m².\n"
      f"Para pintar a parede, você vai precisar de {area/2:.2f}l de tinta.")