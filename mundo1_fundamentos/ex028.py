# Jogo da Adivinhação v1.0
from random import randint
from time import sleep

numAleatorio: int = randint(0, 5)

chute = int(input("Tente advinhar um número entre 0 e 5: "))

print("Verificando sua resposta...")
sleep(2)

if numAleatorio == chute:
    print(f"Parabéns, você acertou! O número é {chute}")
elif chute < 0 or chute > 5:
    print(f"O desafio falhou pois você não digitou um número entre 0 e 5.")
else:
    print(f"Infelizmente, você errou. O número é {numAleatorio} e não {chute}.")