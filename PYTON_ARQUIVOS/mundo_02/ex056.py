#Cabeçalho
print('\033[1:31m-=-\033[m' * 10)
print('\033[1:35mANALISANDO PERFIS DE IDADE\033[m')
print('\033[1:31m-=-\033[m' * 10)

# VARIAVEIS:
sid = 0
mid = 0
mv = 0
mvn = 0
cont = 0
for c in range(1, 5):
    print('----- {} PESSOA -----'.format(c))
    nome = str(input('Nome: '))
    sexo = str(input('Sexo [F / M]: ')).upper()
    idade = int(input('Idade: '))
    sid = sid + idade
    if c == 1 and sexo == 'M':
        mv = idade
        mvn = nome
    if sexo == 'M' and idade > mv:
        mv = idade
        mvn = nome
    if sexo == 'F' and idade < 20:
        cont = cont + 1
mid = sid / 4
print('A média de idade deste grupo de pessoas é {} anos'.format(mid))
print('O homem mais velhor tem {} anos e se chama {}'.format(mv, mvn))
print('Existem {} mulheres com idade inferior a 20 anos'.format(cont))
