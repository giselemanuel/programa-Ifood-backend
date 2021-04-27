# importa a biblioteca factorial existente em math
from math import factorial

# cabeçalho do programa
print('-' * 30)
print(f'{"Calcula Fatorial":^30}')
print('-' * 30)

# solicita o número ao usuário
num = int(input('Digite um número: '))

# calcula o fatorial do número inserido
fatorial = factorial(num)

# imprime o fatorial
print(f'O fatorial de {num} é {fatorial}.')
