"""
Crie um programa:
1. Solicite para o usuário 3 notas
2. Calcule a média.
3. Informe ao usuário se ele foi aprovado ou reprovado. 
4. Considerar que media >= 5 aprovado, media < 5 reprovado.
"""

print('\n')
print('-' * 40)
print(f'{"Programa : Calcula média":^40}')
print('-' * 40)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda: '))
nota3 = float(input('Digite a terceira: '))

media = (nota1 + nota2 + nota3)/3

if media >= 5:
    print(f'Sua média é {media:.2f}, você foi aprovado!')

else:
    print(f'Sua média é {media:.2f}, você foi reprovado!')
