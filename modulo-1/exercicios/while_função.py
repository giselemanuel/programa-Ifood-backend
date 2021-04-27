"""
Programa VamoAI:
Aluna: Gisele Rodrigues Manuel
Atividade : Estrutura de repetição
Descrição do Exercício 
Criar um While com pelo menos uma função;
"""

def cadastrar_produto():
    while True:
        nome = str(input("Digite o nome do produto: "))
        preco = float(input("Digite o valor do produto R$ "))
        resposta = str(input("Deseja cadstrar outro produto [S/N]: ")).upper()
        print("---")
        if resposta == "S":
            continue
        else:
            print("Cadastro realizado com sucesso !")
            break
    

def cabecalho_programa():
    print('-' * 30)
    print(f'{"Cadastro de produtos":^30}')
    print('-' * 30)

cabecalho_programa()
cadastrar_produto()