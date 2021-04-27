"""
Descrição
Crie uma função chamada reverse_string que recebe uma string a retorna de forma invertida.

Lembre-se: Uma string é uma lista de caracteres!

Exemplos

Entrada: "abc123"
Saída: "321cba"

Entrada: "hello"
Saída: "olleh"

Entrada: "arara"
Saída: "arara"
"""
# função exibe o inverso da string
def reverse_string(str):
    # exibe o inverso da string
    return str[::-1]
   
# definição da string
palavra = 'abc123'
# chama a função
reverse_string(palavra)