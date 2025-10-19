# Ano Bissexto

ano = int(input("Digite um ano: "))
anoCentenario: bool = ano % 100 == 0
anoBissexto: bool = False

if anoCentenario and ano % 400 == 0:
    anoBissexto = True
elif not anoCentenario and ano % 4 == 0:
    anoBissexto = True

print(f"O ano {ano} é {'bissexto' if anoBissexto else 'comum'}.")
