# Validação de Dados

generos_validos : list[str] = ['M', 'F', 'NB']

genero : str = ""

while genero not in generos_validos:
    genero = str(input("Digite seu gênero [M/F/NB]: ")).upper().strip()

print(f"\nVocê definiu seu gênero como {genero}.")