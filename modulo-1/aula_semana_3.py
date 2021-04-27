"""
resp = int(input('Qual a sua idade: '))

if resp >= 18 and resp <= 65:
    print('Você é obrigada a votar!')
else:
    print('Você não é obrigado a votar!')

print('------')
"""

print('1. Idoso')
print('2. Indigena')
print('3. Profissional da área da saúde')
print('4. Nenhuma das  opções')
op = int(input('Digite sua opção: '))

while op < 1 or op > 4:
    print('Você selecionou uma opção inválida.')
    print('1. Idoso')
    print('2. Indigena')
    print('3. Profissional da área da saúde')
    print('4. Nenhuma das  opções')
    op = int(input('Digite sua opção: '))
    print('-\n')
    

if op == 1 or op == 2 or op ==3:
    print('Você tem direito a prioridade a vacina.')
else:
    print('Infelizmente, você não tem direito a vacina. ')