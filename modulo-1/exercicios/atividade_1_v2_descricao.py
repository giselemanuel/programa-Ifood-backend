"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade 1.3
Descrição do Exercício 1:
Criar um programa que tenha os itens abaixo e preencha os valores das variáveis com seus dados. 
Executar Print dos dados.
Tenha uma variável referente ao NOME
Tenha uma variável referente ao ANIMAL DE ESTIMAÇÃO
Tenha uma variável referente ao COMIDA FAVORITA
Tenha uma variável referente ao PAÎS QUE QUER VISITAR
Tenha uma variável referente ao IDADE
Tenha uma variável referente ao ALTURA
"""

# Defiinição das variáveis

nome = input(str('Digite seu nome: '))
idade = input(int('Digite sua idade: '))
altura = input(float('Digite sua altura: '))
animal_de_estimacao = input(str('Digite qual é o seu animal de estimação: '))
comida_favorita = input(str('Digite qual a sua comida predileta: '))
pais_visitar = input(str('Digite o pais deseja visitar:'))

# Saída do programa
print('\n')
print('\033[32m')
print('-' * 60)
print(f'{"Atividade 1 - Descrição Pessoal":^60}')
print('-' * 60)
print('\033[m')
print(f'Nome: \033[32m{nome}\033[m')
print(f'Idade: \033[32m{idade}\033[m anos')
print(f'Animal de estimação: \033[32m{animal_de_estimacao}\033[m')
print(f'Comida Favorita: \033[32m{comida_favorita}\033[m')
print(f'País que deseja visitar: \033[32m{pais_visitar}\033[m')
print('\033[32m')
print('-' * 60)
print('\033[m')


