"""
Descrição
Utilizando as mesmas 4 funções da atividade Pilha - Funções Básicas:

cria_pilha()
tamanho(pilha)
adiciona(pilha, valor)
remove(pilha):
Implemente a função palindromo(texto) que recebe um texto(string) como parâmetro e retorna True se o texto é um palíndromo ou False caso contrário.

Um palíndromo é um texto que pode ser lido tanto da esquerda pra direita quanto da direita pra esquerda, contendo o mesmo conteúdo.

Exemplos: arara, ama, abba, ...

Utilize o funcionamento da pilha para que isso aconteça.

Lembre-se:

A pilha funciona seguindo a sequência LIFO(Last In First Out) - Último a entrar, primeiro a sair.
Em python, a pilha é implementada utilizando a estrutura de uma lista.
IMPORTANTE

É OBRIGATÓRIO utilizar pelo menos as funções cria_pilha, adiciona e remove da atividade anterior para implementar a função palindromo. Seu código não passará nos testes se elas não forem utilizadas.

Exemplos

Chamada da função palindromo(texto)
Entrada: "arara"
Saída: True

Entrada: ""
Saída: True

Entrada: "a"
Saída: True

Entrada: "aAbA"
Saída: False

Entrada: "acac"
Saída: False

"""


# função cria_pilha ---------------------------------
def cria_pilha():
    nova_pilha = []
    return nova_pilha


# função tamanho ------------------------------------
def tamanho(pilha):
    return len(pilha)


# função adiciona------------------------------------
def adiciona(pilha, elemento):
    pilha.append(elemento)
    return pilha


# função remove -------------------------------------
def remove(pilha):
    if len(pilha) == 0:
        pilha = None
        return pilha
    else:
        removido = pilha.pop()
        return removido


# função palindromo ---------------------------------
def palindromo(s):
    # nova_pilha = []
    cria_pilha()  # chama função cria_pilha
    if s == '':  # verifica se a string é vzia
        return True

    elif s != '':  # verifica se é um palindromo
        if len(s) > 0:
            inverso = s[::-1]
            if inverso == s:
                adiciona(nova_pilha, s)  # chama função adiciona
                return True
            else:
                nova_pilha.append(s)
                remove(nova_pilha)  # chama função remove
                return False


# declara variáveis --------------------------------
texto = "arara"
nova_pilha = cria_pilha()  # define variável global

# chama função -------------------------------------
palindromo(texto)