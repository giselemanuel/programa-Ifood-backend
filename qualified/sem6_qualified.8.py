"""
Nesta atividade você terá que criar uma função para verificar se a chave do dicionário existe em seus valores.
Cada valor dos pares chave:valor do seu dicionário será uma lista.
O objetivo é verificar se a chave está dentro de sua respectiva lista.
Ao final, sua função deverá ter construído um novo dicionário, onde as chaves são iguais ao dicionário original, mas seus valores deverão ser True ou False. 
True se a chave foi encontrada em seu respectivo valor(lista) ou False caso contrário.
Para mais detalhes, ver os exemplos.

Instruções
Crie uma função com a seguinte assinatura procura_chave_na_lista(dicionario) que recebe um dicionário como parâmetro, onde cada valor é uma lista
Implemente uma lógica para verificar se a chave está dentro de sua respectiva lista.
Sua função deverá retornar um dicionário, onde as chaves são iguais ao dicionário original, mas seus valores deverão ser True ou False
Se o dicionário recebido estiver vazio, o retorno deverá ser um dicionário vazio
Exemplos
Entrada: {"a": ["a", "b", "c"], "b": [1, 2, 3, "b"]}
Saída: {"a": True, "b": True}

Entrada: {1: [0, 5, 10], 3: [1, 2, 3, "b"]}
Saída: {1: False, 3: True}

Entrada: {1: [], 3: []}
Saída: {1: False, 3: False}

Entrada: {}
Saída: {}
"""

def procura_chave_na_lista(dicionario):
    # retorna dicionário vazio se for igual a zero
    if len(dicionario) == 0:
      return dicionario
    else:
      # iteração no for será nos items () considerando as variaveis chave e valor
        for chave , valor in dicionario.items():
            if chave in valor: # verifica se a chave existe na lista de valor
                # substitui a parte de valor por True
                dicionario[chave] = True               
            else: 
                # substitui a parte de valor por False
                dicionario[chave] = False
        return dicionario
                     
dicionario_n = {1: [0, 5, 10], 3: [1, 2, 3, "b"]}
procura_chave_na_lista(dicionario_n)