'''
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade 1.7
Descrição do Exercício 2:
Crie um programa com  uma função que calcule se o resultado do exame do paciente está "bom", "médio" ou "ruim". 
O algoritmo deve conter, pelo menos, três pacientes (um em cada situação). 
Considere os parâmetros: 
Bom : Entre 7 e 10
Médio: Entre 4 e 6
Ruim: Entre 0 e 3
Dependendo do Resultado você deve aconselhar
Bom : Continuar assim
Médio: Buscar se cuidar mais e fazer acompanhamento médico
Ruim: Procurar a equipe médica
'''
# cabeçalho do programa
print('\n')
print('-'  * 100)
print(f'{"Resultado de Exame Médico":^100}')
print('-'  * 100)

# função que calcula resultado do exame médico do paciente  
def resultado_exame(resultado):

    if (resultado >= 7) and (resultado <= 10):
        print('o seu resultado esta bom, continue assim.')
    elif (resultado >= 4) and (resultado <= 6):
        print('o seu resultado esta na média, busque se cuidar e fazer um acompanhamento médico.')
    elif (resultado >= 0) and (resultado <= 3):
        print('o seu resultado esta ruim, procure uma equipe médica.')

for paciente in range (0,3): # loop executará o código dentro do bloco por 3 vezes.
    
    print(f'\033[32m{paciente + 1}º Paciente\033[m')
    nome = input('Informe o seu nome : ')
    exame = int(input('Informe o resultado do seu exame: '))
    print('Olá \033[36m{}\033[m, '.format(nome.strip().title()), end='')
    #strip() vai remover os espaços  inseridos no inicio ou final do input da variável nome
    #title() vai capitalizar a variável nome deixando a primeira letra maiúscula e o resto minuscúla.
    resultado_exame(exame)
    print('-' * 100)
