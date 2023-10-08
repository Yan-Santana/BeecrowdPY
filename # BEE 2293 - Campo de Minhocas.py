# BEE 2293 - Campo de Minhocas

def criaMatriz_int(linha,coluna):
    mat = []
    for i in range(linha):
        lin = input().split()
        lin_int  = coluna * [0]
        for j in range(coluna):
            lin_int[j] = int(lin[j])
        mat.append(lin_int)
    return mat
#>>><><><><><><><><><><><><><><><><><><><><><><><><>><><><><
def somaLinha_coluna(linhaa, colunaa, mat):
    soma_linha = linhaa*[0]
    soma_coluna = colunaa*[0]

    for i in range(linhaa):
        for j in range(colunaa):
            soma_linha[i] += mat[i][j]
            soma_coluna[j] += mat[i][j]
    return soma_linha, soma_coluna
#>>><><><><><><><><><><><><><><><><><><><><><><><><>><><><><

linha1, coluna1 = input().split()
linha = int(linha1)
coluna = int(coluna1)

matriz = criaMatriz_int(linha, coluna)

soma_linha = somaLinha_coluna(linha, coluna, matriz)[0]
soma_coluna = somaLinha_coluna(linha, coluna, matriz)[1]

maior_linha = int(soma_linha[0])
maior_coluna = int(soma_coluna[0])

for c in range(len(soma_linha)):
    if soma_linha[c] > maior_linha:
        maior_linha = soma_linha[c] 

for i in range(len(soma_coluna)):
    if soma_coluna[i] > maior_coluna:
        maior_coluna = soma_coluna[i]
        
maior = 0
if maior_linha > maior_coluna:
    maior = maior_linha
else:
    maior = maior_coluna
print(maior)
