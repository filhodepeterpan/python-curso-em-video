# Contagem Regressiva

from time import sleep

print("Os fogos de artífico vão estourar em:\n")

for n in range(10, 0, -1):
    print(f"{n}...")
    sleep(1)

print("ESTOUROU!")