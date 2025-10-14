# Calculando descontos

porcentagemDesconto = 5

precoProduto = float(input("Qual o preço do produto? R$ "))

print(f"O produto que custava R$ {precoProduto}, na promoção com desconto de {porcentagemDesconto}% vai custar R$ {precoProduto * (1 - (porcentagemDesconto/100)):.2f}")