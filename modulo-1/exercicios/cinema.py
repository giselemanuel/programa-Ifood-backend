"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Desafio : cinema
Descrição do Exercício 1:
Criar um programa que:
1.Pergunte a pessoa usuária:
o nome, a idade e se ela é estudante de Python;
2.Permita apenas pessoas usuárias maiores de 18 anos reservarem um ingresso para um clube de festas;
3.Permita a pessoa usuária escolher entre a entrada padrão, que custa R$ 35,00 e a VIP, que custa R$ 60,00;
Conceda um desconto de 50% aos estudantes de Python;
 Se houver menores de idade, imprima quantos anos faltam para a pessoa usuária ter 18 anos e, consequentemente, ter acesso ao clube. 
"""
# cores
cores = { 
        'limpa' : '\033[m',
        'vermelho': '\033[31m',
        'azul_claro': '\033[36m'
        }

# cabeçalho do programa
print('*' * 35)
print(f'{"Cinema Clube Festa ":^35}')
print('*' * 35)

# declaração de variáveis entrada de valores
nome  = str(input('Digite seu nome: ')).strip().title()
idade = int(input('Digite a sua idade: '))
estudante = str(input('Você é estudante de Python [S/N]: ')).strip().upper()
print()
ingresso = int(input('{}Ingressos p/ Clube de Festa{}\n[1] PADRÃO.......R$ 35,00\n[2] VIP..........R$ 60,00\nInforme a opção: '.format(cores['azul_claro'], cores['limpa'])))
anos = 0
ing_padrao = 35
ing_vip = 60

# Condição para compra de ingressos para o cinema
if idade >= 18 and estudante == 'S':
    if ingresso == 1:
        ing_padrao /= 2
        print("\nOlá {}Pythonista{},\nvocê ganhou 50% de desconto !!!\nO Seu ingresso ficou {}R$ {:.2f}{}.".format(cores['azul_claro'], cores['limpa'], cores['vermelho'], ing_padrao, cores['limpa']))

    elif ingresso == 2:
        ing_vip /= 2
        print("\nOlá {}Pythonista{},\nvocê ganhou 50% de desconto !!!\nO Seu ingresso ficou {}R$ {:.2f}{}.".format(cores['azul_claro'], cores['limpa'], cores['vermelho'], ing_vip, cores['limpa']))
        
elif idade >= 18 and estudante == 'N':
    if ingresso == 1:
        print("\nOlá {},\nO seu ingresso ficou R$ {}{:.2f}{}.".format(nome, cores['vermelho'], ing_padrao, cores['limpa']))

    elif ingresso == 2:
        print("\nOlá {},\nO seu ingresso ficou R$ {}{:.2f}{}.".format(nome, cores['vermelho'], ing_vip, cores['limpa']))
else:
    anos = 18 - idade
    print("\n{}{}{}, você não pode comprar ingressos ainda! Falta {} anos para você ter acesso ao Clube Festa.".format(cores['azul_claro'], nome, cores['limpa'], anos))