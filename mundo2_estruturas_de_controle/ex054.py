# Grupo da Maioridade
from datetime import date

ano_atual : int = date.today().year
maiores_idade : int = 0
qt_pessoas : int = 7

for i in range (0, qt_pessoas):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i+1}ª pessoa: "))

    if ano_nascimento < (ano_atual - 17):
        maiores_idade += 1

print(f"\nMaiores de idade: {maiores_idade}\n"
      f"Menores de idade: {qt_pessoas - maiores_idade}\n")