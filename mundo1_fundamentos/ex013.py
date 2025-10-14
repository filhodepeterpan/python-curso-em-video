# Reajuste Salarial

salario = float(input("Qual é o salário do funcionário? R$ "))

porcentagemReajuste: float = 15
salarioReajustado = salario + (salario * (porcentagemReajuste/100))

print(f"Um funcionário que ganhava R$ {salario:.2f}, com {porcentagemReajuste}% de aumento, passa a receber R$ {salarioReajustado:.2f}.")