# Classificando Atletas
from datetime import date

while True:
    try:
        ano_nascimento = int(input("Ano de nascimento: "))
        ano_minimo = date.today().year - 120

        if ano_nascimento >= ano_minimo:
            idade: int = date.today().year - ano_nascimento
            classificacao: str = ""

            if idade >= 0:
                if idade <= 9:
                    classificacao = "MIRIM"
                elif idade <= 14:
                    classificacao = "INFANTIL"
                elif idade <= 19:
                    classificacao = "JUNIOR"
                elif idade <= 25:
                    classificacao = "SENIOR"
                else:
                    classificacao = "MASTER"

                print(f"\nCom {idade} anos, este atleta está classificado como {classificacao}.")
                break

            else:
                print("\nO atleta não pode ter uma idade negativa.\n")
        else:
            print("\nAno de nascimento inválido.\n")
    except ValueError:
        print("\nDigite apenas números inteiros.\n")