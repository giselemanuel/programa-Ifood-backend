"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade 1.8
Descrição do Exercício 1:
Você deverá utilizar o enunciado abaixo como base para desenvolver algoritmos 
que utilizem todos os conceitos abordados no exercício anterior. 
Uma professora deseja desenvolver um sistema para automatizar
seu trabalho. Ela precisa criar uma solução onde seus alunos consigam:
1. Inserir suas notas (seja a média geral de todas as
matérias ou a média de uma única disciplina)
2. receber a média, 
3. saber sua situação (aprovação, reprovação ou recuperação).

Utilizar os tópicos vistos : 
Computação, Print, Variáves e seus tipos , Operadores lógicos, Casting, Entrada de dados, Algoritimos, 
Pensamento Computacional, Condicionais, Bloco de Códigos,Operadores Lógicos, Funções.
Aluna: Gisele Manunel
"""

# cabeçalho do programa
print('\n')
print('-' * 50)
print(f'{"CALCULA MÉDIA DO CURSO DE PYTHON":^50}')
print('-' * 50)

# função que calcula a média de uma matéria de um aluno


def calcula_media():

    nome = str(input('Digite o nome: ')).strip().title()
    nota1_aluno = float(input('Insira a nota da primeira prova de Python: '))
    nota2_aluno = float(input('Insira a nota da segunda prova de Python: '))
    nota3_aluno = float(input('Insira a nota da terceira prova de Python: '))
    media = (nota1_aluno + nota2_aluno + nota3_aluno) / 3
    return media, nome

# função que verifica se pela média final o aluno foi aprovado


def valida_aprovacao(media, nome):

    if 6 <= media <= 10:
        print()
        print(f'{nome}, você está aprovado(a)!')
        print(f'Sua média em Python foi {media:.2f}')
    elif 5 <= media < 6:
        print()
        print(f'{nome}, você está de recuparação!')
        print(f'Sua média em Python foi {media:.2f}')
    else:
        print()
        print(f'{nome}, você está reprovado(a)!')
        print(f'Média final em Python foi {media:.2f}')

# função que verifica se deseja inserir um novo cadastro


def cadastro_aluno():
    print('--')
    cadastro = str(input('Deseja inserir outro aluno [S/N]: ')).strip().upper()
    if cadastro == 'S':
        print('--')
        media, nome = calcula_media()
        valida_aprovacao(media, nome)
    else:
        fim_programa()

#  função que encerra o programa


def fim_programa():
    print('--\n')
    print('Programa encerrado!')
    quit()


media, nome = calcula_media()
valida_aprovacao(media, nome)
# Considerando que a turma possui 6 alunos o programa será executado 5 vezes caso o usuário não solicite encerra-lo.
cadastro_aluno()
cadastro_aluno()
cadastro_aluno()
cadastro_aluno()
cadastro_aluno()
fim_programa()
