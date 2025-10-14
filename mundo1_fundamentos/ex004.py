# Dissecando uma variável

variavel = input("Digite qualquer coisa para dissecarmos o conteúdo: ")

print(f"O tipo primitivo desse valor é: {type(variavel)}")
print(f"Só tem espaços? {variavel.isspace()}")
print(f"É numérico? {variavel.isnumeric()}")
print(f"É alfabético? {variavel.isalpha()}")
print(f"É alfanumérico? {variavel.isalnum()}")
print(f"Está em maiúsculas? {variavel.isupper()}")
print(f"Está em minúsculas? {variavel.islower()}")
print(f"Está capitalizado? {variavel.istitle()}")