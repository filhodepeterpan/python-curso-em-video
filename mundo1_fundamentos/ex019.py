# Sorteando um item na lista
from random import choice

alunos: any = []

alunos.append(input("Primeiro aluno: "))
alunos.append(input("Segundo aluno: "))
alunos.append(input("Terceiro aluno: "))
alunos.append(input("Quarto aluno: "))

print(f"Alunos participantes: {', '.join(alunos)}\n"
      f"O aluno sorteado foi: {choice(alunos)}\n")