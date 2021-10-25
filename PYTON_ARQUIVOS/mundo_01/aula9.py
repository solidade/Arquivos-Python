frase = "Eu tenho um lapis de cor"
print(frase[0:2])
print(frase[0:25])
print(frase[0:25:2])  # Esse 2 no final faz com que pegue um caractere e outro não, alternando.
print(frase[9::3])  #mesma coisa do anterior. Começa no 9, vai até o final pulando 3 letras
print(frase[:9])
print(frase[18:])
# Além das operações de fatiamento, temos as seguintes operações de análise:
print(len(frase))  # conta a quantidade de caracteres na frase, incluindo espaços (inicia em 0)
print(frase.count('o'))  # conta quantas vezes um caractere se repete na frase
print(frase.count('o', 0, 13))  # mescla contagem e fatiamento. Só contará o caractere 'o' do 0 ao 12
print(frase.find('pis'))  # vai procurar 'pis' na frase e mostrar onde inicia.
print('um' in frase)  # vai mostar se 'um' existe dentro da frase
print(frase.replace('lapis', 'giz'))  # vai substituir uma palavra ou caractere na frase
print(frase.upper())  # torna a frase ou trecho maiscula. frase.lower() menúscula, e
# frase.capitalize() maiúscula na primeira letra da frase, e frase.title() maiúscula no inicio da cada palavra
frase.strip()  # remove espaços inúteis antes e depois da frase, caso existam.
frase.rstrip()  # remove apenas espaços inúveis a direita. r de right
frase.lstrip()  # remove apenas espaços inúteis a esquerda. l de left
frase.split()  # gera uma nova lista com todas as palavras dentro da frase. É como se dividisse a frase nos espaços
' '.join(frase)  # faz o oposto do split, ele junta as palavras em uma frase, 
# pode-se colocar pontos ou traços para separa-las colocando-os entre aspas




