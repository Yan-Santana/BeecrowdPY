
lst_matriz = []

col = int(input())
op = input()

for i in range(12):
    lst_linha = []
    for j in range(12):
        lst_linha.append(float(input()))
    lst_matriz.append(lst_linha)
soma = 0.0
for i in range(12):
    soma += lst_matriz[i][col]

if op == 'S':
    print("{0:.1f}".format(soma))
else:
    print("{0:.1f}".format(soma/12))


