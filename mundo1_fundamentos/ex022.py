# Analisador de Texto

nome = str(input("Digite seu nome completo: "))
nome = nome.strip()

print(f"""
    Nome com todas as letras maiúsculas: {nome.upper()}
    Nome com todas as letras minúsculas: {nome.lower()}
    Quantidade de letras (excetuando espaços): {len(nome) - nome.count(' ')}
    Quantidade de letras do primeiro nome: {len(nome.split()[0])}
""")