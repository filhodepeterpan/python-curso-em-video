# Primeira e última ocorrência de uma string

frase = str(input("Digite uma frase: "))
frase = frase.lower().strip()

print(f"""
    Quantidade de letras 'A': {frase.count('a')}
    Primeira posição que a letra 'A' aparece: {frase.find('a')}
    Última posição que a letra 'A' aparece: {frase.rfind('a')}
""")