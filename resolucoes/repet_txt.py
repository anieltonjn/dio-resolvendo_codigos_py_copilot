# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Solicitar a string e o número inteiro como entrada
string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

print(' '.join([string] * numero))