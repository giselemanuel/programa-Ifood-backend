"""
Fantasma Cor
Descrição
Crie uma classe chamada de Fantasma que possui apenas um atributo: cor.

Objetos Fantasma são instanciados sem nenhum argumento.

O atributo cor do objeto deve ser inicializado uma cor aleatória entre as opções "branco", "amarelo", "roxo" e "vermelho".

Dica: Utilize o módulo random do python para geração de números aleatórios.

Exemplos
fantasma = Fantasma()
fantasma.cor  #=> "branco" ou "amarelo" ou "roxo" ou "vermelho
"""

# importação da biblioteca random para utilizar a função random.choice para escolher uma cor aleatória
import random

# Classe fantasma ----------------------------------------------
class Fantasma():
    def __init__(self, cor=""):
      lista_cores = ["branco", "amarelo", "roxo", "vermelho"]
      self.cor = random.choice(lista_cores)
      
# Objeto fantasma instanciado na classe pessoa -----------------
fantasma = Fantasma()

# solicita o atributo cor da instancia fantasma---------------
fantasma.cor

