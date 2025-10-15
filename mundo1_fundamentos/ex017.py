# Catetos e Hipotenusa

from math import hypot

catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))

print(f"A hipotenusa vai medir {hypot(catetoAdjacente, catetoOposto):.2f}")