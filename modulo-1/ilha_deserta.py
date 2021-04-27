"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Desafio : Ilha Deserta
Descrição do Exercício 2:
Criar um programa que:
1. Pergunte ao usuário quais os três itens ele levaria para uma ilha deserta.
2. Armazene cada um dos itens em uma variável diferente.
3. Exiba na tela o seguinte texto, inserindo nos campos com <variável> correspondente:
"Você levaria para uma ilha deserta: <item 1>, <item 2>, <item 3>."
"""

#Cores
cores = { 'limpa': '\033[m',
          'verde': '\033[32m',
          'azul' : '\033[34m',
          'azul_claro': '\033[36m',
        }

#Cabeçalho do progama
print('\n')
print('-'  * 75)
print(f'{"PROGRAMA ILHA DESERTA - O QUE VOCÊ LEVARIA PARA UMA ILHA DESERTA ?":^75}')
print('-'  * 75)

# Variáveis e entrada de valores
item1 = str(input('{}Digite o primeiro item que você levaria para uma ilha deserta: {}'.format(cores['azul_claro'], cores['limpa'])))
item2 = str(input('{}Digite o segundo item que você levaria para uma ilha deserta: {}'.format(cores['azul_claro'], cores['limpa'])))
item3 = str(input('{}Digite o terceiro item que você levaria para uma ilha deserta: {}'.format(cores['azul_claro'], cores['limpa'])))

# Saída do programa
print(cores['verde'],f'\nVocê levaria para uma ilha deserta: {item1}, {item2}, {item3}.', cores['limpa'])