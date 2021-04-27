"""

Descrição
Nesta atividade você terá que transformar uma lista em um dicionário. As chaves e valores serão iguais para cada elemento da lista.

Instruções
Crie uma função chamada lista_para_dicionario que recebe uma lista como parâmetro
Implemente uma lógica dentro da função para transformar a lista recebida em um dicionário, onde seus pares de chaves e valores são iguais
O retorno da função deve ser um dicionário como especificado no passo 2
Se a lista for vazia, a função deve retornar um dicionário vazio
Exemplos
Entrada: [1, 2, 3, 4, 5]
Saída: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

Entrada: ["a", "b", "c"]
Saída: {"a": "a", "b": "b", "c": "c"}

Entrada: ["a", "a", "b"]
Saída: {"a": "a", "b": "b"}

Entrada: ["a", "a", "a"]
Saída: {"a": "a"}

Entrada: []
Saída: {}

"""

def lista_para_dicionario(lista):
  dicionario = {}
  # valida se a lista esta vázia
  if len(lista) == 0:
      return dicionario
  # cria dicionário
  for d in range (0, len(lista)):
      dicionario[lista[d]] = lista[d]
  return dicionario

lista_n = [1, 2, 3, 4, 5]
lista_para_dicionario(lista_n)