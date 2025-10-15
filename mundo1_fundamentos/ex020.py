# Sorteando uma ordem na lista

from random import shuffle

alunos: any = []

alunos.append(input("Primeiro aluno: "))
alunos.append(input("Segundo aluno: "))
alunos.append(input("Terceiro aluno: "))
alunos.append(input("Quarto aluno: "))

shuffle(alunos)

print(f"A ordem de apresentação dos alunos será: {', '.join((alunos))}")