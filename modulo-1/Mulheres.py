"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Desafio : Grande Mulheres em STEM
Descrição do Exercício 4:
1. Você deverá pesquisar sobre uma mulher que revolucionou alguma das áreas de STEM (ciência, tecnologia, engenharia e matemática);
2.Desenvolver um algoritmo que contenha três perguntas de múltipla escolha sobre a mulher que você pesquisou;
3.Tenha em cada pergunta duas alternativas corretas e considere, caso a pessoa usuária escolha qualquer uma, que ela acertou a questão;
4. Mostre na tela, ao final, a quantidade de perguntas que ela acertou e um resumo sobre a mulher que você pesquisou.
"""

# cabeçalho do programa
print('*' * 75)
print(f'\033[36m{"QUIZ - Mulheres de STEM ":^75}\033[m')
print('*' * 75)
print("\nEste Quiz é sobre Valerie Thomas que revolucionou a área STEM,\nserão 3 perguntas com duas alternativas corretas,\nserá que você acerta uma delas?\n")
print('*' * 75)

cont_acertos = 0

# Pergunta 1 
print("\033[36m\nPergunta 1:\nValerie Thomas esteve presente onde:\033[m")
resposta1  = str(input('\n[A] Universidade de Maryland - UMBC\n[B] Nasa\n[C] Google\nEscolha uma alternativa: ')).strip().upper()

# Resposta 1 - Verifica alteranativas corretas, alternativas corretas A e B
if resposta1 == 'A' or resposta1 == 'B':
    print('\033[32mParabéns! a resposta esta correta !!!\033[m')
    cont_acertos += 1
else:
    print('\033[31mOps,Você errou !!!\033[m')

# Pergunta 2
print('\033[36m\nPergunta 2:\nValerie Thomas se destacou em qual curso na faculdade:\033[m')
resposta2  = str(input('\n[A] Física\n[B] Programação\n[C] Matemática\nEscolha uma alternativa: ')).strip().upper()

# Resposta 2 - Verifica alteranativas corretas, alternativas corretas A e C
if resposta2 == 'A' or resposta2 == 'C':
    print('\033[32mParabéns! a resposta esta correta !!!\033[m')
    cont_acertos += 1
else:
    print('\033[31mOps,Você errou !!!\033[m')

# Pergunta 3
print('\033[36m\nPergunta 3:\nA invenção de Valerie Thomas tem sido usado onde:\033[m')
resposta3  = str(input('\n[A] Cadeiras Ergonômicas\n[B] Desenvolvimento de telas de TV e Vídeo\n[C] Em cirurgias\nEscolha uma alternativa: ')).strip().upper()

# Resposta 3 - Verifica alteranativas corretas, alternativas corretas  B e C
if resposta3 == 'B' or resposta3 == 'C':
    print('\033[32mParabéns! a resposta esta correta !!!\033[m')
    cont_acertos += 1
else:
    print('\33[36mOps,Você errou !!!\033[m')
print()
    
#Encerrando o programa
print("*" * 75)
print(f'\n{"FIM DO QUIZ":^75}')
print(f'                         Você acertou {cont_acertos} das 3 perguntas.\n')
print("*" * 75)

texto = ''' Valerie Thomas, mulher, negra, nascida em 8 de fevereiro 
em 1943, em Marylan nos Estados Unidos,formada em Física na Universiade 
do Estado de Morgan. Após sua graduação foi trabalhar na NASA. Em 1976 ela
participou de um seminário científico onde viu uma exposição que demonstrava
uma ilusão. A exposição usava espelhos côncavos para enganar o espectador 
fazendo-o acreditar que uma lâmpada estava acesa mesmo depois de ter sido 
desparafusada de seu soquete. Ela ficou tão surpresa com o que viu neste 
seminário que queria começar a criar por conta própria. Mais tarde naquele
ano, ela começaria a fazer experiências com espelhos planos e côncavos. 
Os espelhos planos teriam um reflexo em um determinado objeto que pareceria 
estar atrás do vidro. O espelho côncavo teria um reflexo que na verdade 
estaria na frente do vidro, produzindo uma ilusão tridimensional. Com isto, 
ela foi capaz de inventar o Transmissor de Ilusão dispositivo que simula a 
aparência tridimenssional de um objeto. Em 1980 recebeu a patente de sua 
invenção. Sua invenção foi e ainda é utilizada pela Nasa, agência espacial 
onde Thomas trabalhou e foi responsável pelo desenvolvimento dos sistemas 
de processamento de imagem em formatos de mídia digital usados ​​nos primeiros 
anos do programa Landsat. '''
print(texto)
print()