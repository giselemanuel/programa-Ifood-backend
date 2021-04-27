"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Desafio : Animal
Descrição do Exercício 3:
Criar um programa que:
1. Pergunte ao usuário qual aninal ele gostaria de ser e armazene em uma variável.
2. Exiba na tela o texto: "Num primeiro momento , eu gostaria de ser o <animal>
3. Pergunte ao usuário qual animal ele gostaria de ser no lugar desse e armazene esse novo animal na mesma variável.
4. Exibe na tela o seguinte texto: " Pensando melhor , eu gostaria mesmo de ser um <animal>
"""

# Cores
cores = { 'limpa': '\033[m',
          'vermelho': '\033[31m',
          'verde': '\033[32m',
        }

# Cabeçalho do programa
print('\n')
print('-' * 60)
print(f'{"PROGRAMA ANIMAL - QUAL ANIMAL VOCÊ SERIA?":^60}')
print('-' * 60)

# Variável e entradas de valores
animal = str(input('{}1. Se você pudesse ser um animal, qual animal seria? {}'.format(cores['verde'], cores['limpa'])))
print('Num primeiro momento, eu gostaria de ser um(a) {}{}{}.\n'.format(cores['vermelho'], animal, cores['limpa']))
animal = str(input('{}2. Qual outro animal você gostaria de ser? {}'.format(cores['verde'], cores['limpa'])))
print('Pensando melhor, eu gostaria mesmo de ser um(a) {}{}{}\n'.format(cores['vermelho'], animal, cores['limpa']))
