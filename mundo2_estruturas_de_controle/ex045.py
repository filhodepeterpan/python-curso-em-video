# Pedra, Papel e Tesoura

from random import randint

while True:
    escolha_pc : int = randint(1,3)
    resultado: str = ""

    objeto_pc = "PEDRA" if escolha_pc == 1 else "PAPEL" if escolha_pc == 2 else "TESOURA"

    print("Vamos jogar Pedra, Papel ou Tesoura!Escolha uma opção:\n"
          "[ 1 ] Pedra\n"
          "[ 2 ] Papel\n"
          "[ 3 ] Tesoura\n")
    try:
        escolha_jogador = int(input("\nSua escolha: "))

        if 1 <= escolha_jogador <= 3:
            if escolha_pc == 1:
                resultado = "Você venceu!" if escolha_jogador == 2 else "Empatamos!" if escolha_jogador == 1 else "Eu ganhei!"
            if escolha_pc == 2:
                resultado = "Você venceu!" if escolha_jogador == 3 else "Empatamos!" if escolha_jogador == 2 else "Eu ganhei!"
            if escolha_pc == 3:
                resultado = "Você venceu!" if escolha_jogador == 1 else "Empatamos!" if escolha_jogador == 3 else "Eu ganhei!"

            print(f"Eu escolhi {objeto_pc}. {resultado}")
            break
        else:
            print("\nTentativa inválida. Escolha 1, 2 ou 3.\n")
    except ValueError:
        print("\nTentativa inválida. Escolha 1, 2 ou 3.\n")