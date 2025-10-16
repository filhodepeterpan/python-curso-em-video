# Verificando as primeiras letras de um texto

cidade = str(input("Digite o nome de uma cidade: "))
cidade = cidade.lower().strip()

comecaComSanto : bool = cidade[:5] == "santo"
resposta = "SIM" if comecaComSanto else "Não..."

print(f"Começa com Santo?: {resposta}")