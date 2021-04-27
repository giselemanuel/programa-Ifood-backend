"""
Descrição
Crie uma função chamada complete_series que recebe uma lista de números inteiros não negativos como parâmetro e retorna uma nova lista com a sequência completa dos números.

Dica: As sequências devem sempre começar em 0 e terminar com o maior valor da lista.

Se os números da sequência não estiverem em ordem, você deverá ordená-los, mas se houver valores repetidos, você terá que retornar somente o valor zero no array.

Exemplos
Entrada: [2,1]
Saída: [0,1,2]

Entrada: [1,4,4,6]
Saída: [0]
Lembre-se: todos os números são inteiros positivos.

Esse é um exemplo das saídas esperadas para uma certa sequência de entrada:

entradas        saídas
[0,1]   ->    [0,1]
[1,4,6] ->    [0,1,2,3,4,5,6]
[3,4,5] ->    [0,1,2,3,4,5]
[0,1,0] ->    [0]

"""

def complete_series(seq): 
    maior = seq[0]
    nova_lista = []
    lista_dup = []

    # remove duplicado e cria uma nova lista            
    for dup in seq:
      if dup not in lista_dup:
         lista_dup.append(dup)

    # se o tamanho da lista original for diferente da lista nova criada tem item duplicado imprime lista [0] 
    if len(seq) != len(lista_dup):
      lista_dup.clear()
      lista_dup.append(0)
      nova_lista = lista_dup
      return  nova_lista
          
     # verifica se o tamanho da lista original é igual o da lista nova
    elif len(seq) == len(lista_dup):
      # verificar o maior número da lista
      for num in seq:
        if num > maior:
          maior = num
      # cria nova lista de 0 até o maior número
      for num in range (0, maior+1):
          nova_lista.append(num)
        # imprime a nova lista
          #print(nova_lista)
        
      return nova_lista
        
lista = [1,4,4,6]
complete_series(lista)