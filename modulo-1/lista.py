"""
lista_de_compras = ['Maça', 'Uva', 'Requeijão', 'Banana']
dicionario_churras = {'Carne', 'Cerveja', 'Gelo'} 
tupla_num = (1, 7, 5, 9, 0)
print(lista_de_compras)
print(dicionario_churras)
print(tupla_num)
"""

"""

linguagem = ["Python", "R", "Julia", "Lua", "SQL"]
linguagem.append('Scala')
print(linguagem)
linguagem.pop() 
print(linguagem)
linguagem.insert(0,'C++') # insere algo em uma posição
print(linguagem)
linguagem.remove("Python") #  remove um item
print(linguagem)
print('\n')


num = [1, 1, 100, 11, 4, 55,  9]
print(num)
print(num[:3]) # limita uma faixa que será exibida
print(num[2:3]) # limita uma faixa que será exibida [inicio | fim]
print(num[ : : 2]) # imprime pulando um número [inicio | final | em quantos]
num.sort()
print(num)
num.reverse()
print(num)
print(num.count(1))

"""


num = []
for c in range(0,3):
    num.append (int(input('Digite um numero: ')))
print(num)