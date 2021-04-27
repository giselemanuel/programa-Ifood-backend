"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Desafio : Compras
Descrição do Exercício 2:
Criar um programa que:
1.Peça para a pessoa usuária inserir o nome de três produtos de mercado e seus respectivos preços;
Mostre na tela o produto mais barato.
"""
# cores
cores = { 
        'limpa' : '\033[m',
        'vermelho': '\033[31m',
        }

# cabeçalho do programa
print('*' * 35)
print(f'{"Compras":^35}')
print('*' * 35)

# declaração de variáveis e entrada de valores
print('{}Insira o primeiro produto{}'.format(cores['vermelho'], cores['limpa']))
produto1 = str(input('Digite o nome do produto: ')).strip().title()
preco1 = float(input('Digite o preço do produto: R$ '))
print('\n{}Insira o segundo produto{}'.format(cores['vermelho'], cores['limpa']))
produto2 = str(input('Digite o nome do  produto: ')).strip().title()
preco2 = float(input('Digite o preço do   produto: R$ '))
print('\n{}Insira o terceiro produto{}'.format(cores['vermelho'], cores['limpa']))
produto3 = str(input('Digite o nome do  produto: ')).strip().title()
preco3 = float(input('Digite o preço do  produto: R$  '))

# saída do programa exibir o produto mais barato
menor = preco1

if preco2 < preco1 and preco2 < preco3:
    menor = preco2
    print(f'\n\033[36m{produto2}\033[m custa \033[32mR$ {preco2:.2f}\033[m é o mais barato.')

elif preco3 < preco1 and preco3 < preco2:
    menor = preco3
    print(f'\n\033[36m{produto3}\033[m custa \033[32mR$ {preco3:.2f}\033[m é o mais barato.')

else:
    print(f'\n\033[36m{produto1}\033[m custa \033[32mR$ {preco1:.2f}\033[m é o mais barato.')

