# Bee 2419 Costa
linha1, coluna1 = input().split()
linha = int(linha1)
coluna = int(coluna1)

matriz = []
for i in range(linha):
    lin = input()
    matriz.append(list(lin))

cont = 0

for i in range(linha):
    for j in range(coluna):
        if matriz[i][j] == '#':
            if matriz[i][j+1]:
                cont += 1
print(cont)
