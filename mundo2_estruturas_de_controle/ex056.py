# Analisador completo

# ENUNCIADO: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

qt_pessoas : int = 4
dados : list = []

for i in range (0, qt_pessoas):

    print(f"\n ===== {i + 1}ª PESSOA =====\n")

    nome = str(input(f"Nome: ")).strip().capitalize()
    idade = int(input(f"Idade: "))
    sexo = str(input(f"Sexo: ")).strip().upper()[0]

    print("\n")

    dados.append({
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
    })

media_idades : float = sum(p["idade"] for p in dados) / qt_pessoas
mulheres_menores_20 : int = 0
homem_mais_velho : str = ""
idade_homem_mais_velho : int = 0

for p in dados:
    if p ["sexo"] == "M":
        if p["idade"] > idade_homem_mais_velho:
            idade_homem_mais_velho = p["idade"]
            homem_mais_velho = p["nome"]

    if p["sexo"] == "F":
        if p["idade"] < 20:
            mulheres_menores_20 += 1

print(f"\nMédia de idade: {media_idades:.1f}.\n"
      f"Homem mais velho: {homem_mais_velho}\n"
      f"Mulheres com menos de 20: {mulheres_menores_20}\n ")