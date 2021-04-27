"""
Programa VamoAI: Aluna: Gisele Rodrigues Manuel
Exercício Temperatura: você deverá criar um programa que auxiliará um médico gringo que diz com base na temperatura da pessoa usuária 
se ela está com febre ou não. 
1. Pergunte a pessoa usuária qual a temperatura dela e guarde o valor na variável temperatura; 
2. Utilize if com operador de maior que (>) para verificar se a pessoa usuária está com febre (mais de 37);
3. Caso esteja com febre, exiba: 
“Sinto muito, você está com febre, melhor tomar um antitérmico”. 
Caso contrário, exiba: “Você não está com febre, volte para casa!”; 
"""
# cores
cores = { 'limpa': '\033[m',
          'vermelho': '\033[31m',
          'verde': '\033[32m',
          'azul_claro': '\033[36m'
        }

# cabeçalho do programa 
print('-' * 60)
print(f'{"PROGRAMA TEMPERATURA":^60}')
print('-' * 60)

# variáveis e entrada de dados
nome = str(input('{}Olá sou Dra. Rodrigues, informe seu nome: {}'.format(cores['azul_claro'], cores['limpa'])))
temperatura = float(input('{}Por favor, informe a sua temperatura corporal: {}'.format(cores['azul_claro'], cores['limpa'])))

# Condição de saída do programa
if temperatura > 37:
    print('{}Olá {},sinto muito, você está com febre, melhor tomar um antitérmico!{}'.format(cores['vermelho'], nome, cores['limpa']))
else:
    print('{}Olá {},você não está com febre, volte para casa!{}'.format(cores['verde'], nome, cores['limpa']))