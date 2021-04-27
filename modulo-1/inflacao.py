"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade : Inflação
Descrição do Exercício 
Criar um programa que:
Pergunte ao usuário qual foi o preço KG do tomate 1 ano atrás e guarde em uma variável; 
Pergunte ao usuário qual o preço do KG do tomate hoje e guarde em outra variável;
Exibe na tela o texto: “A diferença de preço do KG do tomate em um ano é de: (diferença)”; 
Exibe na tela o texto: “A inflação do KG do tomate em um ano é de (inflação)%”;. 

"""
# Cores
cores ={'limpa' : '\033[m',
        'vermelho' : '\033[31m',
        'verde': '\033[32m'
        }

# Cabeçalho do programa
print('\n')
print('-' * 70)
print(f'{"PROGRAMA INFLAÇÃ0":^70}')
print('-' * 70)

# Variáveis e entrada de valores
valor_anterior = float(input('{}Digite o valor do Kg do tomate 1 ano atrás. R$ {}'.format(cores['verde'],cores['limpa'])))
valor_atual = float(input('{}Digite o valor do Kg do tomate atualmente.  R$ {}'.format(cores['verde'],cores['limpa'])))
diferenca = valor_atual - valor_anterior
inflacao = (diferenca * 100) / valor_anterior

# Saída do programa
print('\nA diferença de preço do Kg do tomate de um ano é de {}R$ {:.2f}{} reais'.format(cores['vermelho'], diferenca, cores['limpa']))
print('A inflação do Kg do tomate em um ano é de {}{:.2f} %{}'.format(cores['vermelho'], inflacao, cores['limpa']))