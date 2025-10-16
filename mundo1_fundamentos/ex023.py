# Separando dígitos de um número

numero = str(input("Digite um número inteiro de 4 dígitos: "))

print(f"""
    Milhares: {numero[0]}
    Centenas: {numero[1]}
    Dezenas: {numero[2]}
    Unidades: {numero[3]}
""")