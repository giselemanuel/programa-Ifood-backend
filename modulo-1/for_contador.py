"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade : estrutura de respetição
Descrição do Exercício 
Criar um programa com for com contador;
"""

# cabeçalho do programa
print('-' * 55)
print(f'{"Cadastro de convidados para uma festa":^55}')
print('-' * 55)


# solicita o número do convidada para a festa
contador = 1

num_convidados = int(input("Informe a quantidade de convidados que seja inserir: "))

# solicita o nome dos convidados para cadastro

for conta_convidados in range (0, num_convidados):
    nome = str(input(f"Digite o nome do {contador}º convidado: "))
    contador += 1

# informa final do programa
print(f"Cadastro concluído, os {num_convidados} convidados foram inseridos!")