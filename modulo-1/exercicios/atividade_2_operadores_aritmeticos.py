"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade 1.3
Descrição do Execício 2:
Criar um programa que: Some : 1024 por 2048, Multiplique: 1024 por 2048, Divida  2048 por 1024,Subtraia  1024 por 2048, executar print dos operadores aritméticos.
"""

#Definição das variáveis
num1 = 1024
num2 = 2048
soma = num1 + num2
multiplica = num1 * num2
divide = num2 / num1
subtrai = num2 - num1

#Saída do programa
print('\n')
print('\033[32m') 
print('-' * 50)
print(f'{"Atividade 2 - Operadores Aritméticos":^50}')
print('-' * 50)
print('\033[m')
print(f'Operação de Soma de {num1} + {num2} = {soma}')
print(f'Operação de Multiplicação {num1} * {num2} = {multiplica}')
print(f'Operação de Divisão {num2} / {num1} = {divide}')
print(f'Operação de Subtração {num2} - {num1} = {subtrai}')
print('\033[32m')
print('-' * 50)
print('\033[m')