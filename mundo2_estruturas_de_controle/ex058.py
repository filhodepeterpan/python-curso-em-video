# Jogo da Adivinhação v2.0

from random import randint


numAleatorio: int = randint(0, 10)
chute : int | None = None
tentativas : int = 0

while chute != numAleatorio:
    chute = int(input("\nTente advinhar um número entre 0 e 10: "))

    if 0 > chute > 5:
        print(f"\nO desafio falhou pois você não digitou um número entre 0 e 10.")
    else:
        print(f"\nO número sorteado é {'maior' if chute < numAleatorio else 'menor'} que {chute}.")
        tentativas += 1

print(f"\nParabéns, o número é {chute}! Você acertou com {tentativas} {'tentativas' if tentativas > 1 else 'tentativa'}.")