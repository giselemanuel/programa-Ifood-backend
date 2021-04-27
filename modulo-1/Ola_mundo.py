"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade : ola_mundo_parte2
Descrição do Exercício 
Criar um programa que:
	Pergunte ao usuário seu nome; 
	Pergunte ao usuário sua idade; 
	Retorna ao usuário o seguinte texto: Olá (nome), como você tem (idade) anos, eu calculo que você já tenha vivido mais de (dias de vida)! 
Leve em consideração que cada ano possui 365 dias;  
"""
# Cores
cores ={'limpa' : '\033[m',
        'azul' : '\033[34m',
        'verde': '\033[32m'
        }

# Cabeçalho do programa
print('\n')
print('-' * 70)
print(f'{"PROGRAMA OLÁ MUNDO":^70}')
print('-' * 70)

# Variáveis
nome = str(input('{}Digite seu nome: {}'.format(cores['verde'], cores['limpa'])))
idade = int(input('{}Digite sua idade: {}'.format(cores['verde'], cores['limpa'])))
total_dias = idade * 365

# Saída do programa
print(cores['azul'],f'Olá {nome}, como você tem {idade} anos, eu calculo que você já tenha vivido mais de {total_dias} dias', cores['limpa'])