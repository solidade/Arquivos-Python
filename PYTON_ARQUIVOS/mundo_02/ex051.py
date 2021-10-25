# CONSTRUINDO UMA PROGRESSÂO ARITIMETICA
import time
# Cabeçalho
print('\033[1:31m-=-\033[m' * 13)
print('\033[1:35mCONSTRUINDO UMA PROGRESSÂO ARITIMETICA\033[m')
print('\033[1:31m-=-\033[m' * 13)
# Variáveis
pt = int(input("Digite o primeiro valor da PA: "))
r = int(input("Agora digite a razão da PA: "))
u = pt + (r * 10)
print("\033[1:31mOK! Vou te dar os 10 primeiros termos da sua PA:\033[m")
time.sleep(1)
# Estrutura de laço
for c in range(pt, u, r):
    print(c)
