"""
Descrição
Nesta atividade você deve criar uma função que recebe os tempos(em minutos) de corrida de 3 competidores de uma maratona olímpica e exibe a ordem de chegada seguida de seu respectivo tempo de corrida.

A ordem deve ser crescente(do menor para o maior)
Instruções
Crie uma função chamada podio_olimpico() que recebe 3 parâmetros: tempo_chegada1, tempo_chegada2 e tempo_chegada3.
Implemente a lógica da função para ordenar de forma crescente os tempos de corrida.
No final da função, você deve retornar um string que representa o pódio olímpico como descrito na seção Importante desta atividade.
Importante

A função deve retornar uma string com a ordem dos competidores exatamente no seguinte formato:

1 - X minutos
2 - Y minutos
3 - Z minutos
Exemplo

tempo_chegada1 = 120
tempo_chegada2 = 90
tempo_chegada3 = 110
Retorno esperado da função:

1 - 90 minutos
2 - 110 minutos
3 - 120 minutos
"""

def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    # Implemente aqui a lógica da função
    posicao1 = posicao2 = posicao3 = tempo_chegada1
    if tempo_chegada1 > tempo_chegada2 > tempo_chegada3:
        posicao1 = tempo_chegada3
        posicao2 = tempo_chegada2
        posicao3 = tempo_chegada1
    if tempo_chegada1 > tempo_chegada3 > tempo_chegada2:
        posicao1 = tempo_chegada2
        posicao2 = tempo_chegada3
        posicao3 = tempo_chegada1
    if tempo_chegada2 > tempo_chegada1 > tempo_chegada3:
        posicao1 = tempo_chegada3
        posicao2 = tempo_chegada1
        posicao3 = tempo_chegada2
    if tempo_chegada2 > tempo_chegada3 > tempo_chegada1:
        posicao1 = tempo_chegada1
        posicao2 = tempo_chegada3
        posicao3 = tempo_chegada2
    if tempo_chegada3 > tempo_chegada1 > tempo_chegada2:
        posicao1 = tempo_chegada2
        posicao2 = tempo_chegada1
        posicao3 = tempo_chegada3
    if tempo_chegada3 > tempo_chegada2 > tempo_chegada1:
        posicao1 = tempo_chegada1
        posicao2 = tempo_chegada2
        posicao3 = tempo_chegada2

    #podio = "1 - {p1} minutos\n2 - {p2} minutos\n3 - {p3} minutos"
    return print(f'1 - {posicao1} minutos' + '\n' + f'2 - {posicao2} minutos' + '\n' + f'3 - {posicao3} minutos')
   
  
podio_olimpico(120, 90, 110)