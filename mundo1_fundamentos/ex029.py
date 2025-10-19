# Radar Eletrônico

velocidade_carro = float(input("Velocidade do carro em km/h: "))
velocidade_maxima_permitida : int = 80
multa_por_km : int = 7
total_multa : float = 0

if velocidade_carro > velocidade_maxima_permitida:
    total_multa = (velocidade_carro - velocidade_maxima_permitida) * multa_por_km
    print(f"O carro estava a {velocidade_carro}km/h e uma multa de R${total_multa:.2f} será cobrada.")

else:
    print(f"O limite de velocidade é {velocidade_maxima_permitida}km/h. Não há aplicação de multa.")