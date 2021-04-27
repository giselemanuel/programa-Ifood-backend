uso_mascara = str(input('Você pegou a máscara [S/N]: ')).upper().strip()
uso_gel = str(input('Você pegou o álcool gel [S/N]:  ')).upper()

if uso_mascara == 'S' and uso_gel == 'S':
    print('Você pode sair de casa!')
elif uso_mascara == 'S' and uso_gel == 'N':
    print('Volte e pegue o alcool gel!')
elif uso_mascara == 'N' and uso_gel == 'S':
    print('Volte e pegue a máscara.')    
else:
    print('Pegue a máscara e o álcool gel antes de sair de casa.')