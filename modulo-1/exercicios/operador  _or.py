febre = str(input('Você esta com febre [S/N]: ')).upper().strip()
tosse = str(input('Você esta com tosse [S/N]: ')).upper().strip()
   
if febre == 'S' or tosse == 'S':
    print('Você precisa ficar isolado.')
else:
    print('Você pode sair de casa, seguindo as orinetações de segurança.')