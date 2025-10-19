# Maior e menor número

entrada = input("Digite vários números separados por vírgula. Ex: 1,2,3: ")
entrada = entrada.strip().split(",")
numeros = [int(numero) for numero in entrada]

print(f"Números digitados: {','.join(entrada)}\n"
      f"Maior número: {max(numeros)}\n"
      f"Menor número: {min(numeros)}")

