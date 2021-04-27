'''
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade 1.7
Descrição do Exercício 3:
Crie um algoritmo que multiplique dois valores aleatórios entre 1 e 50. 
Você deverá usar condicionais e funções nesse processo. 
'''
# cabeçalho do programa
print('\n')
print('-'  * 45)
print(f'{"Multiplica":^45}')
print('-'  * 45)

# função de multiplicação de números
def multiplica(num1, num2):
    multiplica = (num1 * num2)
    print(f'O resultado de {num1} * {num2} = {multiplica}')

# entrada de valores
print('Digite um número entre 1 e 50')
numero1 = int(input('Digite o primeiro número: ')) 
numero2 = int(input('Digite o segundo número: '))

# valida condição de entrada dos números de 1 a 50 só sai quando usuário inserir o número dentro desta faixa.
while True:
    print('--')
    if (numero1 < 1) or (numero1 > 50):
        print('\033[31mPrimeiro número inserido inválido!\033[m')
        numero1 = int(input('Digite o primeiro número entre 1 a 50: '))
    elif(numero2 < 1) or (numero2 > 50):
        print('\033[31mSegundo número inserido inválido!\033[m')
        numero2 = int(input('Digite o segundo número entre 1 a 50: '))
    else:
        break

# chama a função multiplica realiza multiplicação dos números recebidos.
multiplica(numero1, numero2)