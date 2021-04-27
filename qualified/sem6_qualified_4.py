"""
Instruções
Crie uma função com a seguinte assinatura verifica_chave(dicionario, chave) que recebe um dicionário e um valor qualquer como parâmetro
Implemente uma lógica para checar se a chave passada como parâmetro já existe no dicionário
Se a chave existir no dicionário, a função deve retornar o booleano True
Caso contrário, deve retornar o booleanno False
Exemplos
Entrada: {"a": 1, "b": 2, "c": 2}, "a"
Saída: True

Entrada: {"a": 1, "b": 2, "c": 2}, "d"
Saída: False

Entrada: {}, "d"
Saída: False

Entrada: {1: 1, 2: 2}, 1
Saída: True
"""

def verifica_chave(dicionario, chave):
  # valida se a chave existe no dicionário
  if chave in dicionario:
    return True
  else:
    return False
    
dicionario_n = {"a": 1, "b": 2, "c": 2}
valor = "a"
# chama função e passa os paramêtros
verifica_chave(dicionario_n, valor)