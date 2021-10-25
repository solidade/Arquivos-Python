# CONTAGEM REGRESSIVA DOS FOGOS DE ARTIFICIO

# IMPORTANDO BIBLIOTECAS
import time

# CABEÇALHO
print('\033[1:31m-=-\033[m' * 15)
print('\033[1:35mCONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIO\033[m')
print('\033[1:31m-=-\033[m' * 15)

# ESTRUTURA DE REPETIÇÃO COM LAÇO for
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
time.sleep(1)
print('\033[1:31m{}\033[m \033[1:35mFeliz Ano Novo!!\033[m \033[1:31m{}\033[m'.format('\U0001f386', '\U0001f386'))
