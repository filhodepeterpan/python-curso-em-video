# Analisador completo

# ENUNCIADO: Desenvolva um programa que leia o nome, idade e gênero de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

from typing import List, Dict

qt_pessoas = int(input("Quantas pessoas você gostaria de analisar? "))
dados: List[Dict[str, str | int]] = []

for i in range (0, qt_pessoas):

    print(f"\n ===== {i + 1}ª PESSOA =====\n")

    nome = str(input(f"Nome: ")).strip().capitalize()
    idade = int(input(f"Idade: "))
    genero = str(input(f"Gênero: ")).strip().upper()[0]

    print("\n")

    dados.append({
        "nome": nome,
        "idade": idade,
        "genero": genero,
    })

media_idades : float = sum(p["idade"] for p in dados) / qt_pessoas
mulheres_menores_20 : int = 0
homem_mais_velho : str = "" if 'M' in [p["genero"] for p in dados] else "não há"
idade_homem_mais_velho : int = 0

print(f"\n===== TABELA DE DADOS =====\n"
      f"{'NOME':<10} | {'IDADE':<5} | {'GENERO':<6}")

for p in dados:
    if p ["genero"] == "M":
        if p["idade"] > idade_homem_mais_velho:
            idade_homem_mais_velho = p["idade"]
            homem_mais_velho = p["nome"]

    if p["genero"] == "F":
        if p["idade"] < 20:
            mulheres_menores_20 += 1

    print(f"{p["nome"]:<10} | {p["idade"]:<5} | {p["genero"]:<6}")

print(f"\n===== ANÁLISE DE DADOS =====\n"
      f"Média de idade: {media_idades:.1f}\n"
      f"Homem mais velho: {homem_mais_velho}.\n"
      f"Mulheres com menos de 20: {mulheres_menores_20}\n ")