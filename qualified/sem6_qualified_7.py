"""
Nesta atividade você terá que ordenar um dicionário a partir dos seus valores.

Instruções
Crie uma função chamada ordena_dicionario que recebe um dicionário como parâmetro
Implemente uma lógica dentro da função para ordenar o dicionário pelos seus valores, ao final, retorne este dicionário
Se o dicionário for vazio, a função deve retornar um dicionário vazio
Dica: Você pode tanto criar um novo dicionário ordenado quanto ordenar no próprio dicionário original.

Os valores devem ser numéricos
As chaves podem ter qualquer valor, não são importantes para a solução
Dê preferência para uma solução utilizando uma estrutura de repetição
Exemplos
Entrada: {"a": 2, "b": 3, "c": 1}
Saída: {"c": 1, "a": 2, "b": 3}

Entrada: {0: 10, 3: 5, "c": 1}
Saída: {"c": 1, 3: 5, 0: 10}

Entrada: {}
Saída: {}
"""

# importa a biblioteca para utilizar a funçao itemgetter
from operator import itemgetter

def ordena_dicionario(dicionario):
  ordenado = {}
  # retorna 0 se o dicionario estiver vazio
  if len(dicionario) == 0:
      return ordenado
  else:
    # ordena o dicionário pelos valores
    ordenado = dict(sorted(dicionario.items(), key=itemgetter(1)))
    return ordenado
     
dicionario_n = {"a": 2, "b": 3, "c": 1}
ordena_dicionario(dicionario_n)
