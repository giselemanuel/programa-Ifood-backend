"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Desafio : Vidente
Descrição do Exercício 1:
Criar um programa que:

1. Pergute pelo nome do usuário o armazena em uma variável.
2. Pegunte pelo número de filhos que o usuário deseja ter e o armazena em uma variável.
3. Pergunte a cidade na qual o usuário gostaria demorar e a armazena em uma variável.
4. Pergunte a profissão dos sonhos do usuário e a armazena em uma variável.
5. Exibe na tela o seguinte texto inserindo os campos com as variáveis.
'A Vidente prevê: <nome> terá <filho> e viverá em <cidade> trabalhando como <profissão> em 2023.'
"""

#Cores
cores = { 'limpa': '\033[m',
          'azul': '\033[34m',
          'azul_claro': '\033[36m',
          'verde': '\033[32m'
        }

# Cabeçalho do programa
print('\n')
print('-' * 60)
print(f'{"PROGRAMA DA VIDENTE - VOU CONTAR SOBRE SEU FUTURO ! ":^60}')
print('-' * 60)

# Variáveis e entrada de valores
nome = str(input('{}Digite seu nome: {}'.format(cores['azul_claro'], cores['limpa'])))
qtd_filhos = int(input('{}Quantos filhos deseja ter: {}'.format(cores['azul_claro'], cores['limpa'])))
cidade = str(input('{}Em qual cidade gostaria de morar: {}'.format(cores['azul_claro'], cores['limpa'])))
profissão = str(input('{}Qual a sua profissão dos sonhos:{}'.format(cores['azul_claro'], cores['limpa'])))

#Saída do programa
print(cores['verde'], f'\nA vidente prevê: {nome} terá {qtd_filhos} filhos e viverá em {cidade} trabalhando como {profissão} em 2021.', cores['limpa'])

