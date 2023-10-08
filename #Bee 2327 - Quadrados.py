#Bee 2327 - Quadrados

# Função sem parâmetro formal e com valor de retorno int
def ler_dim():
    """
    Função que lê a dimensão da matriz e a retorna.
    """
    '''
    dim = int(input())
    return dim
    '''
    return int(input())

# Função com um parâmetro formal e o retorno de uma matriz
def ler_criar_matriz(dim):
    """
    Recebe a dimensão da matriz quadrada, lê
    cada linha, transforma cada valor da linha em int,
    insere a linha na matriz.
    Ao final, retorna a matriz criada.
    """
    mat = []
    for i in range(dim):
        lstr = input().split()
        lint = [0]*dim
        for j in range(dim):
            lint[j] = int(lstr[j])
        mat.append(lint) # mat += [lint]
    return mat

# Função com dois parâmetros formais e o retorno de uma lista
def calcular_somas(M, dim):
    """
    Recebe a matriz quadrada M de dimensão dim, calcula
    as somas de linhas, colunas e diagonais, e as retorna.
    """
    lins = dim*[0]
    cols = dim*[0]
    dp = 0
    ds = 0
    cds = dim - 1
    
    for i in range(dim):
        for j in range(dim):
            lins[i] += M[i][j]
            cols[j] += M[i][j]
        dp += M[i][i]
        ds += M[i][cds]
        cds -= 1
        
    return [lins, cols, dp, ds]

# Função com 5 parâmetros formais e retorno da soma
def verificar(sl, sc, sdp, sds, dim):
    qm = True
    if sdp != sds:
        qm = False
    if qm == True:
        for k in range(dim):
            if sdp != sl[k] or sdp != sc[k]:
                qm = False
                break
    if qm:
        return sds
    return -1

# Ler a dimensão n da matriz quadrada Q
n = ler_dim()

# Ler as linhas da matriz Q, transformar cada valor
# de cada linha em inteiro e inserir cada linha em Q
Q = ler_criar_matriz(n)

# Calcular as somas de cada linha, de cada coluna
# e das diagonais principal e secundária de Q
s_lin, s_col, s_dp, s_ds = calcular_somas(Q, n)

# Verificar se todas as somas calculadas são iguais.
# Mostrar uma das somas caso o quadrado seja mágico,
# ou mostrar -1, caso contrário.
print(verificar(s_lin, s_col, s_dp, s_ds, n))