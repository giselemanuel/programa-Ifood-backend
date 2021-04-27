"""
Descrição
Nesta atividade você terá que adicionar uma chave e um valor à um dicionário que já existe na função.
O dicionário que já existe: {"1+1": 2, "1+2": 3}.
O par de chave valor que deve ser adicionado: {"1+3": 4}
Instruções
Crie uma função chamada adicionar_chave_e_valor que não recebe nenhum parâmetro
Implemente uma lógica para adicionar o par de chave e valor {"1+3": 4} ao dicionário
O retorno da função deve ser o dicionário com o novo par de chave e valor adicionado
Exemplos
Saída: {"1+1": 2, "1+2": 3, "1+3": 4}
"""

def adiciona_chave_e_valor():
    dicionario = {"1+1": 2, "1+2": 3}
    dicionario['1+3'] = 4
    return dicionario