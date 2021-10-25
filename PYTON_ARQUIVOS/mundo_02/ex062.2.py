from time import sleep
# Cabeçalho
print('\033[1:31m-=-\033[m' * 13)
print('\033[1:35mCONSTRUINDO UMA PROGRESSÂO ARITIMETICA x3\033[m')
print('\033[1:31m-=-\033[m' * 13)
# Variáveis
pt = int(input("Digite o primeiro valor da PA: "))
r = int(input("Agora digite a razão da PA: "))
termo = pt
cont = 1
total = 0
mais = 10
print("\033[1:31mOK! Vou te dar os 10 primeiros termos da sua PA:\033[m")
sleep(1)
# Estrutura de laço while
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} --> '.format(termo), end='')
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Deseja mais termos desta PA? Quantos? '))
print('PA finalizada com {} termos mostrados'.format(total))