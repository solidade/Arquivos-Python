from time import sleep
print('\033[31m=-=\033[m' * 10)
print('\033[33mANALISANDO DADOS DE UM GRUPO\033[m')
print('\033[31m=-=\033[m' * 10)
ci = csm = csf = csfi = 0
while True:
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = str(input(f'Qual o sexo de {nome}? [M / F]: ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input(f'Qual o sexo de {nome}? [M / F]: ')).upper().strip()[0]
    print('---' * 12)
    continuar = str(input('Deseja continuar? [S / N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S / N]: ')).upper().strip()[0]
    if sexo == 'M':
        csm = csm + 1
    if sexo == 'F':
        csf = csf + 1
        if idade < 20:
            csfi = csfi + 1
    if idade > 18:
        ci = ci + 1
    if continuar == 'N':
        break
    print('---' * 12)
print('ANALISANDO DADOS...')
sleep(4)
print(f'Dentre as pessoas cadastradas {ci} tem mais de 18 anos.')
print(f'O total de pessoas do sexo masculino equivale a {csm}.')
print(f'E existem {csf} mulheres, {csfi} com idade inferior a 20 anos.')
