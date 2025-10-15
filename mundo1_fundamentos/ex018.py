# Seno, Cosseno e Tangente
from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo que você deseja: "))

print(f"O ângulo de {angulo} tem:\n"
      f"Seno de {sin(radians(angulo)):.2f}.\n"
      f"Cosseno de {cos(radians(angulo)):.2f}.\n"
      f"Tangente de {tan(radians(angulo)):.2f}.")