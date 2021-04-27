"""
Crie uma fila comentando o que cada linha dentro dela está fazendo 
Aluna: Gisele Rodrigues Manuel
"""

# Cabeçalho do programa/ imprime o título
print('\n')
print('-' * 50)
print(f'{"Adicionando itens em uma lista de compras":^50}')
print('-' * 50)

# função para criação de uma lista de compras com 3 itens
def lista_compras(lista):
    print('Inclua três itens na lista de compras.')
    print('-')
    for l in range (1,4):
        l = input(f'Digite o {l}º item da lista de compra: ')
        lista.append(l)
    print('-')
    print(f'Sua lista de compra é :\n{lista}\n')

# função que removerá o primeiro item da lista caso o usuário desejar.
    while True:
        print('-')
        op = str(input(f'Deseja remover {lista[0]}  da lista de compras [S/N]: ')).upper()
        if op == "S": # remove o primeiro item caso o usuário responda sim
            item_removido = lista.pop(0)
            print(f'\nO {item_removido} foi removido(a) da lista.')
            print(f'Sua lista agora é: {lista}')
            break
        else: #  exibe os itens adicionados caso o usuário responda não.
            print('Lista de compra concluída.')
            print(lista)
            break

# declaração da fila
queue = []
# chama função e passa a fila declarada por parâmetro
lista_compras(queue)


