# Grupo da Maioridade
from datetime import date

ano_atual : int = date.today().year
idade_maioridade : int = 18
adultos : int = 0
qt_pessoas : int = 7
cor_padrao: str = "\033[0m"
cor_vermelho: str = "\033[31m"
cor_verde: str = "\033[32m"

while True:
    try:
        for i in range(0, qt_pessoas):
            ano_nascimento = int(input(f"Ano de nascimento da {i + 1}ª pessoa: "))

            if ano_atual - ano_nascimento >= idade_maioridade:
                adultos += 1
        break
    except ValueError:
        print("\nVocê digitou um ano inválido. Tente novamente.")

print(f"\n{cor_verde}Maiores de idade:{cor_padrao} {adultos}\n" 
      f"{cor_vermelho}Menores de idade:{cor_padrao} {qt_pessoas - adultos}\n")