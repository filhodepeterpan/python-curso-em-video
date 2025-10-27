# Grupo da Maioridade
from datetime import date

ano_atual : int = date.today().year
idade_maioridade : int = 18
adultos : int = 0
qt_pessoas : int = 7

while True:
    try:
        for i in range(0, qt_pessoas):
            ano_nascimento = int(input(f"Ano de nascimento da {i + 1}ª pessoa: "))

            if ano_atual - ano_nascimento >= idade_maioridade:
                adultos += 1
        break
    except ValueError:
        print("\nVocê digitou um ano inválido. Tente novamente.")

print(f"\nMaiores de idade: {adultos}\n" 
      f"Menores de idade: {qt_pessoas - adultos}\n")