# Aprovando empréstimo

valor_casa = float(input("Digite o valor da casa: R$ "))
salario_comprador = float(input("Digite o salário do comprador: R$ "))
anos_financiamento = int(input("Quantos anos de financiamento? "))
emprestimo_liberado: bool = False

prestacao_mensal : float = valor_casa / (anos_financiamento * 12)

if prestacao_mensal <= (salario_comprador * 0.30):
    emprestimo_liberado = True

print(f"Para pagar uma casa no valor de R$ {valor_casa:.2f} em {anos_financiamento} anos de financiamento, a prestação mensal será de R$ {prestacao_mensal:.2f}.\n"
      f"Portanto, seu empréstimo foi {'APROVADO' if emprestimo_liberado else 'NEGADO'}.")