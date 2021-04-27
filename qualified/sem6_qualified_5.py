"""
Nesta atividade você terá que transformar duas listas em um único dicionário, onde os elementos da primeira lista serão as chaves e os elementos da segunda lista serão os valores.

A combinação deve ser feita respeitando a posição dos valores das listas.

Se as listas tiverem tamanhos diferentes a função deve retornar um dicionário vazio {}

Instruções
Crie uma função chamada listas_para_dicionario que recebe duas listas como parâmetros
Implemente uma lógica dentro da função para transformar as listas recebidas em um único dicionário, onde os pares de chave e valor devem respeitar a posição dos elementos da lista
O retorno da função deve ser um dicionário como especificado no passo 2
Se a listas forem vazias, a função deve retornar um dicionário vazio
Se as listas tiverem tamanhos diferentes, a função deve retornar um dicionário vazio
Exemplos
Entrada: ["a", "b", "c"], [1, 2, 3]
Saída: {"a": 1, "b": 2, "c": 3}

Entrada: [0, 10, 15], ["z", "X", "K"]
Saída: {0: "z", 10: "X", 15: "K"}

Entrada: ["a", "a", "b"], [1, 2, 3]
Saída: {"a": "2", "b": "3"}

Entrada: ["a", "a", "a"], [1, 2, 3]
Saída: {"a": 3}

Entrada: [], []
Saída: {}

Entrada: [1, 2], ["a"]
Saída: {}
"""

def listas_para_dicionario(lista1, lista2):
  
  dicionario = {}
  # retorna dicionario vazio se as len() for diferente
  if len(lista1) != len(lista2):
    return dicionario
  else:
    # concatena as duas listas em um dicionario
    for d in range (len(lista1)):
      dicionario[lista1[d]] = lista2[d]
    return dicionario
  
lista_l = ["a", "b", "c"]
lista_num = [1, 2, 3]
listas_para_dicionario(lista_l, lista_num)
  
  