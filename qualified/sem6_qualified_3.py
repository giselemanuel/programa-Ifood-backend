"""
Descrição
Nesta atividade você terá que criar uma função que soma todos os valores de um dicionário e retorna esta soma.

Os valores devem ser numéricos.

Se o dicionário estiver vazio, o valor retornado pela função deve ser 0.

Instruções
Crie uma função com a seguinte assinatura soma_valores(dicionario) que recebe um dicionário como parâmetro
Implemente uma lógica para somar os valores do dicionário recebido e retornar a soma
Se o dicionário estiver vazio, o retorno deve ser 0
Exemplos
Entrada: {"a": 1, "b": 2, "c": 2}
Saída: 5

Entrada: {"a": 10, "b": 50, "c": 5}
Saída: 65

Entrada: {}
Saída: 0

Entrada: {1: 1, 200: 2}
Saída: 3

Entrada: {1: -10, 200: 10}
Saída: 0
"""
def soma_valores(dicionario):
  soma = 0
  # se o dicionario estiver vazio retorna 0
  if len(dicionario) == 0:
    return soma
  # do contrário soma os valores do dicionário
  else:
    for num in dicionario.values():
      soma += num
    return soma

dicionario_n = {"a": 1, "b": 2, "c": 2}
soma_valores(dicionario_n)
