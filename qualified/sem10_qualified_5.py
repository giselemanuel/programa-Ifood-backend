"""
Descrição
Implemente a função balanceado(texto) que recebe uma string contendo uma série de parênteses - ( e ) - e retorna se os parênteses estão balanceados ou não.

A função deve dizer se todos os parênteses que são abertos possuem um correspondente para fechá-los.

Existem várias formas de implementar esta função. Tente utilizar o conhecimento adquirido até sobre todas as estruturas de dados para pensar numa boa solução.

Não há restrição em relação às ferramentas da linguagem que podem ser utilizadas.

Exemplos

Chamada da função balanceado(texto)
Entrada: "(2+3+4) * 3"
Saída: True

Entrada: "(()))"
Saída: False

Entrada: "((())"
Saída: False

Entrada: "("
Saída: False

Entrada: "2 + 3"
Saída: True

Entrada: "(a / 2) * ((3 * 1) / 9)"
Saída: True

Entrada: ""
Saída: True
"""


# Função -------------------------------------------------------
def balanceado(texto):
    abre_lista = []  # lista com pararenteses (
    fecha_lista = []  # lista com pararenteses )

# iteração para validar os itens da lista -------------------
    for item in texto:
        if texto[0] == ')':
            return False
        elif item == '(':
            abre_lista.append(item)
        elif item == ')':
            fecha_lista.append(item)

# verifica se os paranteses estão balanceados --------------
    if len(abre_lista) == len(fecha_lista):
        return True
    else:
        return False


# definição da variável ---------------------------------------
string_texto = "(()))"

# chama função -------------------------------------------------
balanceado(string_texto)