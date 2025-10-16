# Verificando as primeiras letras de um texto

cidade = str(input("Digite o nome de uma cidade: "))
cidade = cidade.lower().strip().split()

comecaComSanto = cidade[0] == "santo"
resposta = "SIM" if comecaComSanto else "Não..."

print(f"Começa com Santo?: {resposta}")