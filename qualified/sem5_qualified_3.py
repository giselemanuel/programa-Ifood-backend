"""
Descrição
Escreva uma função que receba um array(lista) de 10 números inteiros (entre 0 e 9) . Esta função deve retornar uma string na qual esses números formam um número de telefone (estilo americano como no exemplo).

Exemplos
Entrada: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Saída: "(123) 456-7890"

Entrada: [3, 2, 1, 1, 2, 3, 0, 0, 0, 9]
Saída: "(321) 123-0009"
Em código:

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])  # => retorna "(123) 456-7890"

create_phone_number([3, 2, 1, 1, 2, 3, 0, 0, 0, 9])  # => retorna "(321) 123-0009"
"""
# função que cria layout do telefone
def create_phone_number(lista):
  t1 = []
  t2 = []
  t3 = []
# cria a primeira parte do telefone (XXX)
    
  t1.append("(")
  for p1 in lista[:3]:
    #t1.append(str(p1))
    t1.append(p1)
       #print(f'{p1}', end='')
  t1.append(") ")

# cria a segunda parte do telefone (-YYY)
  for p2 in lista[3:6]:
    t2.append(p2)
        #print(p2, end='')
  t2.append('-')

#cria a terceira parte do telefone (-ZZZ)
  for p3 in lista[6:11]:
    t3.append(p3)
      #print(p3, end='')

# une todas as partes    
  tel = t1 + t2  + t3
  telefone = ''.join(map(str, tel))
  print(telefone)
  return telefone

# declaração da lista
num = [3, 2, 1, 7, 2, 3, 0, 0, 0, 9]
# chama a função
create_phone_number(num)

