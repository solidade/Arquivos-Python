# Variáveis com códigos de cores!
vermelho, amarelo, azul1, lilas, azul, fim = '\033[1:31m', '\033[1:33m', '\033[1:34m', '\033[1:35m', \
                                             '\033[1:36m', '\033[m'
# Cabeçalho
print(vermelho, '-=-' * 9, fim)
print(azul, 'LENDO O SEXO DE UMA PESSOA', azul)
print(vermelho, '-=-' * 9, fim)

# Laço com while | SUPER GAMBIARRA KKKKKKKKKKKK
sexo = str(input('Qual o seu sexo? [M / F]: ')).upper().strip()[0]
while sexo != 'F':
    if sexo == 'M':
        print('Ok! Você é HOMEM')
        quit()
    else:
        sexo = str(input('Algo deu errado!\nQual o seu sexo? [M / F]: ')).upper().strip()[0]
print('Ok! você é MULHER')
# CORRIGINDO A GAMBIARRA!!!!!!!!!
#while sexo not in 'MmFf':
#   sexo = str(input('Algo deu errado!\nQual o seu sexo? [M / F]: ')).upper().strip()[0]
#print('Sexo {} registrado com sucesso!'.format(sexo))

