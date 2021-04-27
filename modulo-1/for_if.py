"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade : Estrutura de repetição
Descrição do Exercício 
Criar um programa com for com if;
"""

# cabeçalho do programa
print('-' * 25)
print(f'{"Contando até 10":^25}')
print('-' * 25)

# exibindo a contagem de 1 até 10
for conta_num in range (1,11):
    if conta_num == 11:
        break
    print(conta_num, end=' ')
print("\nFim da contagem.")