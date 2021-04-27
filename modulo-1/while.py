"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade : Estrutura de repetição
Descrição do Exercício 
Criar um programa com while;
"""
# cabeçalho do programa
print('-' * 60)
print(f'{"Número secreto":^60}')
print('-' * 60)

# recebe o número do usuário e solicita um novo número caso ele erre.
num_secreto = 10
print('\nAdivinhe qual é o número secreto!')
num = int(input('Digite um número de 0 a 10: '))
while num != num_secreto:
    num = int(input("Você errou, tente novamente, digite um número:  "))

# Informa ao usuário que ele acertou
print(f"Parabéns você acertou, o número secreto é {num_secreto}")