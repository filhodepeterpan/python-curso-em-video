# Procurando uma string dentro de outra

nome = str(input("Digite seu nome completo: "))
nome = nome.lower().strip()

temSilva : bool = "silva" in nome
resposta = "SIM" if temSilva else "Não..."

print(f"Tem Silva no nome? {resposta}")