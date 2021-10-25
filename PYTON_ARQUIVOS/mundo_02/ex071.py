# SIMULANDO CAIXA ELETRÔNICO
from time import sleep
print('\033[31m=-=\033[m' * 10)
print('\033[33mSIMULANDO CAIXA ELETRÔNICO\033[m')
print('\033[31m=-=\033[m' * 10)

valorSaque = int(input('Qual valor deseja sacar? R$'))
print('===' * 10)
v = valorSaque % 50
r = valorSaque % 20
z = valorSaque % 10
v1 = valorSaque // 50
r1 = valorSaque // 20
z1 = valorSaque // 10
while True:
    if valorSaque < 50:
        if valorSaque < 20:
            if valorSaque < 10:
                if valorSaque <= 0:
                    print('Tente um valor acima de 0! Obrigado!')
                    break
                print(f'Total de {valorSaque} de cédulas de R$1')
                break
            else:
                if valorSaque == 10:
                    print(f'Total de {z1} cédulas de R$10')
                    break
                print(f'Total de {z1} cédulas de R$10')
                print(f'Total de {z} cédulas de R$1')
                break
        else:
            if valorSaque == 20:
                print(f'Total de {r1} cédulas de R$20')
                break
            print(f'Total de {r1} cédulas de R$20')
            if r < 20:
                if r < 10:
                    if r == 0:
                        break
                    print(f'Total de {r} cédulas de R$1')
                    break
                else:
                    if r == 10:
                        print(f'Total de {r // 10} cédulas de R$10')
                        break
                    print(f'Total de {r // 10} cédulas de R$10')
                    if r % 10 > 0:
                        print(f'Total de {r % 10} cédulas de R$1')
                        break
            else:
                if r == 20:
                    print(f'Total de {r // 20} cédulas de R$20')
                    break
                print(f'Total de {r // 20} cédulas de R$20')
                if r % 20 > 0:
                    print(f'Total de {r % 20} cédulas de R$1')
                    break
    else:
        print(f'Total de {v1} cédulas de R$50')
        if v < 20:
            if v < 10:
                if v == 0:
                    break
                print(f'Total de {v} cédulas de R$1')
                break
            else:
                print(f'Total de {v // 10} cédulas de R$10')
                if v == 10:
                    break
                print(f'Total de {v % 10} cédulas de R$1')
                break
        else:
            print(f'Total de {v // 20} cédulas de R$20')
            if v == 20:
                break
            else:
                if v % 20 == 10:
                    print(f'Total de {(v % 20) // 10} cédulas de R$10')
                    break
                else:
                    if v % 20 < 10:
                        if v % 20 > 0:
                            print(f'Total de {v % 20} cédulas de R$1')
                        break
                    else:
                        print(f'Total de {(v % 20) // 10} cédulas de R$10')
                        print(f'Total de {(v % 20) % 10} cédulas de R$1')
                        break
print('===' * 10)
print('\033[34mVolte sempre ao Banco MSP! Tenha um bom dia!\033[m')
