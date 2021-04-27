"""
Acumulador
Descrição
Escreva uma função chamada summation que recebe num como parâmetro e soma todos os números positivos de 1 até num.
A função deve retornar o resultado desta soma.

Obs: O parâmetro num sempre será um número inteiro positivo!

Exemplos
Entrada: 2
Saída: 1 + 2 -> 3 

Entrada: 8
Saída: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 -> 36

"""
# função de soma 
def summation(num):
    soma = 0
    # soma todos o números até a variável numero
    for s in range (1,num+1):
      soma = soma + s
    # imprime a soma
    print(soma)
    return soma
  
# define variável
numero = 8
# chama função
summation(numero)