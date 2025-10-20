# Alistamento Militar

while True:

    try:
        idade = int(input("Digite sua idade: "))
        idade_minima = 18
        alistamento_possivel: bool = idade >= idade_minima

        if alistamento_possivel:

            if idade == idade_minima:
                print("\nVocê está no momento certo para se alistar. Vá até a Junta de Serviço Militar mais próxima.")
            else:
                anos_atraso = idade - idade_minima
                print(f"\nVocê já está {anos_atraso} {'ano' if anos_atraso == 1 else 'anos'} atrasado para se alistar. Corra até a Junta de Serviço militar mais próxima.")
        else:
            print(f"\nVocê ainda precisa esperar {idade_minima - idade} anos para se alistar.")

        break
    except ValueError:
        print("\nDigite apenas números inteiros.")