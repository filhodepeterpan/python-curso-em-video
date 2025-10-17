# Jogo da Advinhação v.1.0
from random import randint

numAleatorio: int = randint(0, 5)

chute = int(input("Tente advinhar um número entre 0 e 5: "))

if numAleatorio == chute:
    print(f"Parabéns, você acertou! O número é {chute}")
elif chute < 0 or chute > 5:
    print(f"O desafio falhou pois você não digitou um número entre 0 e 5.")
else:
    print(f"Infelizmente, você errou... o número é {numAleatorio} e não {chute}.")