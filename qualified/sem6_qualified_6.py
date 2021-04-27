"""
Nesta atividade você terá que criar uma função que faz a contagem das letras de uma string utilizando um dicionário.

As chaves do dicionário devem ser as letras que existem na string e os valores serão as suas respectivas quantidades.

Instruções
Crie uma função com a seguinte assinatura conta_letras(string) que recebe uma string como parâmetro
Implemente uma lógica para fazer a contagem de cada letra da string recebida utilizando um dicionário, onde as chaves são as letras e os valores são a quantidade de vezes que aquela letra aparece na string.
A função deverá retornar o dicionário com a contagem das letras.
Se a string for vazia, deve-se retornar um dicionário vazio
Exemplos
Entrada: "abc"
Saída: {"a": 1, "b": 1, "c": 1}

Entrada: AaaBBb
Saída: {"A": 1, "a": 2, "B": 2, "b": 1}

Entrada: ""
Saída: {}
"""

def conta_letras(string):
    dicionario = {}
    # retorna dicionário vazio se a lista  = 0
    if len(string) == 0:
      return dicionario
    # cria dicionário com a contagem das letras
    else:
      for d in string:
        dicionario[d] = string.count(d)
        return dicionario
      
letra = "abc"
conta_letras(letra)