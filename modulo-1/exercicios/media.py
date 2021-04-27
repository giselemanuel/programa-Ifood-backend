"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade 1.7
Descrição do Exercício 1:
Faça um programa que contenha uma função que calcule a média de cinco alunos 
(as notas de cada aluno deverão ser distintas);
"""

# cabeçalho do programa
print('\n')
print('-'  * 45)
print(f'{"CALCULA MÉDIA DAS NOTAS DA TURMA":^45}')
print('-'  * 45)

# função que calcula a média de notas de 5 alunos de uma turma
def media(nota1, nota2, nota3, nota4, nota5):
    media = (nota1 + nota2 + nota3 + nota4 + nota5)/5
    print('-'  * 45)
    print(f'A média da turma foi é {media:.2f}\n')

# Variáveis globais e entrada de valores
aluno1 = float(input('Insira a nota do primeiro aluno:  '))
aluno2 = float(input('Insira a nota do segundo aluno:  '))
aluno3 = float(input('Insira a nota do terceiro aluno:  '))
aluno4 = float(input('Insira a nota do quarto aluno:  '))
aluno5 = float(input('Insira a nota do quinto aluno:  '))

# Chamada da função para calcular média
media(aluno1, aluno2, aluno3, aluno4, aluno5)