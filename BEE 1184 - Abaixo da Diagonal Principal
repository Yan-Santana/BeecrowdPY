lst_matriz = []
op = input()  # "S" ou "M"

for i in range(12):
    lst_linha = []

    for j in range(12):
        lst_linha.append(float(input()))
    lst_matriz.append(lst_linha)

n = 0  # contador verde para elementos de interesse
soma = 0  # Variavel soma para armazenar a soma dos elementos de interesse
for i in range(1, 12):
    for j in range(0, i):  # para j de 0 a i-1
        soma += lst_matriz[i][j]
        n += 1

if op == 'S':
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/n))
