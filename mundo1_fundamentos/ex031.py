# Custo da Viagem

distancia = float(input("Digite a distância de viagem em km: "))
valor_passagem : float = 0

if distancia <= 200:
    valor_passagem = distancia * 0.50
else:
    valor_passagem = distancia * 0.45

print(f"Valor total da passagem: R${valor_passagem:.2f}")