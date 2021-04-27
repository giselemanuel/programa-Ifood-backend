"""
Descrição
Nesta atividade você vai criar a mesma função da atividade Pódio Olímpico Versão 1, mas com uma diferença: agora os corredores terão nomes! Ninguém quer ganhar uma medalha olímpica e continua desconhecido, certo?

Instruções
Crie uma função chamada podio_olimpico() que recebe 3 parâmetros: tempo_chegada1, tempo_chegada2,tempo_chegada3, nome_corredor1, nome_corredor2 e nome_corredor3.
Implemente a lógica da função para ordenar de forma crescente os tempos de corrida.
No final da função, você deve retornar um string que representa o pódio olímpico como descrito na seção Importante desta atividade.
Importante

A função deve retornar uma string com a ordem dos competidores exatamente no seguinte formato:

1 - Nome do corredor que chegou em primeiro - X minutos
2 - Nome do corredor que chegou em segundo - Y minutos
3 - Nome do corredor que chegou em terceiro - Z minutos
Exemplo

tempo_chegada1 = 120
tempo_chegada2 = 90
tempo_chegada3 = 110
nome_corredor1 = "Ronaldo"
nome_corredor2 = "Wanderlei Cordeiro de Lima"
nome_corredor3 = "Eliud Kipchoge"
Retorno esperado da função:

1 - Wanderlei Cordeiro de Lima - 90 minutos
2 - Eliud Kipchoge - 110 minutos
3 - Ronaldo - 120 minutos
"""

def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
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
    return print(f'1 - {nome_corredor2} - {posicao1} minutos' + '\n' + f'2 - {nome_corredor3} - {posicao2} minutos' + '\n' + f'3 - {nome_corredor1} - {posicao3} minutos')
   
  
podio_olimpico(120, 90, 110, "Ronaldo", "Wanderlei Cordeiro de Lima", "Eliud Kipchoge")