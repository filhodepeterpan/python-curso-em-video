# Primeiro e último nome de uma pessoa

nomeCompleto = str(input("Digite um nome completo: "))
nomeCompleto = nomeCompleto.strip().split()

primeiroNome = nomeCompleto[0]
ultimoNome = nomeCompleto[len(nomeCompleto) - 1]

print(f"""
    Primeiro nome: {primeiroNome}
    Último nome: {ultimoNome}
""")